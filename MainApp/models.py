from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f"{self.name}"


class Producer(models.Model):
    name = models.CharField(max_length=60, unique=True)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} ({self.country})"


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=300, blank=True)
    price = models.IntegerField(default=0)
    availability = models.BooleanField(default=True)
    producer = models.ForeignKey(Producer, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')  # category.products.all()

    def __str__(self):
        return f"{self.name} ({self.price})"


class Basket(models.Model):
    pass


class ProductBasket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # product.productbusket_set.all()
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='product_baskets')
    amount = models.IntegerField(default=1)

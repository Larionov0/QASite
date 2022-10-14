from django.shortcuts import render, HttpResponse, redirect, Http404
from .models import *
from django.contrib.auth.decorators import login_required


@login_required
def all_categories(request):
    return render(request, 'all_categories.html', context={'categories': Category.objects.all(),
                                                           'username': request.user.username})


@login_required
def create_category(request):
    data = request.GET
    name = data.get('name')
    description = data.get('description')
    Category.objects.create(name=name, description=description)
    return redirect('/main/all_categories')


@login_required
def delete_category(request, cat_id):
    Category.objects.get(id=cat_id).delete()
    return redirect('/main/all_categories')


def store(request):
    cat_id = request.GET.get('category')
    try:
        category = Category.objects.get(id=cat_id)
    except Category.DoesNotExist as exc:
        category = Category.objects.get(id=8)

    products = Product.objects.filter(category=category)
    return render(request, 'store.html', context={'categories': Category.objects.all(), 'category': category,
                                                  'products': products})

from django.shortcuts import render, HttpResponse

store = [
    {
        'name': 'pizza Margarita',
        'price': 20
    },
    {
        'name': 'Lazanga',
        'price': 35
    },
    {
        'name': 'Bolongeze',
        'price': 30
    },
    {
        'name': 'pizza Pizza',
        'price': 25
    },
]


def first_view(request):

    return HttpResponse('<p>My first view</p>')


def restaurant_view(request):
    html = '<table>' \
           '<tr><th>Name</th><th>Price</th></tr>'
    for dish in store:
        html += f'<tr><td>{dish["name"]}</td><td>{dish["price"]}</td></tr>'
    html += '</table>'
    return HttpResponse(html)


def restaurant_view2(request):
    return render(request, 'restaurant.html', context={'amount': 4, 'store': store})

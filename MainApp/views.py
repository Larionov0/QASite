from django.shortcuts import render, HttpResponse


def first_view(request):

    return HttpResponse('<p>My first view</p>')

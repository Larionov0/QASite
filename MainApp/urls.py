from django.urls import path
from . import views


urlpatterns = [
    path('first/', views.first_view),
    path('restaurant/', views.restaurant_view),
    path('restaurant2/', views.restaurant_view2),
]

from django.urls import path
from . import views


urlpatterns = [
    path('all_categories/', views.all_categories),
    path('create_category/', views.create_category),
    path('delete_category/<int:cat_id>/', views.delete_category),
    path('store/', views.store),
]

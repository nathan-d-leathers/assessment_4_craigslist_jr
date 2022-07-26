from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categories/', views.list_categories, name="categories"),
    path('categories/new/', views.add_category, name="add_category"),
    path('categories/<int:category_id>/edit/',views.edit_category, name="edit_category"),
    path('categories/<int:category_id>/posts/',views.list_posts, name="list_posts"),
    path('categories/<int:category_id>/new/', views.add_post, name="add_post"),
    path('categories/<int:category_id>/posts/<int:post_id>/view/',views.view_post, name="view_post"),
    path('categories/<int:category_id>/posts/<int:post_id>/edit/',views.edit_post, name="edit_post"),
]

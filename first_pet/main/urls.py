from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#views (as auth_views) - стандартные представления для работы с аутентификацией

app_name = 'main'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
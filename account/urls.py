from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # previous login view
    # path('login/', views.login_view, name='login'),
    # new auth view
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),

    # register and edit view
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

    # list and details in people section
    path('users/', views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/<username>/', views.user_detail, name='user_detail'),
]


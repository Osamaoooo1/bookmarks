from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('', views.image_list, name='list'),
    path('create/', views.create_image, name='create'),
    path('detials/<int:id>/<slug:slug>/', views.image_details, name='details'),
    path('like/', views.image_like, name='like'),
    path('ranking/', views.image_ranking, name='ranking'),
]

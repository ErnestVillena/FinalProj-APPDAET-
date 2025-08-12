from django.urls import path
from . import views

app_name = 'id'

urlpatterns = [
    path('', views.id_list, name='id-list'),
    path('add/', views.id_add, name='id-add'),
    path('preview/', views.id_preview, name='id-preview'),
    path('edit/<int:pk>/', views.id_edit, name='id-edit'),
    path('delete/<int:pk>/', views.id_delete, name='id-delete'),
    path('<int:pk>/', views.id_detail, name='id-detail'),
]
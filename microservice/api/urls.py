from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', views.ItemRetrieveUpdateDeleteView.as_view(), name='item-detail'),
]
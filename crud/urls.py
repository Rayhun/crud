from django.urls import path
from .views import home, create_info, update_info, delete_info

urlpatterns = [
    path('', home, name="home"),
    path('create/', create_info, name="create_info"),
    path('update/<int:pk>/', update_info, name='update_info'),
    path('delete/<int:pk>/', delete_info, name='delete_info')
]

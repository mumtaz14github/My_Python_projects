from django.urls import path
from . import views
app_name = 'todoapp'
urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:deid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update')
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('Index/', views.Index, name='Index'),

    path('add_I/', views.add_I, name='add_I'),
    path('add_E/', views.add_E, name='add_E'),

    path('update_I/<int:pk>', views.update_I, name="update_I"),
    path('update_E/<int:pk>', views.update_E, name="update_E"),

    path('delete_E/<int:pk>', views.delete_E, name="delete_E"),
    path('delete_I/<int:pk>', views.delete_I, name="delete_I"),
]
from django.urls import path
from . import views

urlpatterns =[
    path('',views.gallery, name='gallery',)
    path('photo/<str:pk>',views.viewSnap, name='phoyo',)
    path('add/',views.addSnap, name='add', )
]
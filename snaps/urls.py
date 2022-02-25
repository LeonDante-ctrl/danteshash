from django.urls import path
from . import views

urlpatterns =[
    path('',views.gallery, name='gallery'),
    path('snap/<str:pk>/',views.viewSnap, name='photo',),
    path('add/',views.addSnap, name='add' ),
]

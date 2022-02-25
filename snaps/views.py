from multiprocessing import context
from django.shortcuts import render
from .models import Category, Snaps


def gallery(request):
    categories = Category.objects.all()
    snaps = Snaps.objects.all
    context = {'categories' : categories, 'snaps':snaps}
    return render(request,'snaps/gallery.html', context)

def viewSnap(request, pk):
    snap = Snaps.objects.get(id=pk)
    return render(request,'snaps/snap.html', {'snap':snap} )

def addSnap(request):
    return render(request,'snaps/add.html')

# Create your views here.

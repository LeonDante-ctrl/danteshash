from django.shortcuts import render


def gallery(request):
    return render(request,'snaps/gallery.html')

def viewSnap(request, pk):
    return render(request,'snaps/snap.html')

def addSnap(request):
    return render(request,'snaps/add.html')

# Create your views here.

from email.mime import image
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Category, Snaps


def gallery(request):
    category = request.GET.get('category')
    if category == None:
     snaps = Snaps.objects.all()
    else:
        snaps = Snaps.objects.filter(category__name=category)
        
    categories = Category.objects.all()   
    context = {'categories' : categories, 'snaps':snaps}
    return render(request,'snaps/gallery.html', context)

def viewSnap(request, pk):
    snap = Snaps.objects.get(id=pk)
    return render(request,'snaps/snap.html', {'snap':snap} )

def addSnap(request):
    categories = Category.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('image')
        
        if data['category'] != 'none':
                category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create( name=data['category_new'])
        else:
            category = None
            
        snap = Snaps.objects.create(
                category=category,
                name=data['description'],
                image=image,
            )
        return redirect('gallery')
       # print('data:', data)
        # print('image:', image)
        
    
    context = {'categories' : categories, }
    return render(request,'snaps/add.html', context)

# Create your views here.

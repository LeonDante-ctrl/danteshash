from django.contrib import admin

# Register your models here.
from .models import Snaps, Category

admin.site.register(Category)
admin.site.register(Snaps)
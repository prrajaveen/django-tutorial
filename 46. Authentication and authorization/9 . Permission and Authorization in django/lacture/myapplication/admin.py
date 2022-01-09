from django.contrib import admin
from myapplication.models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']

admin.site.register(Blog,BlogAdmin)
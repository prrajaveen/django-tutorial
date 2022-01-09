from django.contrib import admin
from myapplication.models import Blogpost,ContactForm
# Register your models here.

@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']


@admin.register(ContactForm)
class ContactForm(admin.ModelAdmin):
    list_display=['firstname','lastname','emailaddress','message']
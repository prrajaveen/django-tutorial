from django.contrib import admin
from .models import Page
# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    #if you delete user then page is automatically deleted
    list_display=['page_name','page_cat','page_publish_date','user']
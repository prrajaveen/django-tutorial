from django.contrib import admin
from myapplication.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','desc','publish_date']
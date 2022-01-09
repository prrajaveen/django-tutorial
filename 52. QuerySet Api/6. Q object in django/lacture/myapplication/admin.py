from django.contrib import admin
from myapplication.models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city','marks','pass_date','admdatetime']

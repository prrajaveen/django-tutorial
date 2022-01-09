from django.contrib import admin
from django.db import models
from myapplication.models import Student,Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city','marks','pass_date']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','t_id','city','salary','join_date']
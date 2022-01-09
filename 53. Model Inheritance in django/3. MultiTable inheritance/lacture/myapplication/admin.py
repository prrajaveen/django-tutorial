from django.contrib import admin
from myapplication.models import ExamCenter,Student

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display=['cname','city']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll','cname','city']
# Register your models here.

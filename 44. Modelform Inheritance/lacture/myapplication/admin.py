from django.contrib import admin
from myapplication.models import User,Teacher

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')
admin.site.register(User,UserAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')

admin.site.register(Teacher,TeacherAdmin)
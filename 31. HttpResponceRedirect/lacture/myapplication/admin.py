from django.contrib import admin
from myapplication.models import Student,Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('stuid','stuname','stuemail','stupass','comment')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=('tid','tname','temail','tpass','comments')\

# admin.site.register(Teacher,TeacherAdmin)
# admin.site.register(Student,StudentAdmin)


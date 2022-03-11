from django.contrib import admin
from .models import Students,Courses

# Register your models here.


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']


admin.site.register(Students,StudentsAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_name']


admin.site.register(Courses,CourseAdmin)


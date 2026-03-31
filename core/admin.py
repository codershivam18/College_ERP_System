from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Classroom, Subject, TeacherProfile, StudentProfile, Attendance, Fee, Result

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_student', 'is_teacher', 'is_admin', 'phone', 'address', 'profile_pic')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_student', 'is_teacher', 'is_admin', 'phone', 'address', 'profile_pic')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Classroom)
admin.site.register(Subject)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
admin.site.register(Attendance)
admin.site.register(Fee)
admin.site.register(Result)

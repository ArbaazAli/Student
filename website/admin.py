from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(StudentInfo)
admin.site.register(AcademicInfo)
admin.site.register(Fees)
admin.site.register(Marks)
admin.site.register(Attendance)
admin.site.register(StaffInfo)
admin.site.register(StaffEducation)
admin.site.register(StudentLogin)
admin.site.register(StaffLogin)


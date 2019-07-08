from django.urls import path
from .import views


urlpatterns = [

    path('', views.home, name = 'Home Page'),
    path('login/', views.login, name ='Login Page'),
    path('login2/', views.login2, name ='Login2 Page'),
    path('logout/', views.logout, name ='Logout'),
    path('marks/', views.marks, name = 'Marks Page'),
    path('show_marks/', views.show_marks, name = 'Marks'),
    path('fees/', views.fees, name = 'Fees Page'),
    path('show_fees/', views.show_fees, name = 'Fees'),
    path('attendance/', views.attendance, name = 'Attendance Page'),
    path('show_attendance/', views.show_attendance  , name = 'Attendance'),
    path('profile/', views.student_profile, name = 'Student Profile Page'),
    path('fill_marks/', views.fill_marks, name = 'Fill Marks Page'),
    path('fill_attendance/', views.fill_attendance, name = 'Fill Attendance Page'),
    path('fill_fees/', views.fill_fees, name = 'Fill Fees Page'),
    path('show_students/', views.show_students, name = 'Show Students Profiles'),
    path('student_details/', views.student_details, name = 'Student Details Page'),
    path('staff_profile/', views.staff_profile, name = 'Staff Profile Page'),
    path('edit_staff/', views.edit_staff, name = 'Edit Staff Profile'),
    path('edit_student/', views.edit_student, name = 'Edit Student Profile'),

    # college contents
    path('vision/', views.vision, name = 'Vision Mission Page'),
    path('admission/', views.admission, name = 'Admission Page'),
    path('faculties/', views.faculties, name = 'Faculty Page'),
    path('affiliation/', views.affiliation, name = 'Affiliation Page'),

    # Resume
    path('my-resume/', views.resume, name = 'Resume Page'),


]


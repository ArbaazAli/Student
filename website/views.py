from django.shortcuts import render
from .models import *
from .business import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.


def home(request): # Home page
    if request.session.has_key('username'):
        student = request.session['username']
        return render(request, 'home.html', {'student':student})
    elif request.session.has_key('username1'):
        staff = request.session['username1']
        return render(request, 'home.html', {'staff':staff})
    return render(request, 'home.html')


def login(request): #Student login page (authentication and session creation)
    if request.method == "POST":
        # get username from request of student
        username = request.POST['username']
        # get password from request of student
        password = request.POST['password']
        if True:
            # check if username and password are present in database
            if StudentLogin.objects.filter(ID_No=username , Password = password).exists():
                request.session['username'] = username
                return HttpResponseRedirect(reverse('Student Profile Page'))
            else:
                return HttpResponse("<strong>Wrong student username or password!!")
    return render(request, 'login.html')


def login2(request): #Staff login page (authentication and session creation)
    if request.method == "POST":
        # get username from request of staff
        username1 = request.POST['username1']
        # get password from request of staff
        password1 = request.POST['password1']
        # check if username is present in database
        if StaffLogin.objects.filter(ID_No=username1, Password=password1).exists():
            request.session['username1'] = username1
            print("Staff ID checked")
            print("Staff password checked")
            print("Session Key = " + username1)
            return HttpResponseRedirect(reverse('Staff Profile Page'))
        else:
            return HttpResponse("<strong>Wrong staff ID or password!!")
    return render(request, 'login2.html')


def logout(request):
    try:
        del request.session['username']
    except:
        del request.session['username1']
    finally:
        pass
    return HttpResponseRedirect(reverse('Home Page'))

def marks(request): # show marks records to staff
    if request.session.has_key('username1'):
        marks = Marks.objects.all()
        return render(request, 'staff/studentmarks.html', {'students':marks})
    return HttpResponseRedirect(reverse('Login2 Page'))

def show_marks(request): # show marks record to student
    if request.session.has_key('username'):
        logged_in_user = request.session['username']
        marks = Marks.objects.filter(Student_ID = logged_in_user)
        return render(request, 'student/marks.html', {'students': marks})
    return HttpResponseRedirect(reverse('Login Page'))

def fees(request): #show fees records to staff
    if request.session.has_key('username1'):
        fees = Fees.objects.all()
        return render(request, 'staff/studentfees.html', {'students' : fees})
    return HttpResponseRedirect(reverse('Login2 Page'))

def show_fees(request): #show fees record to student
    if request.session.has_key('username'):
        logged_in_user = request.session['username']
        fees = Fees.objects.filter(Student_ID=logged_in_user)
        return render(request, 'student/fees.html', {'students' : fees})
    return HttpResponseRedirect(reverse('Login Page'))


def attendance(request): #show attendance records to staff
    if request.session.has_key('username1'):
        attendance = Attendance.objects.all()
        return render(request, 'staff/studentattendance.html', {'students': attendance})
    return HttpResponseRedirect(reverse('Login2 Page'))

def show_attendance(request): # show attendance record to student
    if request.session.has_key('username'):
        logged_in_user = request.session['username']
        attendance = Attendance.objects.filter(Student_ID=logged_in_user)
        return render(request, 'student/attendance.html', {'students': attendance})
    return HttpResponseRedirect(reverse('Login Page'))

def show_students(request):
    if request.session.has_key('username1'):
        students_profile = StudentInfo.objects.all()
        return render(request ,'staff/studentsprofiles.html',{'students':students_profile})
    return HttpResponseRedirect(reverse('Login2 Page'))

def student_profile(request): # show Student profile page to student
    if request.session.has_key('username'):
        logged_in_user = request.session['username']
        profile =  StudentInfo.objects.filter(Student_ID = logged_in_user)
        return render(request, 'student/profile.html', {'students': profile})
    return HttpResponseRedirect(reverse('Login Page'))

def staff_profile(request): #staff profile page
    if request.session.has_key('username1'):
        logged_in_staff = request.session['username1']
        profile = StaffInfo.objects.filter(Staff_ID = logged_in_staff)
        return render(request, 'staff/staffprofile.html', {'staffs': profile})
    return HttpResponseRedirect(reverse('Login2 Page'))


def student_details(request): # Student details to add or show for staff
    if request.session.has_key('username1'):
        return render(request, 'staff/studentdetails.html')
    return HttpResponseRedirect(reverse('Login2 Page'))

def fill_marks(request): # edit student marks records
    if request.session.has_key('username1'):
         if request.method == 'POST':
             marks_store(request)
             return render(request, 'staff/studentdetails.html')
         return render(request, 'forms/marks.html')
    return HttpResponseRedirect(reverse('Login2 Page'))

def fill_attendance(request): # edit student attendance records
    if request.session.has_key('username1'):
        if request.method == 'POST':
            attendance_store(request)
            return render(request, 'staff/studentdetails.html')
        return render(request, 'forms/attendance.html')
    return HttpResponseRedirect(reverse('Login2 Page'))

def fill_fees(request): # edit student fees records
    if request.session.has_key('username1'):
        if request.method == 'POST':
            fees_store(request)
            return render(request, 'staff/studentdetails.html')
        return render(request, 'forms/fees.html')
    return HttpResponseRedirect(reverse('Login2 Page'))

def edit_staff(request): # edit staff profile (update)
    if request.method == 'POST':
        edit_staff_profile(request)
    return render(request, 'forms/editstaffprofile.html')

def edit_student(request): # edit/add student profile
    if request.session.has_key('username1'):
        if request.method == 'POST':
            edit_student_profile(request)
            return render(request, 'staff/studentdetails.html')
        return render(request, 'forms/editstudentprofile.html')
    return HttpResponseRedirect(reverse('Login2 Page'))

def vision(request): # vision page (home page content)
    if request.session.has_key('username'):
        student = request.session['username']
        return render(request, 'college/vision.html', {'student':student})
    elif request.session.has_key('username1'):
        staff = request.session['username1']
        return render(request, 'college/vision.html', {'staff':staff})
    return render(request, 'college/vision.html')

def admission(request): # admission page (home page content)
    if request.session.has_key('username'):
        student = request.session['username']
        return render(request, 'college/admission.html', {'student':student})
    elif request.session.has_key('username1'):
        staff = request.session['username1']
        return render(request, 'college/admission.html', {'staff':staff})
    return render(request, 'college/admission.html')

def faculties(request): # faculty information
    faculty = StaffInfo.objects.all()
    if request.session.has_key('username'):
        student = request.session['username']
        return render(request, 'college/faculties.html', {'student':student, 'faculties': faculty})
    elif request.session.has_key('username1'):
        staff = request.session['username1']
        return render(request, 'college/faculties.html', {'staff':staff, 'faculties': faculty})
    return render(request, 'college/faculties.html', {'faculties': faculty})

def affiliation(request): # affiliation page (home page content)
    if request.session.has_key('username'):
        student = request.session['username']
        return render(request, 'college/affiliation.html', {'student':student})
    elif request.session.has_key('username1'):
        staff = request.session['username1']
        return render(request, 'college/affiliation.html', {'staff':staff})
    return render(request, 'college/affiliation.html')

def resume(request):
    return render(request, 'resume.html')
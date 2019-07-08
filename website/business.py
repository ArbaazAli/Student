from .models import *
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

def marks_store(request):
    if request.method == 'POST':
        # Store all html data in database
        id_no = request.POST['id number']
        academic_year = request.POST['academic year']
        subject = request.POST['subject']
        semester = request.POST['semester']
        mid_term = request.POST['mid term']
        end_term = request.POST['end term']
        average = request.POST['average']

        if StudentLogin.objects.filter(ID_No = id_no).exists():
            sid = StudentLogin.objects.get(ID_No = id_no)
            marks = Marks(Student_ID = sid, Academic_Year = academic_year, Subject = subject,
                          Semester = semester, Mid_Term = mid_term, End_Term = end_term, Average = average)
            marks.save()
            print(marks)
            return HttpResponse("Marks uploaded successfully!")

        else:
            print("Wrong ID number")
            return HttpResponse("ID number is incorrect!")

def attendance_store(request):
    if request.method == 'POST':
        # Store all html data in database
        id_no = request.POST['id number']
        academic_year = request.POST['academic year']
        subject = request.POST['subject']
        faculty = request.POST['faculty']
        semester = request.POST['semester']
        total_classes = request.POST['total classes']
        present = request.POST['present']
        absent = request.POST['absent']

        if StudentLogin.objects.filter(ID_No=id_no).exists():
            sid = StudentLogin.objects.get(ID_No=id_no)
            attendance = Attendance(Student_ID=sid, Academic_Year=academic_year, Faculty=faculty, Subject=subject,
                          Semester=semester, Total_Classes=total_classes, Present=present, Absent=absent)
            attendance.save()
            print(attendance)
            return HttpResponse("Attendance uploaded successfully!")

        else:
            print("Wrong ID number")
            return HttpResponse("ID number is incorrect!")

def fees_store(request):
        # Store all html data in database
        id_no = request.POST['id number']
        academic_year = request.POST['academic year']
        amount = request.POST['amount']
        semester = request.POST['semester']
        status = request.POST['status']
        due_date = request.POST['due date']

        if StudentLogin.objects.filter(ID_No=id_no).exists():
            sid = StudentLogin.objects.get(ID_No=id_no)
            attendance = Fees(Student_ID=sid, Academic_Year=academic_year, Amount=amount,
                          Semester=semester,  Status=status, Due_Date=due_date)
            attendance.save()
            print(attendance)
            return HttpResponse("Attendance uploaded successfully!")

        else:
            print("Wrong ID number")
            return HttpResponse("ID number is incorrect!")

# Test here

def edit_staff_profile(request):
    # Store all html data in database
    id_no = request.POST['id number']
    name = request.POST['name']
    designation = request.POST['designation']
    department = request.POST['department']
    date_of_joining = request.POST['date of joining']
    email = request.POST['email']
    print (request.FILES)
    profile_picture = request.FILES['upload profile picture'] if 'upload profile picture' in request.FILES else 'profile_picture/staff.png'
    if StaffLogin.objects.filter(ID_No=id_no).exists():
        sid = StaffLogin.objects.get(ID_No=id_no)
        print(sid)
        staff = StaffInfo(Staff_ID=sid, Name=name, Designation = designation, Department = department,
                          Date_of_Joining= date_of_joining, Email = email, Profile_Picture = profile_picture)
        staff.save()
        print(staff)
        return HttpResponse("Your Info uploaded successfully!")
    else:
         print("Wrong ID number")
         return HttpResponse("ID number is incorrect!")


def edit_student_profile(request):
    # Store all html data in database
    id_no = request.POST['id number']
    first_name = request.POST['first name']
    middle_name = request.POST['middle name']
    last_name = request.POST['last name']
    blood_group = request.POST['blood group']
    contact_number = request.POST['contact number']
    date_of_birth = request.POST['date of birth']
    email = request.POST['email']
    address = request.POST['address']
    profile_picture = request.FILES['upload profile picture'] if 'upload profile picture' in request.FILES else 'profile_picture/student.png'
    if StudentLogin.objects.filter(ID_No=id_no).exists():
        sid = StudentLogin.objects.get(ID_No=id_no)
        print(sid)
        student = StudentInfo(Student_ID=sid, First_Name=first_name, Middle_Name=middle_name, Last_Name=last_name,
                              Blood_Group = blood_group, Contact_Number = contact_number, Date_of_Birth= date_of_birth,
                              Email =email, Address = address, Profile_Picture = profile_picture)
        student.save()
        print(student)
        return HttpResponse("Your Info uploaded successfully!")
    else:
        print("Wrong ID number")
        return HttpResponse("ID number is incorrect!")



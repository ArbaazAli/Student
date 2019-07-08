from django.db import models
from django import forms

# Create your models here.

class StudentLogin(models.Model):
    ID_No = models.CharField(max_length=10, primary_key=True)
    Password = models.CharField(max_length=20)
    Block = models.BooleanField()
    def __str__(self):
        return self.ID_No

    class Meta:
        db_table = 'Student Credentials'
        verbose_name_plural = "Student Credentials"

class StaffLogin(models.Model):
    ID_No = models.CharField(max_length=10, primary_key=True)
    Password = models.CharField(max_length=20)
    Block = models.BooleanField()
    def __str__(self):
        return self.ID_No

    class Meta:
        db_table = 'Staff Credentials'
        verbose_name_plural = "Staff Credentials"

class StudentInfo(models.Model):
    Student_ID = models.ForeignKey(StudentLogin, on_delete=models.CASCADE, null=True, unique=True)
    First_Name = models.CharField(max_length=20)
    Middle_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Date_of_Birth = models.CharField(max_length=10)
    Blood_Group = models.CharField(max_length=10)
    Contact_Number = models.CharField(max_length=10)
    Email = models.EmailField()
    Address = models.CharField(max_length=80)
    Profile_Picture = models.FileField(upload_to= 'profile_picture/', default= 'profile_picture/student.png',
                                       null=True, blank=True)
    def __str__(self):
        return self.First_Name

    class Meta:
        db_table = 'Student Profile'
        verbose_name_plural = "Student Profile"

class AcademicInfo(models.Model):
    Student_ID = models.ForeignKey(StudentLogin, on_delete=models.CASCADE, null=True)
    Academic_Year = models.CharField(max_length=10)
    Year_of_Passing = models.CharField(max_length=10)
    Semester_Result = models.DecimalField(max_digits=2, decimal_places=1)
    Branch = models.CharField(max_length=10)
    ID_no = models.IntegerField()
    def __str__(self):
        return self.ID_no

    class Meta:
        db_table = 'Academic Profile'
        verbose_name_plural = "Academic Profile"

class Fees(models.Model):
    Student_ID = models.ForeignKey(StudentLogin, on_delete=models.CASCADE, null=True)
    Academic_Year = models.CharField(max_length=10)
    Amount = models.CharField(max_length=6)
    Semester = models.CharField(max_length=8)
    Status = models.CharField(max_length=9)
    Due_Date = models.CharField(max_length=10, default= '-/-/-')
    def __str__(self):
        return self.Semester

    class Meta:
        db_table = 'Fees Report'
        verbose_name_plural = "Fees Report"

class Marks(models.Model):
    Student_ID = models.ForeignKey(StudentLogin, on_delete=models.CASCADE, null=True)
    Academic_Year = models.CharField(max_length=10)
    Subject = models.CharField(max_length=50)
    Semester = models.CharField(max_length=8)
    Mid_Term = models.CharField(max_length=5)
    End_Term = models.CharField(max_length=5)
    Average = models.CharField(max_length=5)
    def __str__(self):
        return self.Subject

    class Meta:
        db_table = 'Marks Report'
        verbose_name_plural = "Marks Report"

class Attendance(models.Model):
    Student_ID = models.ForeignKey(StudentLogin, on_delete=models.CASCADE, null=True)
    Academic_Year = models.CharField(max_length=10)
    Faculty = models.CharField(max_length=30)
    Subject = models.CharField(max_length=50)
    Semester = models.CharField(max_length=8)
    Total_Classes = models.CharField(max_length=5)
    Present = models.CharField(max_length=5)
    Absent = models.CharField(max_length=5)

    def __str__(self):
        return self.Subject

    class Meta:
        db_table = 'Attendance Report'
        verbose_name_plural = "Attendance Report"

class StaffInfo(models.Model):
    Staff_ID = models.ForeignKey(StaffLogin, on_delete=models.CASCADE, null=True, unique=True)
    Name = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Date_of_Joining = models.CharField(max_length=10)
    Email = models.EmailField()
    Profile_Picture = models.FileField(upload_to= 'profile_picture/', default= 'profile_picture/staff.png', null=True, blank=True)
    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'Staff Profile'
        verbose_name_plural = "Staff Profile"

class StaffEducation(models.Model):
    Staff_ID = models.ForeignKey(StaffLogin, on_delete=models.CASCADE, null=True)
    Education = models.CharField(max_length=20)
    Teaching_Subject = models.CharField(max_length=50)
    Branch = models.CharField(max_length=20)
    def __str__(self):
        return self.Teaching_Subject

    class Meta:
        db_table = 'Staff Education'
        verbose_name_plural = "Staff Education"

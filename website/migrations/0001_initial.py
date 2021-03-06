# Generated by Django 2.2.2 on 2019-06-25 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffLogin',
            fields=[
                ('ID_No', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=20)),
                ('Block', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Staff Credentials',
                'db_table': 'Staff Credentials',
            },
        ),
        migrations.CreateModel(
            name='StudentLogin',
            fields=[
                ('ID_No', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=20)),
                ('Block', models.BooleanField(default=False, null=True)),
            ],
            options={
                'verbose_name_plural': 'Student Credentials',
                'db_table': 'Student Credentials',
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=10)),
                ('Middle_Name', models.CharField(max_length=10)),
                ('Last_Name', models.CharField(max_length=10)),
                ('Date_of_Birth', models.CharField(max_length=10)),
                ('Blood_Group', models.CharField(max_length=10)),
                ('Contact_Number', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=25)),
                ('Student_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.StudentLogin')),
            ],
            options={
                'verbose_name_plural': 'Student Profile',
                'db_table': 'Student Profile',
            },
        ),
        migrations.CreateModel(
            name='StaffInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('Date_of_Birth', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Staff_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.StaffLogin')),
            ],
            options={
                'verbose_name_plural': 'Staff Profile',
                'db_table': 'Staff Profile',
            },
        ),
        migrations.CreateModel(
            name='StaffEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Education', models.CharField(max_length=20)),
                ('Teaching_Subject', models.CharField(max_length=15)),
                ('Branch', models.CharField(max_length=10)),
                ('Staff_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.StaffLogin')),
            ],
            options={
                'verbose_name_plural': 'Staff Education',
                'db_table': 'Staff Education',
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Academic_Year', models.CharField(max_length=10)),
                ('Subject', models.CharField(max_length=20)),
                ('Semester', models.CharField(max_length=5)),
                ('Mid_Term', models.CharField(max_length=5)),
                ('End_Term', models.CharField(max_length=5)),
                ('Average', models.CharField(max_length=5)),
                ('Student_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.StudentLogin')),
            ],
            options={
                'verbose_name_plural': 'Marks Report',
                'db_table': 'Marks Report',
            },
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Academic_Year', models.IntegerField()),
                ('Amount', models.CharField(max_length=6)),
                ('Semester', models.CharField(max_length=5)),
                ('Status', models.CharField(max_length=6)),
                ('Due_Date', models.CharField(max_length=10)),
                ('Student_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.StudentLogin')),
            ],
            options={
                'verbose_name_plural': 'Fees Report',
                'db_table': 'Fees Report',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Academic_Year', models.CharField(max_length=10)),
                ('Faculty', models.CharField(max_length=20, null=True)),
                ('Subject', models.CharField(max_length=20)),
                ('Semester', models.CharField(max_length=5, null=True)),
                ('Total_Classes', models.CharField(max_length=5, null=True)),
                ('Present', models.CharField(max_length=5)),
                ('Absent', models.CharField(max_length=5)),
                ('Student_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.StudentLogin')),
            ],
            options={
                'verbose_name_plural': 'Attendance Report',
                'db_table': 'Attendance Report',
            },
        ),
        migrations.CreateModel(
            name='AcademicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admission_Year', models.IntegerField()),
                ('Year_of_Passing', models.IntegerField()),
                ('Semester_Result', models.DecimalField(decimal_places=1, max_digits=2)),
                ('Branch', models.CharField(max_length=10)),
                ('ID_no', models.IntegerField()),
                ('Student_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.StudentLogin')),
            ],
            options={
                'verbose_name_plural': 'Academic Profile',
                'db_table': 'Academic Profile',
            },
        ),
    ]

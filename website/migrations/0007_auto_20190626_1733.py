# Generated by Django 2.2.2 on 2019-06-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20190626_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Subject',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='marks',
            name='Subject',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='staffeducation',
            name='Teaching_Subject',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='staffinfo',
            name='Name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='Address',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='First_Name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='Last_Name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='Middle_Name',
            field=models.CharField(max_length=20),
        ),
    ]
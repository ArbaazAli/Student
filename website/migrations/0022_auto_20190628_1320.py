# Generated by Django 2.2.2 on 2019-06-28 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_staffinfo_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffinfo',
            name='Profile_Picture',
            field=models.FileField(blank=True, null=True, upload_to='media/staff'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='Profile_Picture',
            field=models.FileField(blank=True, null=True, upload_to='media/staff'),
        ),
    ]

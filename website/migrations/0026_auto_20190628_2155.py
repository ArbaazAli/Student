# Generated by Django 2.2.2 on 2019-06-28 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_auto_20190628_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffinfo',
            name='Profile_Picture',
            field=models.FileField(blank=True, default='profile_picture/staff.png', null=True, upload_to='profile_picture/'),
        ),
    ]

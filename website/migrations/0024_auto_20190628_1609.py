# Generated by Django 2.2.2 on 2019-06-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_auto_20190628_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffinfo',
            name='Profile_Picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='Profile_Picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
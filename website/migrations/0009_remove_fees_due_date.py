# Generated by Django 2.2.2 on 2019-06-26 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20190626_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fees',
            name='Due_Date',
        ),
    ]
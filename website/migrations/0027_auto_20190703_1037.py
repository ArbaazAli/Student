# Generated by Django 2.2.2 on 2019-07-03 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20190628_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffinfo',
            name='Staff_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.StaffLogin', unique=True),
        ),
    ]

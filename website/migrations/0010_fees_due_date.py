# Generated by Django 2.2.2 on 2019-06-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_fees_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='fees',
            name='Due_Date',
            field=models.CharField(default='-/-/-', max_length=10),
        ),
    ]

# Generated by Django 4.2.4 on 2023-12-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Student'), (2, 'Institute'), (3, 'StateAuthority'), (4, 'superuser')]),
        ),
    ]

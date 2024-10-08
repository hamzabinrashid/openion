# Generated by Django 5.1 on 2024-08-12 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authservice', '0002_user_is_active_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(max_length=10, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=254, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=254, null=True, verbose_name='last name'),
        ),
    ]

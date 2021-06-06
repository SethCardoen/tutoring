# Generated by Django 3.2.3 on 2021-06-06 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education_level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diploma', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(blank=True, max_length=200, null=True, verbose_name='Priviliges')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('surname', models.CharField(max_length=200, verbose_name='Surname')),
                ('birthdate', models.DateField(verbose_name='enter your birthdate')),
                ('sign_in_date', models.DateField(auto_now_add=True)),
                ('education_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.education_level')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.level')),
            ],
        ),
    ]

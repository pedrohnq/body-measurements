# Generated by Django 4.1 on 2022-08-10 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='BodyMeasurementSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('right_biceps', models.DecimalField(decimal_places=2, max_digits=5)),
                ('left_biceps', models.DecimalField(decimal_places=2, max_digits=5)),
                ('right_forearm', models.DecimalField(decimal_places=2, max_digits=5)),
                ('left_forearm', models.DecimalField(decimal_places=2, max_digits=5)),
                ('shoulder', models.DecimalField(decimal_places=2, max_digits=5)),
                ('chest', models.DecimalField(decimal_places=2, max_digits=5)),
                ('waist', models.DecimalField(decimal_places=2, max_digits=5)),
                ('abdomen', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hip', models.DecimalField(decimal_places=2, max_digits=5)),
                ('right_thigh', models.DecimalField(decimal_places=2, max_digits=5)),
                ('left_thigh', models.DecimalField(decimal_places=2, max_digits=5)),
                ('right_calf', models.DecimalField(decimal_places=2, max_digits=5)),
                ('left_calf', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]

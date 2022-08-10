from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class BodyMeasurementSheet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    right_biceps = models.DecimalField(max_digits=5, decimal_places=2)
    left_biceps = models.DecimalField(max_digits=5, decimal_places=2)
    right_forearm = models.DecimalField(max_digits=5, decimal_places=2)
    left_forearm = models.DecimalField(max_digits=5, decimal_places=2)
    shoulder = models.DecimalField(max_digits=5, decimal_places=2)
    chest = models.DecimalField(max_digits=5, decimal_places=2)
    waist = models.DecimalField(max_digits=5, decimal_places=2)
    abdomen = models.DecimalField(max_digits=5, decimal_places=2)
    hip = models.DecimalField(max_digits=5, decimal_places=2)
    right_thigh = models.DecimalField(max_digits=5, decimal_places=2)
    left_thigh = models.DecimalField(max_digits=5, decimal_places=2)
    right_calf = models.DecimalField(max_digits=5, decimal_places=2)
    left_calf = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.student.name + ' - ' + self.date.strftime('%d/%m/%Y')

    
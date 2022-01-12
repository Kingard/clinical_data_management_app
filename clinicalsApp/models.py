from django.db import models

# Create your models here.
class Patient(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10,choices=[('MALE','Male'),('FEMALE','female')])
    email = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class ClinicData(models.Model):
    symptom1 = models.CharField(max_length=30)
    symptom2 = models.CharField(max_length=30)
    symptom3 = models.CharField(max_length=30)
    symptom4 = models.CharField(max_length=30)
    symptom5 = models.CharField(max_length=30)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    additional_info = models.TextField()
    entryTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient

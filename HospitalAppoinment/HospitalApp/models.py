from django.db import models


class signup_db(models.Model):
    name = models.CharField(max_length=200)
    phno = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    status_choice = [('male', 'Male'), ('female', 'Female'), ('notspecified', 'Notspecified')]
    gender = models.CharField(max_length=25, choices=status_choice, default='Notspecified')

    def __str__(self):
        return self.name


class appoinments(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    status_choices = [('male', 'male'), ('female', 'female'), ('not specified', 'not specified')]
    gender = models.CharField(max_length=25, choices=status_choices, default='not specified')
    phone_number = models.CharField(max_length=400)
    payment = models.CharField(max_length=200, default=0)
    booking_choice = [('approve', 'approve'), ('reject', 'reject'), ('pending', 'pending')]
    booking_status = models.CharField(max_length=100, choices=booking_choice, default='pending')

    def __str__(self):
        return self.name


class admin_log(models.Model):
    admin_name = models.CharField(max_length=25)
    admin_pass = models.CharField(max_length=25)

    def __str__(self):
        return self.admin_name

class doctors(models.Model):
    name = models.CharField(max_length=200)
    doctor_id = models.CharField(max_length=400)
    uploadphoto = models.FileField()
    department = models.CharField(max_length=200)
    def __str__(self):
        return self.name





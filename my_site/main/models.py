from django.db import models

SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    sex = models.CharField(choices=SEX_CHOICES, max_length=20, default='M')
    education = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    experience = models.TextField()


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthday = models.DateField(auto_now=False, auto_now_add=False)


class Grade(models.Model):
    description = models.TextField()
    grade = models.IntegerField()


class Review(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    grade = models.OneToOneField(Grade, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Student(models.Model):
    names = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    adm_no = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.names

    class Meta:
        ordering = ['-created_at']
        db_table = 'student'


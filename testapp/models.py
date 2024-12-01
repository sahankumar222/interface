from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/')
    video = models.FileField(upload_to='videos/')

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    
class Library(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.name
    
   
   
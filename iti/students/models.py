from django.db import models

class Track(models.Model):
    name= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True)
    image = models.ImageField(upload_to="students/images/" , null=True, blank=True)
    grade = models.IntegerField(default=100)
    track = models.ForeignKey(Track, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
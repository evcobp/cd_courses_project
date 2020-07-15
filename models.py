from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    actions = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

class Description(models.Model):
    description = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

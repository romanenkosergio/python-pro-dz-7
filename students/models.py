from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.first_name

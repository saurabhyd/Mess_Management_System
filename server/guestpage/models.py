from django.db import models

# Create your models here.
class guestreg(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    block = models.PositiveIntegerField()
    meal = models.CharField(max_length=15)
    date = models.DateField()

    def __str__(self):
        return self.fname + self.lname

from django.db import models

# Create your models here.
class student_details(models.Model):
    usn = models.CharField(primary_key=True, max_length=15)
    pwd = models.CharField(max_length=15)
    messrno = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    bno = models.PositiveIntegerField()
    branch = models.CharField(max_length=50)
    sem = models.PositiveIntegerField()

    def __str__(self):
        return self.usn + "-" + self.name

class messreg(models.Model):
    usn = models.ForeignKey(student_details)
    messbno = models.PositiveIntegerField()
    validity = models.DateField()

    def __str__(self):
        return str(self.usn) + "-" + str(self.messbno)
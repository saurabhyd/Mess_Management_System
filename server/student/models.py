from django.db import models

# Create your models here.
class student_details(models.Model):
    usn = models.CharField(primary_key=True, max_length=15)
    pwd = models.CharField(max_length=15)
    messrno = models.PositiveIntegerField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50,null=True)
    bno = models.PositiveIntegerField()
    branch = models.CharField(max_length=50)
    sem = models.PositiveIntegerField()

    def __str__(self):
        return self.usn + "-" + self.fname

class messreg(models.Model):
    usn = models.CharField(max_length=15)
    messbno = models.PositiveIntegerField()
    validity = models.DateField()

    def __str__(self):
        return str(self.usn) + "-" + str(self.messbno)

class feed(models.Model):
    block=models.PositiveIntegerField()
    fdb=models.CharField(max_length=500)

    def __str__(self):
        return str(self.block)
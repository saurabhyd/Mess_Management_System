from django.db import models

# Create your models here.

class messadmin(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    pwd = models.CharField(max_length=15)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50,null=True)
    messbno = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.fname + "-" + str(self.messbno)

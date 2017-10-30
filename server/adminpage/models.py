from django.db import models

# Create your models here.

class messadmin(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    pwd = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    messbno = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name + "-" + str(self.messbno)

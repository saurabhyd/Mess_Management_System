from django.db import models


# Create your models here.
class mess(models.Model):
    messbno = models.PositiveIntegerField(primary_key=True)
    type = models.CharField(max_length=15)
    region = models.CharField(max_length=15)
    vacancy = models.PositiveIntegerField()

    def __str__(self):
        return str(self.messbno) + "-" + self.type


class menu(models.Model):
    s1 = models.PositiveIntegerField()
    s2 = models.PositiveIntegerField()
    messbno = models.ForeignKey(mess)
    weekday = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    food = models.CharField(max_length=500)

    def __str__(self):
        return str(self.messbno) + self.weekday + "-" + self.type + "-" + self.food

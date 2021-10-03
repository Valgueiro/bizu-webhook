from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    cidade = models.CharField(max_length=128)
    endereco = models.CharField(max_length=128)
    

    def __str__(self) -> str:
        return "{} <{}>".format(self.name, self.email)

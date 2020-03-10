from django.db import models
# Create your models here.

class Usuarios(models.Model):
    user_name: models.CharField(max_length=50)
    email: models.EmailField()
    password: models.CharField(max_length=50)

    def _str_(self):
        return self.user_name


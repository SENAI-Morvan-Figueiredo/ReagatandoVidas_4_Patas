from django.db import models
from django.contrib.auth.models import AbstractUser


class Adminstrador(models.Model):
    email = models.EmailField(max_length=50, unique=True, verbose_name="Email")
    senha = models.CharField(max_length=128, verbose_name="Senha") 
    
    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        db_table = "adminstrador"
    
    def __str__(self):
        return self.email
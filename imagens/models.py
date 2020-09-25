from django.db import models

# Create your models here.

class Image(models.Model):
    descricao = models.CharField(max_length=255)
    foto = models.ImageField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descricao

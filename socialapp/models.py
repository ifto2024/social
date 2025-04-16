from django.db import models


# Create your models here.
class Postagem(models.Model):
    id_postagem = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    curtidas = models.IntegerField(default=0)
    descurtidas = models.IntegerField(default=0)

    def __str__(self):
        return self.conteudo[:30]


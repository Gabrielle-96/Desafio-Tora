from django.db import models

# Create your models here.


class TipoAcesso(models.Model):
    nome = models.CharField(max_length=30)

    class Meta:
        db_table = "tipo_acesso"


class Equipes(models.Model):
    nome = models.CharField(max_length=35)

    class Meta:
        db_table = "equipes"


class Usuarios(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.IntegerField()
    tipo_acesso = models.ForeignKey(TipoAcesso, on_delete=models.PROTECT)
    equipes = models.ForeignKey(Equipes, on_delete=models.PROTECT)

    class Meta:
        db_table = "usuarios"

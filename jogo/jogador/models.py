from django.db import models

# Create your models here.
class Jogador(models.Model):
    idjogador = models.IntegerField(db_column='idJogador', primary_key=True)
    nome = models.CharField(max_length=25)
    login = models.CharField(max_length=25)
    senha = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'jogador'
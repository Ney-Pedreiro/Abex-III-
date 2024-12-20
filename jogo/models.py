# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Banco(models.Model):
    idbanco = models.IntegerField(db_column='idBanco', primary_key=True)  # Field name made lowercase.
    valor_emprestimo = models.FloatField(blank=True, null=True)
    valor_investimento = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    personagem_idpersonagem = models.ForeignKey('Personagem', models.DO_NOTHING, db_column='Personagem_idPersonagem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'banco'


class Compra(models.Model):
    idcompra = models.IntegerField(db_column='idCompra', primary_key=True)  # Field name made lowercase.
    personagem_idpersonagem = models.ForeignKey('Personagem', models.DO_NOTHING, db_column='Personagem_idPersonagem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compra'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EstadoPersonagem(models.Model):
    idestadopersonagem = models.IntegerField(db_column='idEstadoPersonagem', primary_key=True)  # Field name made lowercase.
    status_fome = models.IntegerField(blank=True, null=True)
    status_sede = models.IntegerField(blank=True, null=True)
    status_felicidade = models.IntegerField(blank=True, null=True)
    personagem_idpersonagem = models.ForeignKey('Personagem', models.DO_NOTHING, db_column='Personagem_idPersonagem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado_personagem'


class Jogador(models.Model):
    idjogador = models.IntegerField(db_column='idJogador', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=25)
    login = models.CharField(max_length=25)
    senha = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'jogador'


class Loja(models.Model):
    idloja = models.IntegerField(db_column='idLoja', primary_key=True)  # Field name made lowercase.
    nome_produto = models.CharField(max_length=25)
    preco = models.FloatField()
    quantidade = models.IntegerField(blank=True, null=True)
    compra_idcompra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='Compra_idCompra')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loja'


class Minijogo(models.Model):
    idminijogo = models.IntegerField(db_column='idMiniJogo', primary_key=True)  # Field name made lowercase.
    minijogo = models.CharField(max_length=25)
    personagem_idpersonagem = models.ForeignKey('Personagem', models.DO_NOTHING, db_column='Personagem_idPersonagem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'minijogo'


class Personagem(models.Model):
    idpersonagem = models.IntegerField(db_column='idPersonagem', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=25)
    genero = models.CharField(max_length=1, blank=True, null=True)
    necessidades = models.IntegerField()
    jogador_idjogador = models.ForeignKey(Jogador, models.DO_NOTHING, db_column='Jogador_idJogador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personagem'


class Profissao(models.Model):
    idprofissao = models.IntegerField(db_column='idProfissao', primary_key=True)  # Field name made lowercase.
    profissao = models.CharField(max_length=25, blank=True, null=True)
    salario = models.FloatField(blank=True, null=True)
    minijogo_idminijogo = models.ForeignKey(Minijogo, models.DO_NOTHING, db_column='MiniJogo_idMiniJogo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profissao'

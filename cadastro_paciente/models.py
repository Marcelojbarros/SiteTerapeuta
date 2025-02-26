from django.db import models
from login_terapeuta.models import LoginTerapeuta
class CadastroPaciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    ESTADO_CIVIL_CHOICES = [
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)'),
        ('uniao_estavel', 'União Estável'),
        ('outro', 'Outro'),
    ]

    idPaciente = models.AutoField(primary_key=True, null=False, blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    email = models.EmailField(max_length=254, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    rg = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    endereco = models.TextField(max_length=100, null=True, blank=True)
    nacionalidade = models.CharField(max_length=100, null=True, blank=True)
    estado_civil = models.CharField(max_length=50, choices=ESTADO_CIVIL_CHOICES)
    profissao = models.CharField(max_length=100, null=True, blank=True)
    convenio = models.CharField(max_length=150, null=True, blank=True)
    #idTerapeuta = models.ForeignKey(LoginTerapeuta, on_delete=models.CASCADE)

    def calcular_idade(self):
        from datetime import date
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) <       (self.data_nascimento.month, self.data_nascimento.day))
        return idade

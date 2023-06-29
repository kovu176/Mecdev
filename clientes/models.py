from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User (AbstractUser):
    email = models.CharField(max_length=55,)

class Clientes (models.Model):
    MARCA_CHOICES = (  #CRIAR LISTA PREDEFINIDA DE VALORES 
        ('Honda', 'Honda'), 
        ('Volkswagen', 'Volkswagen'),
        ('Fiat', 'Fiat'), 
    )
    nome = models.CharField(max_length= 50 )
    sobrenome = models.CharField(max_length= 50 )
    cpf = models.PositiveIntegerField(default= 0)
    carro = models.ManyToManyField ('Carro', related_name= 'carro_cliente', blank=True)
    
    def __str__(self):
        return f'{self.nome}' # f força ser uma string passa o proprio objeto como parametro e retorna o atributo nome.


    


class Carro (models.Model):
    MARCA_CHOICES = (  #CRIAR LISTA PREDEFINIDA DE VALORES 
        ('Honda', 'Honda'), 
        ('Volkswagen', 'Volkswagen'),
        ('Fiat', 'Fiat'),
        ('Ford', 'Ford'), 
        ('Hyundai', 'Hyundai'), 
        ('Jeep', 'Jeep'), 
        ('Renault', 'Renault'),  
    )
    COR_CHOICES = (
        ('Branco', 'Branco'),
        ('Preto', 'Preto'),
        ('Vermelho', 'Vermelho'),
        ('Prata', 'Prata'),
        ('Rosa', 'Rosa'),
        ('Azul', 'Azul'),
        ('Outra', 'Outra')
    )
    marca = models.CharField(choices=MARCA_CHOICES, max_length=55)
    modelo = models.CharField(max_length=55)
    placa = models.CharField(max_length=12)
    ano = models.PositiveIntegerField(default=0)
    cor = models.CharField(choices=COR_CHOICES, max_length=55)
    func = models.ForeignKey('User', related_name='func_carro', null=True, blank=True, default=None ,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.modelo}  {self.placa}'
    

class Servicos(models.Model):
    SERVICO_CHOICES = (
        ('Limpeza', 'Limpeza'),
        ('Manutenção', 'Manutenção'),
        ('Funilaria', 'Funilaria'),
        ('Diagnóstico', 'Diagnóstico'),
        ('Alinhamento', 'Alinhamento'),
        ('Troca de Pneu', 'Troca de Pneu'),
        ('Outro', 'Outro')
)
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluido', 'Concluido')
    )
    tipo = models.CharField(choices=SERVICO_CHOICES, max_length=55)
    status = models.CharField(choices=STATUS_CHOICES, max_length=55, default='Pendente')
    descricao = models.CharField(max_length=80)
    cliente = models.ForeignKey('Clientes', related_name='service_cliente', null=True, blank=True, default=None, on_delete=models.CASCADE)
    servCar = models.ForeignKey('Carro', related_name='serv_car', null=True, blank=True, default=None, on_delete=models.CASCADE)
    
    def _str_(self):
        return f'{self.cliente} {self.servCar}'
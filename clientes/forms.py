from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Carro, Clientes, User, Servicos


class ClientesModelForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = (
            'nome',
            'sobrenome',
            'cpf',
            'carro'
            
        )
  



class CarroModelForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = (
            'marca',
            'modelo',
            'placa',
            'ano',
            'cor'
        )
        

class ServicosModelForm(forms.ModelForm):
    class Meta:
        model = Servicos
        fields = (
            'tipo',
            'descricao',
            'cliente',
            'servCar'
        )
        



        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)
        field_classes = {'username': UsernameField}
        
        
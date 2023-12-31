from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin # Essa view precisa estar logado 
from django.contrib.auth import authenticate, login
from django.views import generic
from .models import Clientes, Carro, Servicos
from .forms import CarroModelForm, CustomUserCreationForm, ClientesModelForm, ServicosModelForm





def user_Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render('base.html')
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...



    # USER VIEWS

class LandingView(generic.TemplateView):
    template_name = 'landing.html'
    
class LandingQueryView(generic.ListView):
    template_name = 'landing.html'

    def get_queryset(self):
        qs = {
            'services_geral': Servicos.objects.all().distinct(), #evitar print repetido
            'clientes_geral': Clientes.objects.all().distinct(),
            'carros_geral': Carro.objects.all().distinct(), 
        } 
        return qs
    def get_context_data(self, **kwargs):
        data = super(LandingQueryView, self).get_context_data(**kwargs)
        valorPendente = 0
        valorAndamento = 0
        valorConcluido = 0
        for aux in Servicos.objects.all():
            if aux.status == 'Pendente':
                valorPendente = valorPendente+1
            if aux.status == 'Em Andamento':
                valorAndamento = valorAndamento+1
            if aux.status == 'Concluido':
                valorConcluido = valorConcluido+1
        data['valorPendente'] = valorPendente
        data['valorAndamento'] = valorAndamento
        data['valorConcluido'] = valorConcluido                

        
        
        
        return data

class SignupView(generic.CreateView):
    template_name = 'signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse ('landing')
    
    
    # END USER VIEWS
    
    # CLIENTE LIST
    
class ClienteListView (generic.ListView):
    template_name = 'clientes.html'
   
    
    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            qs = Clientes.objects.filter(Q(nome__icontains=search) | Q(sobrenome__icontains=search) | Q(cpf__icontains=search))
        else:
            qs = Clientes.objects.all()
        return qs
    
    
    
    #CLIENTE CREATE
    
class ClienteCreateView (generic.CreateView):
    template_name = 'clientes_create.html'
    form_class = ClientesModelForm
    
    def form_valid(self, form):
        form.instance.func = self.request.user
        return super(ClienteCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('clientes-list')


    #CLIENTE UPDATE
    
class ClienteUpdateView(generic.UpdateView):
    template_name = 'clientes_update.html'
    form_class = ClientesModelForm
    def get_queryset(self):
        return Clientes.objects.filter()
    
    def get_success_url(self):
        return reverse('clientes-list')
    

    #CLIENTE DELETE

class ClienteDeleteView (generic.DeleteView):
    template_name = 'clientes_delete.html'
    
    def get_queryset(self):
        return Clientes.objects.filter()
    
    def get_success_url(self):
        return reverse('clientes-list')
    
    
    #CLIENTE DETAIL
    
class ClienteDetailView (generic.DetailView):
    template_name = 'clientes_detail.html'
    
    def get_queryset(self):
        return Clientes.objects.filter()
    

    
    
    
    
    
    
    


    
    # CRUD CARRO VIEWS
   
    
class CarroListView (generic.ListView):
    template_name = 'carro_list.html'
    
    
    
    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            qs = Carro.objects.filter(Q(marca__icontains=search) | Q(modelo__icontains=search) | Q(ano__icontains=search))
        else:
            qs = Carro.objects.all()
        return qs
       
      #CARRO CREATE 
       
class CarroCreateView (generic.CreateView):
    template_name = 'carro_create.html'
    form_class = CarroModelForm
    
    def form_valid(self, form):
        form.instance.func = self.request.user
        return super(CarroCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('carro-list')

    #CARRO UPDATE

class CarroUpdateView(generic.UpdateView):
    template_name = 'carro_update.html'
    form_class = CarroModelForm
    def get_queryset(self):
        return Carro.objects.filter()
    
    def get_success_url(self):
        return reverse('carro-list')
    
    #CARRO DELETE
    
class CarroDeleteView (generic.DeleteView):
    template_name = 'carro_delete.html'
    
    def get_queryset(self):
        return Carro.objects.filter()
    
    def get_success_url(self):
        return reverse('carro-list')

    #CARRO DETAIL

class CarroDetailView (generic.DetailView):
    template_name = 'carro_detail.html'
    
    def get_queryset(self):
        return Carro.objects.filter()
    

  # CRUD CARRO END
  


    #SERVICO LIST

class ServicosListView (generic.ListView):
    template_name = 'servicos_list.html'
    
    
   
    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            qs = Servicos.objects.filter(Q(cliente__icontains=search) | Q(servCar__icontains=search))
        else:
            qs = Servicos.objects.all()
        return qs
    

    #SERVICO CREATE
    
class ServicosCreateView (generic.CreateView):
    template_name = 'servicos_create.html'
    form_class = ServicosModelForm
    
    def form_valid(self, form):
        form.instance.func = self.request.user
        return super(ServicosCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('servicos-list')


    #SERVICO UPDATE 
    
class ServicosUpdateView(generic.UpdateView):
    template_name = 'servicos_update.html'
    form_class = ServicosModelForm
    def get_queryset(self):
        return Servicos.objects.filter()
    
    def get_success_url(self):
        return reverse('servicos-list')
    
    
    #SERVICO DELETE
    
    
class ServicosDeleteView (generic.DeleteView):
    template_name = 'servicos_delete.html'
    
    def get_queryset(self):
        return Servicos.objects.filter()
    
    def get_success_url(self):
        return reverse('servicos-list')
    
    
    #SERVICO DETAIL
    
class ServicosDetailView (generic.DetailView):
    template_name = 'servicos_detail.html'
    
  
    
    def get_queryset(self):
        return Servicos.objects.filter()
    

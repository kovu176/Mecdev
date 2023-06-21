from django.urls import path
from .views import  (ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
                     ClienteDetailView, CarroListView, CarroCreateView, CarroUpdateView,
                     CarroDeleteView, CarroDetailView,ServicosListView,ServicosCreateView,
                     ServicosUpdateView, ServicosDeleteView, ServicosDetailView)



urlpatterns = [
        
        path('cliente/', ClienteListView.as_view(), name= "clientes-list"), 
        path('clientes/create', ClienteCreateView.as_view(), name='cliente-create'),
        path('clientes/<int:pk>/update', ClienteUpdateView.as_view(), name='cliente-update'),
        path('clientes/<int:pk>/delete', ClienteDeleteView.as_view(), name='cliente-delete'),
        path('clientes/<int:pk>/detail', ClienteDetailView.as_view(), name='cliente-detail'),
        path('carro/', CarroListView.as_view(), name='carro-list'),
        path('carro/create', CarroCreateView.as_view(), name='carro-create'),
        path('carro/<int:pk>/update', CarroUpdateView.as_view(), name='carro-update'),
        path('carro/<int:pk>/delete', CarroDeleteView.as_view(), name='carro-delete'),
        path('carro/<int:pk>/detail', CarroDetailView.as_view(), name='carro-detail'),
        path('servicos/', ServicosListView.as_view(), name='servicos-list'),
        path('servicos/create', ServicosCreateView.as_view(), name='servicos-create'),
        path('servicos/<int:pk>/update', ServicosUpdateView.as_view(), name='servicos-update'),
        path('servicos/<int:pk>/delete', ServicosDeleteView.as_view(), name='servicos-delete'),
        path('servicos/<int:pk>/detail', ServicosDetailView.as_view(), name='servicos-detail')
        
]   
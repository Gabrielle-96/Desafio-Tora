from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from usuarios.models import Usuarios


class UsuarioList(ListView):
    model = Usuarios


class UsuarioView(DetailView):
    model = Usuarios


class UsuarioCreate(CreateView):
    model = Usuarios
    fields = ['nome', 'cpf', 'equipes_id', 'tipo_acesso_id']
    success_url = reverse_lazy('usuario_list')


class UsuarioUpdate(UpdateView):
    model = Usuarios
    fields = ['nome']
    success_url = reverse_lazy('usuario_list')


class UsuarioDelete(DeleteView):
    model = Usuarios
    success_url = reverse_lazy('usuario_list')

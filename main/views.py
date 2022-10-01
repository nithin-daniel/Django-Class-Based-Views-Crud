from django.shortcuts import render
from . models import Core
from django.views.generic import ListView, DetailView, UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.


class IndexView(ListView):
    model = Core 
    template_name = 'main/index.html'
    context_object_name = 'index'

class SingleView(DetailView):
    model = Core
    template_name = 'main/single.html'
    context_object_name = 'post'    

class PostsView(ListView):
    model = Core 
    template_name = 'main/posts.html'
    context_object_name = 'post_list'

class AddView(CreateView):
    model = Core
    filelds =  ['name']
    template_name = 'main/add.html'
    fields = '__all__'
    success_url = reverse_lazy('main:posts')


class EditView(UpdateView):
    model = Core
    template_name = 'main/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('main:posts')

class DeleteView(DeleteView):
    model = Core
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('main:posts')
    template_name = 'main/confirm-delete.html'
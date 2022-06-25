from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import UpdateView

#I don't understand the link between decsription and the video.. Couldn't grasp.
# Create your views here.
class PostListView(ListView):
    model = Post
    templates_name = 'post_list.html'

class PostCreateView(CreateView):
    model = Post
    fields = [
              "title"
              "description"
            ]
    templates_name = 'post_form.html'
    
class PostDetailView(DetailView):
        model = Post
        templates_name = 'post_detail.html'
        
class PostUpdateView(UpdateView):
    model = Post
    fields = []
    
class PostDeleteView(UpdateView):
    model = Post
    fields = []
    templates_name = 'post_confirm_delete.html'
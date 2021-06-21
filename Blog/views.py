from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag

class Home(ListView):
    model = Post
    template_name = 'Blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context

class PostsByCategory(ListView):
    template_name = 'Blog/index.html'
    context_object_name = 'posts'
    paginate_by = 1
    allow_empty = False # 404

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


def index(request):
    return render(request, 'Blog/index.html')

def get_category(request, slug):
    return render(request, 'Blog/category.html')

def get_post(request, slug):
    return render(request, 'Blog/category.html')

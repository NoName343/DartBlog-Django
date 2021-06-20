from django.shortcuts import render


def index(request):
    return render(request, 'Blog/index.html')

def get_category(request, slug):
    categories = Category.objects.all()
    return render(request, 'Blog/category.html')

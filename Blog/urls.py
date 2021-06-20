from django.urls import path
from Blog.views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>', get_category, name='categore'),
]

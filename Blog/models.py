from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title


    class Meta():
        ordering = ['title']

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title


    class Meta():
        ordering = ['title']

class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, verbose_name='Изображение')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Посты')

    def __str__(self):
        return self.title


    class Meta():
        ordering = ['-created_at']

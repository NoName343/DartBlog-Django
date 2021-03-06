# Generated by Django 3.2.4 on 2021-06-10 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотры')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='Blog.category')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='Blog.Tag', verbose_name='Посты')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]

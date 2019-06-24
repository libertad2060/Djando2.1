from django.db import models
from django.utils import timezone

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    login=models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    def __str__(self): # __unicode__ en Python 2
        return self.nombre


class Post(models.Model):
    author = models.ForeignKey('Autor', on_delete=models.CASCADE)
    #autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=100)
    comentario=models.CharField(max_length=1000)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

    def publish(self):
        self.published_date = timezone.now()
        self.save()


"""class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
  autores = models.ManyToManyField(Autor)
    editor = models.ManyToManyField(Editor)
    def __str__(self):
        return self.title"""

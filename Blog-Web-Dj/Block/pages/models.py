from django.db import models 
from ckeditor.fields import RichTextField
# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo")
    content=RichTextField(verbose_name="Contenido")
    
    slug=models.CharField(unique=True,max_length=200,verbose_name="URL Amigable")
    order=models.IntegerField(default=0,verbose_name="Orden")
    public=models.BooleanField(verbose_name="¿Publicado?")
    created_at=models.DateField(auto_now_add=True,verbose_name="Creado el :")
    update_at=models.DateField(auto_now=True,verbose_name="Actualizado el :")

    class Meta:
        verbose_name="Pagina"
        verbose_name_plural="Paginas"
    #Imprimir cada uno de los titulos de las paginas en el panel de administracion 
    def __str__(self):
        return self.title 
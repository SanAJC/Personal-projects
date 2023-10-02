from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    """
    Esta clase representa el modelo de Categoría en la base de datos.
    """
    name=models.CharField(max_length=100,verbose_name='Nombre')
    description=models.CharField(max_length=255,verbose_name='Descripcion')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Creado el:')

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

    def __str__(self) :
        """
        Este método define la representación en cadena del objeto Category.
        Devuelve el nombre de la categoría.
        """
        return self.name
    
class Article(models.Model):
    """
    Esta clase representa el modelo de Artículo en la base de datos.
    """
    user= models.ForeignKey(User,verbose_name='Usuario',on_delete=models.CASCADE)
    '''
    El campo 'user' es una clave externa (ForeignKey) en el modelo actual.
    Representa una relación con el modelo 'User' proporcionado por Django, el cual
    representa a los usuarios registrados en el sistema.
    El parámetro 'verbose_name' se utiliza para dar un nombre descriptivo al campo
    en la interfaz de administración de Django, en este caso, se le asigna el nombre "Usuario".
    El parámetro 'on_delete' especifica qué hacer con los objetos relacionados cuando se elimine
    el objeto principal al que se refiere esta clave externa.
    En este caso, se utiliza 'models.CASCADE', lo que significa que cuando se elimina un objeto 'User'
    relacionado, también se eliminarán todos los objetos que tengan esta clave externa.
    '''
    categories=models.ManyToManyField(Category,verbose_name='Categorias',blank=True)
    '''
    El campo 'categories' es un campo de relación ManyToMany en el modelo actual.
    Representa una relación de muchos a muchos con el modelo 'Category'.
    El parámetro 'verbose_name' se utiliza para dar un nombre descriptivo al campo en la interfaz
    de administración de Django, en este caso, se le asigna el nombre "Categorias".
    El parámetro 'null=True' permite que este campo pueda ser nulo en la base de datos.
    El parámetro 'blank=True' indica que este campo puede estar en blanco, es decir, no es requerido.
    Estos dos parámetros 'null=True' y 'blank=True' juntos permiten que el campo sea opcional.
    '''

    title=models.CharField(max_length=150,verbose_name='Titulo')
    content= RichTextField(verbose_name='Contenido')
    image=models.ImageField(default='null',verbose_name="Imagen",upload_to="articles")
    public=models.BooleanField(verbose_name='¿Publicado?')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    update_at=models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name='Articulo'
        verbose_name_plural='Articulos'
        

    def __str__(self) :
        """
        Este método define la representación en cadena del objeto Category.
        Devuelve el nombre de la categoría.
        """
        return self.title
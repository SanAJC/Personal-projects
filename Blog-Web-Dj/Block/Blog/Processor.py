from Blog.models import Category,Article


def get_categories(request):
    ids=Article.objects.filter(public=True).values_list('categories',flat=True)
    categories=Category.objects.filter(id__in=ids).values_list('id','name')

    return{
        'categories':categories,
        'ids':ids
    }
#Diccionario con todas las paginas guardadas
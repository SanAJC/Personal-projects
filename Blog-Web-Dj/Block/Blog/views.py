from django.shortcuts import render , get_object_or_404
from Blog.models import Category,Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login")

def articles(request):
    #sacar articulos
    articles=Article.objects.all()
    #Paginar los articulos
    paginator=Paginator(articles,2)

    #Recoger numero pagina
    page=request.GET.get('page')
    page_articles=paginator.get_page(page)

    return render(request,'articles/articles.html',{
        'title':'Articulos',
        'articles':page_articles
    }) 

def category(request,category_id):
    category=Category.objects.get(id=category_id)
    articles=Article.objects.filter(categories=category)
    return render(request,'categories/category.html',{
        'category':category,
        'articles':articles
    })  

def article(request,article_id):

    article= get_object_or_404(Article,id=article_id)

    return render(request,'articles/detail.html',{
        'article':article 
    })
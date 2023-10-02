from typing import Any
from django.contrib import admin
from .models import Category,Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created_at',)
    list_display=('name','created_at')
    search_fields=('name','description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('user','created_at','update_at')
    search_fields=('title','content')
    list_filter=('public',)
    list_display=('title','public','created_at')
    def save_model(self, request,obj,form,change) :
      
        obj.user_id=request.user.id
        obj.user=request.user
        
        obj.save()


    
# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)


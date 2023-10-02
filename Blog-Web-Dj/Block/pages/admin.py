from django.contrib import admin
from .models import Page

#Configuracion extra 
class PageAdmin(admin.ModelAdmin):
    search_fields=('title','content')
    list_filter=('public',)
    list_display=('title','public','created_at')

# Register your models here.
admin.site.register(Page,PageAdmin)
#Configuracion del panel
title="Blog | Admin"
subtitle="Panel de gestion"

admin.site.site_header=title
admin.site.site_title=title
admin.site.index_title=subtitle
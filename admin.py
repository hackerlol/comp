from django.contrib import admin

# Register your models here.
from .models import Article, Image, Contributor

admin.site.register(Article)
admin.site.register(Image)
admin.site.register(Contributor)


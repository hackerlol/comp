from django.shortcuts import render
from .models import Article, Image
# Create your views here.


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    images_list = Image.objects.order_by('-path')[:5]
    context = {'latest_articles_list': latest_articles_list, 'images_list': images_list}
   
    
    return render(request, 'news/index.html', context)
  

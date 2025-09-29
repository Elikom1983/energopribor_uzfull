from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, "news/new.html", {"news_list": news})

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    newsall = News.objects.all().order_by('-created_at')[:2]
    data={
        'news':news,
        'newsall':newsall
    }
    return render(request, "news/single_post.html", data)
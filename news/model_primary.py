from .models import News, Category

def last_news(request):
    last_news = News.objects.all().order_by('-publish_time')[:10]
    navbar = Category.objects.all()

    context = {
        "last_news": last_news,
        'navbar': navbar
    }
    return context
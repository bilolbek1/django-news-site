from .models import News, Category
from datetime import datetime

def last_news(request):
    last_news = News.objects.all().order_by('-publish_time')[:10]
    navbar = Category.objects.all()
    now = datetime.now()

    context = {
        "last_news": last_news,
        'navbar': navbar,
        'now': now,
    }
    return context
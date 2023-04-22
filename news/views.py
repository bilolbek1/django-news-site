from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .form import ContactForm
from django.http import HttpResponse
from .models import News, Category

# Create your views here.

# def NewsView(request):
#     newsall = News.objects.all()
#
#     context = {
#         'newsall': newsall
#     }
#     return render(request, 'news.html', context=context)
#
# def NewsDetailView(request):
#     newsdetail = News.objects.all()
#
#     context = {
#         'newsdetail': newsdetail
#     }
#     return render(request, 'news_detail.html', context=context)


class NewsAllView(ListView):
    model = News
    template_name = 'news/news.html'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'




# HOMEPAGEVIEW WITH FUNCTION

# def HomePageView(request):
#     home_page = News.objects.all().order_by("-publish_time")[:10]
#     category = Category.objects.all()
#     local_card = News.objects.all().filter(category__name='BIZNESS').order_by('-publish_time')[1:6]
#     local_primary = News.objects.all().filter(category__name='BIZNESS').order_by('-publish_time')[:1]
#     context = {
#         "home_page": home_page,
#         "category": category,
#         "local_card": local_card,
#         "local_primary": local_primary
#
#     }
#     return render(request, 'news/home.html', context=context)




# HOMEPAGEVIEW WITH CLASS

class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_page'] = News.objects.all().order_by("-publish_time")
        context['last_massage'] = News.objects.all().order_by('-publish_time')[:5]
        context['category'] = Category.objects.all()
        context['local_card'] = News.objects.all().filter(category__name='MAHALLIY').order_by('-publish_time')[1:6]
        context['local_primary'] = News.objects.all().filter(category__name='MAHALLIY').order_by('-publish_time')[:1]
        context['xorij'] = News.objects.all().filter(category__name='XORIJ').order_by('-publish_time')
        context['sport'] = News.objects.all().filter(category__name='SPORT').order_by('-publish_time')
        context['siyosat'] = News.objects.all().filter(category__name='SIYOSAT').order_by('-publish_time')

        return context



# SECTION-CONTACT-US

def ContactPageView(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("<h1> Xabaringiz uchun tashakkur")
    context = {
        "form": form
    }
    return render(request, 'news/contact.html', context=context)


# 404-ERROR NOT FIND SECTION

def P4PPageView(request):
    context = {

    }
    return render(request, 'news/404.html', context)



# NAVBARDAGI MENU BO'YICHA ALOHIDA QILIB CHIQARISH UCHUN M: MAHALLIY,SPORT,XORIJ,SIYOSAT

class SiyosatNewsView(ListView):
    model = News
    template_name = 'news/siyosat.html'
    context_object_name = 'siyosat'

    def get_queryset(self):
        single = self.model.objects.all().filter(category__name='SIYOSAT')
        return single


class XorijNewsView(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij'

    def get_queryset(self):
        single = self.model.objects.all().filter(category__name='XORIJ')
        return single



class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport'

    def get_queryset(self):
        single = self.model.objects.all().filter(category__name='SPORT')
        return single




class MahalliyNewsView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy'

    def get_queryset(self):
        single = self.model.objects.all().filter(category__name='MAHALLIY')
        return single

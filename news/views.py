from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from hitcount.utils import get_hitcount_model

from .form import ContactForm, CommentForm
from django.http import HttpResponse
from .models import News, Category
from .models import Comment
from project.custom_permission import OnlyAdminUser
from hitcount.views import HitCountDetailView, HitCountMixin


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

def NewsDetailView(request, id):
    news = News.objects.get(id=id)
    context = {}
    # HITCOUNT COUNT VIEW LOGIC
    hit_count = get_hitcount_model().objects.get_for_object(news)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits+1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hitmassage'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits
    # END COUNT VIEW IS HITCOUNT LOGIC
    comments = news.comments.filter(active=True)
    comment_count = comments.count()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()

    else:
        comment_form = CommentForm()
    context = {
        'news': news,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'comment_count': comment_count,
    }
    return render(request, 'news/news_detail.html', context)





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



# YANGILIKLARNI TAHRIRLASH UCHUN VIEWLAR CREATE,DELETE,UPDATE


class NewsUpdateView(OnlyAdminUser, UpdateView):
    model = News
    template_name = 'rename/edit.html'
    fields = ['title', 'body', 'image', 'category', 'status']


class NewsDeleteView(OnlyAdminUser, DeleteView):
    model = News
    template_name = 'rename/delete.html'
    success_url = reverse_lazy('home')

class NewsCreateView(OnlyAdminUser, CreateView ):
    model = News
    template_name = 'rename/create.html'
    fields = ('title', 'slug', 'body', 'image', 'category', 'status')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def AdminPageView(request):
    admin_page = User.objects.all()

    context = {
        'admin_page': admin_page
    }
    return render(request, 'profile/admin_page.html', context)


class SearchView(ListView):
    model = News
    template_name = 'news/search.html'
    context_object_name = 'search'

    def get_queryset(self):
        result = self.request.GET.get('q')
        return News.objects.filter(
            Q(title__icontains=result) or Q(body__icontains=result)
        )
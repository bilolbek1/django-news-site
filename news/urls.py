from django.urls import path
from .views import NewsAllView, NewsDetailView,HomePageView,ContactPageView,P4PPageView
from .views import SportNewsView,SiyosatNewsView,MahalliyNewsView,XorijNewsView

urlpatterns = [
    path('news/', NewsAllView.as_view(), name='news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('', HomePageView.as_view(), name='home'),
    path('contact-us/', ContactPageView , name='contact'),
    path('404/', P4PPageView, name='404'),
    path('sport/', SportNewsView.as_view(), name='sport_news'),
    path('xorij/', XorijNewsView.as_view(), name='xorij_news'),
    path('siyosat/', SiyosatNewsView.as_view(), name='siyosat_news'),
    path('mahalliy/', MahalliyNewsView.as_view(), name='mahalliy_news')
]

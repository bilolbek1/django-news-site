from django.urls import path
from .views import NewsAllView, NewsDetailView, HomePageView, ContactPageView, P4PPageView
from .views import SportNewsView, SiyosatNewsView, MahalliyNewsView, XorijNewsView
from .views import NewsUpdateView, NewsDeleteView, NewsCreateView, AdminPageView,SearchView, CommentView

urlpatterns = [
    path('news/', NewsAllView.as_view(), name='news'),
    path('news/<int:id>', NewsDetailView, name='news_detail'),
    path('', HomePageView.as_view(), name='home'),
    path('contact-us/', ContactPageView, name='contact'),
    path('404/', P4PPageView, name='404'),
    path('sport/', SportNewsView.as_view(), name='sport_news'),
    path('xorij/', XorijNewsView.as_view(), name='xorij_news'),
    path('siyosat/', SiyosatNewsView.as_view(), name='siyosat_news'),
    path('mahalliy/', MahalliyNewsView.as_view(), name='mahalliy_news'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='edit'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='delete'),
    path('news/create/', NewsCreateView.as_view(), name='create'),
    path('admin-page/', AdminPageView, name='admin-page'),
    path('search-results/', SearchView.as_view(), name='search_results'),
    path('<int:id>/comment/', CommentView.as_view(), name='comment')
]

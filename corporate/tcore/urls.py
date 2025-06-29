from django.urls import path


from .views import  HaberDetayView, PagesView , BlogView, BlogDetailView, EntegrasyonView, IndexView, MisyonumuzView, VizyonumuzView, HakkımızdaView, İBBHaritasıView, İstanbulRotaView,  HaberlerView
from django.conf import settings
from django.conf.urls.static import static
from .views import search

urlpatterns=[

    path('', IndexView.as_view(), name='index'),
    path('misyonumuz', MisyonumuzView.as_view(), name='misyonumuz'),
    path('vizyonumuz',VizyonumuzView.as_view(), name='vizyonumuz'),
    path('hakkımızda',HakkımızdaView.as_view(), name='hakkımızda'),
    path('istanbul-bisiklet-haritası', İBBHaritasıView.as_view(), name='İBBHaritası'),
    path('istanbul-eurovelo-rota-çalışmaları',İstanbulRotaView.as_view(),name='rota'),
    path('entegrasyon', EntegrasyonView.as_view(), name='entegrasyon' ),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('haberler/', HaberlerView.as_view(), name='haberler'),
    path('haberler/<int:pk>/', HaberDetayView.as_view(), name='haber_detay'),
    path('search/', search, name='search'),
   

    path('pages', PagesView.as_view(), name='pages'),
   




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
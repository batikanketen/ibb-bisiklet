from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Blog, Haberler, Pages, Slider, Entegrasyon  
from .forms import SearchForm, BlogSearchForm


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'sliders'
    queryset = Slider.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(page_type='hakkımızda').first
        context['haberler'] = Haberler.objects.all()
        return context
    
    
 
class MisyonumuzView(TemplateView):
    template_name='misyonumuz.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(page_type='misyonumuz').first()
        return context

class VizyonumuzView(TemplateView):
    template_name='vizyonumuz.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(page_type='vizyonumuz').first()
        return context
        
class HakkımızdaView(TemplateView):
    template_name='hakkımızda.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(page_type='hakkımızda').first()
        return context

class İBBHaritasıView(TemplateView):
    template_name='istanbul-bisiklet-haritası.html'

class İstanbulRotaView(TemplateView):
    template_name='rota.html'   


class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Blog'] = Blog.objects.all()
        return context
"""
def blog_search(request):
    query = request.GET.get('q', '')
    if query:
        results = Blog.objects.filter(title__icontains=query)
    else:
        results = Blog.objects.all()
    return render(request, 'blog_search.html', {'results': results, 'query': query})"""
    


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'


class HaberlerView(ListView):
    model = Haberler
    template_name = 'haberler.html'
    context_object_name = 'haberler'
"""
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query) | queryset.filter(description__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
"""   
class HaberDetayView(DetailView):
    model = Haberler
    template_name = 'haber_detay.html'
    context_object_name = 'haber'

        



class PagesView(TemplateView):
    template_name='pages-detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Pages.objects.all()
        return context


class EntegrasyonView(TemplateView):
    template_name = 'entegrasyon.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entegrasyon = Entegrasyon.objects.first()
        context['entegrasyon'] = entegrasyon
        context['anadolu_yakasi_list'] = entegrasyon.anadolu_yakasi.split(',')
        context['avrupa_yakasi_list'] = entegrasyon.avrupa_yakasi.split(',')
        return context
    

def search(request):
    query = request.GET.get('q', '')
    
    haberler_results = Haberler.objects.filter(title__icontains=query)
    blog_results = Blog.objects.filter(title__icontains=query)
    
    return render(request, 'search_results.html', {
        'haberler_results': haberler_results,
        'blog_results': blog_results,
        'query': query
    })  
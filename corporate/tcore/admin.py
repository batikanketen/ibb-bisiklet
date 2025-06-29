from django.contrib import admin

from tcore.models import Blog, Entegrasyon, Haberler, Pages, Settings, Slider, Vizyonumuz, Hakkımızda, Misyonumuz
"""
@admin.register(Hakkımızda)
class HakkımızdaAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
"""
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('logo1', 'logo2', 'footerlogo1', 'footerlogo2', 'anasayfaimg',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image','extraimg1','extraimg2','extraimg3','extraimg4','extraimg5','extraimg6','extraimg7','extraimg8')
    search_fields = ('title',)
    list_filter = ('title',)


    



@admin.register(Entegrasyon)
class EntegrasyonAdmin(admin.ModelAdmin):
     list_display = ('title', 'content', 'image','anadolu_yakasi','avrupa_yakasi',)



@admin.register(Haberler)
class HaberlerAdmin(admin.ModelAdmin):
    list_display = ('title', 'pk','image', 'image1','extraimg1','extraimg2','extraimg3','extraimg4','extraimg5','extraimg6','extraimg7','extraimg8')
    prepopulated_fields = {}  # Slug alanı olmadığından, bu kısmı boş bırakıyoruz




"""
@admin.register(Vizyonumuz)
class VizyonumuzAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

@admin.register(Misyonumuz)
class MisyonumuzAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
"""
@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('title','page_type',)  # 'page_type' yerine 'content' ve 'slug' ekledim



# Sadece bir kez kaydediyoruz
# admin.site.register(Pages, PagesAdmin)  # Bu satırı kaldırın çünkü yukarıda @admin.register ile zaten kayıt ettik

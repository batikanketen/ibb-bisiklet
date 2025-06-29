from django.db import models
from ckeditor.fields import RichTextField



class Settings(models.Model):
    logo1=models.FileField(upload_to='dimg',null=True,blank=True,)
    logo2 = models.FileField(upload_to='dimg',null=True,blank=True,)
    footerlogo1=models.FileField(upload_to='dimg',null=True,blank=True,)
    footerlogo2=models.FileField(upload_to='dimg',null=True,blank=True,)
    anasayfaimg=models.FileField(upload_to='dimg',null=True,blank=True,)


class Slider(models.Model):
    title=models.CharField(max_length=200)
    description=RichTextField()
    image=models.ImageField(upload_to='slider') 

class Hakkımızda(models.Model):
    title=models.CharField(max_length=200)
    content=RichTextField()
    
    def __str__(self):
        return self.title

class Vizyonumuz(models.Model):
    title=models.CharField(max_length=200)
    content=RichTextField()
       
class Misyonumuz(models.Model):
    title=models.CharField(max_length=200)
    content=RichTextField()

    
class Blog(models.Model):
    title=models.CharField(max_length=200)
    content=RichTextField()
    image=models.ImageField(upload_to='dimg',null=True,blank=True,)
    
    extraimg1=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg2=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg3=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg4=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg5=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg6=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg7=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg8=models.ImageField(upload_to='dimg',null=True,blank=True,)


class Haberler(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
        
    image1=models.ImageField(upload_to='dimg',null=True,blank=True,)
    image=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg1=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg2=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg3=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg4=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg5=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg6=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg7=models.ImageField(upload_to='dimg',null=True,blank=True,)
    extraimg8=models.ImageField(upload_to='dimg',null=True,blank=True,)

    def __str__(self):
        return self.title
    



class Pages(models.Model):
    PAGE_TYPE_CHOICES = [
        ('hakkımızda', 'Hakkımızda'),
        ('vizyonumuz', 'Vizyonumuz'),
        ('misyonumuz', 'Misyonumuz'),
    ]
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='dimg', null=True, blank=True)
    page_type = models.CharField(max_length=50, choices=PAGE_TYPE_CHOICES, unique=True)
    

class Entegrasyon(models.Model):
    title = models.CharField(max_length=200)
    content=RichTextField()
    image = models.ImageField(upload_to='dimg')
    anadolu_yakasi = models.TextField(default='')
    avrupa_yakasi = models.TextField(default='')

    def _str_(self):
        return self.title










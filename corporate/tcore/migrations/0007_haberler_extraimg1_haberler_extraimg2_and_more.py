# Generated by Django 5.0.7 on 2024-08-03 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0006_rename_extraimg_blog_extraimg1_blog_extraimg2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='haberler',
            name='extraimg1',
            field=models.ImageField(blank=True, null=True, upload_to='dimg'),
        ),
        migrations.AddField(
            model_name='haberler',
            name='extraimg2',
            field=models.ImageField(blank=True, null=True, upload_to='dimg'),
        ),
        migrations.AddField(
            model_name='haberler',
            name='extraimg3',
            field=models.ImageField(blank=True, null=True, upload_to='dimg'),
        ),
        migrations.AddField(
            model_name='haberler',
            name='extraimg4',
            field=models.ImageField(blank=True, null=True, upload_to='dimg'),
        ),
        migrations.AddField(
            model_name='haberler',
            name='extraimg5',
            field=models.ImageField(blank=True, null=True, upload_to='dimg'),
        ),
        migrations.AddField(
            model_name='haberler',
            name='extraimg6',
            field=models.ImageField(blank=True, null=True, upload_to='dimg'),
        ),
        migrations.AddField(
            model_name='haberler',
            name='extraimg7',
            field=models.ImageField(blank=True, null=True, upload_to='dimg'),
        ),
        migrations.AddField(
            model_name='haberler',
            name='extraimg8',
            field=models.ImageField(blank=True, null=True, upload_to='dimg'),
        ),
        migrations.AlterField(
            model_name='haberler',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dimg'),
        ),
    ]

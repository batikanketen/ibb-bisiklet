# Generated by Django 5.0.7 on 2024-08-07 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0010_entegrasyon_anadolu_yakasi_entegrasyon_avrupa_yakasi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='entegrasyonimg',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='hakkımızdaimg',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='misyonimg',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='vizyonimg',
        ),
    ]

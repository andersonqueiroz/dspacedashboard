# Generated by Django 2.2 on 2019-04-29 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('handle', models.CharField(max_length=30, verbose_name='Nome')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileImport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='imports.Collection', verbose_name='Coleção de destino')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário de importação')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

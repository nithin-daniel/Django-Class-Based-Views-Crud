# Generated by Django 4.1 on 2022-08-30 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Core',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('excerpt', models.TextField(null=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
    ]

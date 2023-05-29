# Generated by Django 4.2.1 on 2023-05-24 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models
import users.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('avatar', models.ImageField(default='profile/default.png', max_length=10000, storage=users.storage.OverwriteStorage(), upload_to=users.models.image_rename)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

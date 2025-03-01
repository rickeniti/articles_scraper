# Generated by Django 5.0.3 on 2024-03-25 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.TextField()),
                ('url', models.URLField()),
                ('image_url', models.URLField()),
                ('publishing_datetime', models.DateTimeField()),
                ('content', models.TextField()),
            ],
        ),
    ]

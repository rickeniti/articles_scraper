# Generated by Django 5.0.3 on 2024-03-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_article_author_alter_article_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_url',
            field=models.TextField(default=''),
        ),
    ]

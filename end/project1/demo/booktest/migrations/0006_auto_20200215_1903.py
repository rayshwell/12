# Generated by Django 3.0.3 on 2020-02-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0005_article_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(to='booktest.Article', verbose_name='tages'),
        ),
    ]
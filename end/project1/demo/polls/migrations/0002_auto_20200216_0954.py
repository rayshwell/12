# Generated by Django 3.0.3 on 2020-02-16 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='content',
            field=models.CharField(max_length=20, verbose_name='投票内容'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='count',
            field=models.FloatField(default=6, verbose_name='投票数量'),
        ),
    ]

# Generated by Django 2.2.5 on 2020-04-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_articlecomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecomments',
            name='email',
            field=models.EmailField(default='aa@gmail.com', max_length=254, verbose_name='邮箱'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlecomments',
            name='nic_name',
            field=models.CharField(default='test', max_length=128, verbose_name='昵称'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlecomments',
            name='web_site',
            field=models.URLField(default='http://pornhub.com', verbose_name='网址'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.2.5 on 2023-10-02 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='posts.tag', verbose_name='Теги'),
        ),
    ]

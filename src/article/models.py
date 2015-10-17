# -*- coding: utf-8 -*-
from django.db import models


class Article(models.Model):
    class Meta():
        db_table = "article"

    article_title = models.CharField(max_length=150)
    article_text = models.TextField()
    article_date = models.DateTimeField()


class Comments(models.Model):
    class Meta():
        db_table = "comments"

    comments_text = models.TextField(verbose_name="Текст коментария")
    comments_article = models.ForeignKey(Article)


class Images(models.Model):
    class Meta():
        db_table = "img"

    images_img = models.ImageField(upload_to="img", verbose_name=u'Photo')
    images_article = models.ForeignKey(Article)

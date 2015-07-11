from django.db import models


class Article(models.Model):
    class Meta():
        db_table = "_article"

    article_title = models.CharField(max_length=150)
    article_text = models.TextField()
    article_data = models.DateTimeField()
    article_likes = models.IntegerField()

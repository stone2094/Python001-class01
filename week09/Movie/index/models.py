from django.db import models

# Create your models here.

class Movies(models.Model):
    # id 自动创建
    name = models.CharField(max_length=50)
    comments = models.CharField(max_length=400)
    stars = models.FloatField()

    #id = models.BigAutoField(primary_key=True)
    #rating = models.IntegerField()
    #content = models.CharField(max_length=400)
    #date = models.DateField()

class T1(models.Model):
    #id = models.BigAutoField(primary_key=True)
    movie_name = models.CharField(max_length=50)
    movie_comments = models.CharField(max_length=400)
    movie_stars = models.FloatField()

    # 元数据，不属于任何一个字段的数据
    class Meta:
        managed = False
        db_table = 'index_movies'
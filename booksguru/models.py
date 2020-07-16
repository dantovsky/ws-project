from django.db import models
import datetime


class Book(models.Model):
    book_id = models.IntegerField(default=0)
    good_reads_book_id = models.IntegerField(default=0)
    isbn = models.CharField(max_length=10)
    isbn13 = models.CharField(max_length=13)
    authors = models.CharField(max_length=250)
    pub_year = models.IntegerField(default=2020)
    title = models.CharField(max_length=250)
    language = models.CharField(max_length=10)
    average_rating = models.FloatField(default=0)
    ratings_count = models.IntegerField(default=0)
    ratings_1 = models.IntegerField(default=0)
    ratings_2 = models.IntegerField(default=0)
    ratings_3 = models.IntegerField(default=0)
    ratings_4 = models.IntegerField(default=0)
    ratings_5 = models.IntegerField(default=0)
    image_url = models.URLField(max_length=500)
    small_image_url = models.URLField()

    def __str__(self):
        return self.title



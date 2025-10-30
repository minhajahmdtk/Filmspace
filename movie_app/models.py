from django.db import models


class Movie(models.Model):
  movie_name=models.CharField(max_length=50)
  movie_year=models.IntegerField()
  movie_language=models.CharField(max_length=50,default='None')
  movie_director=models.CharField(max_length=50)
  movie_descrption=models.TextField()
  movie_image=models.ImageField(upload_to='movie_images')

def __str__(self):
  return self.movie_name

class Series(models.Model):
  series_name=models.CharField(max_length=50)
  series_year=models.CharField(max_length=50)
  series_language=models.CharField(max_length=50,default='None')
  series_seasons=models.IntegerField()
  series_director=models.CharField(max_length=50)
  series_descrption=models.TextField()
  series_image=models.ImageField(upload_to='series_images')

def __str__(self):
  return self.series_name

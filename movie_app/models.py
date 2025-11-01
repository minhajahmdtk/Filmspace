from django.db import models


class Movie(models.Model):
  movie_name=models.CharField(max_length=50)
  movie_year=models.IntegerField()
  movie_language=models.CharField(max_length=20,default='None')
  movie_genre=models.CharField(max_length=50,default='None')
  movie_director=models.CharField(max_length=50)
  movie_description=models.TextField()
  movie_image=models.ImageField(upload_to='movie_images')

  def __str__(self):
    return self.movie_name

class Series(models.Model):
  series_name=models.CharField(max_length=50)
  series_year=models.CharField(max_length=10)
  series_language=models.CharField(max_length=10,default='None')
  series_genre=models.CharField(max_length=20,default='None')
  series_seasons=models.CharField(max_length=20)
  series_director=models.CharField(max_length=50)
  series_description=models.TextField()
  series_image=models.ImageField(upload_to='series_images')

  def __str__(self):
   return self.series_name

class MovieWatchlist(models.Model):
    movie_name = models.CharField(max_length=20)
    movie_year = models.IntegerField()
    movie_genre = models.CharField(max_length=20)
    movie_image = models.ImageField(upload_to='movie_watchlist')

    def __str__(self):
        return self.movie_name
    
class SeriesWatchlist(models.Model):
    series_name = models.CharField(max_length=20)
    series_year = models.CharField(max_length=10)
    series_genre = models.CharField(max_length=20)
    series_seasons = models.CharField(max_length=20)
    series_image = models.ImageField(upload_to='series_watchlist')

    def __str__(self):
        return self.series_name
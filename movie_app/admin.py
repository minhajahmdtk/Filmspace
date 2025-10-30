from django.contrib import admin
from .models import Movie,Series,MovieWatchlist,SeriesWatchlist

admin.site.register(Movie)
admin.site.register(Series)
admin.site.register(MovieWatchlist)
admin.site.register(SeriesWatchlist)
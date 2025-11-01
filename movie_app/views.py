from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from .models import Movie,Series,MovieWatchlist,SeriesWatchlist




def index(request):
  return render(request,'index.html')

def home(request):
  return render(request,'home.html')

def login(request):
  if request.method=="POST":
    user_name=request.POST['username']
    password=request.POST['password']

    user=auth.authenticate(username=user_name,password=password)
    if user is not None:
      auth.login(request,user)
      return redirect('home')
    else:
      messages.info(request,"Invalid usrename or password ")
      return redirect('login')
    
  return render(request,"login.html")

def logout(request):
  auth.logout(request)
  return redirect('index')

def register(request):
  if request.method=="POST":
    username=request.POST['user_name']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    gmail=request.POST['email']
    password=request.POST['pass_word']
    confirm=request.POST['confirm']

    if confirm==password:
      if User.objects.filter(username=username).exists():
        messages.info(request,"Username already exist!!!")
        return redirect('register')
      elif User.objects.filter(email=gmail).exists():
        messages.info(request,"Email already exsit!!!!")
        return redirect('register')
      else:
        reg=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=gmail,password=password)
        reg.save()
        return redirect('login')
  return render(request,'register.html')


def movies(request):
  movies=Movie.objects.all()
  paginator=Paginator(movies,9)
  page=int(request.GET.get('page',1))
  try:
    movies=paginator.page(page)
  except (InvalidPage,EmptyPage):
    movies=paginator.page(paginator.num_pages)
  return render(request,'movies.html',{"mov1":movies})

def series(request):
  series=Series.objects.all()
  paginator=Paginator(series,9)
  page=int(request.GET.get('page',1))
  try:
    series=paginator.page(page)
  except (InvalidPage,EmptyPage):
    series=paginator.page(paginator.num_pages)
  return render(request,'series.html',{"ser1":series})


def add_movie_watchlist(request,movie_id):
  page = request.GET.get('page', 1)
  try:
    movie_watch=Movie.objects.get(id=movie_id)
  except Movie.DoesNotExist:
    messages.error(request,"Movie not found!!!")
    return redirect('movies')
  
  if not MovieWatchlist.objects.filter(movie_name=movie_watch.movie_name).exists():
    MovieWatchlist.objects.create(
            movie_name=movie_watch.movie_name,
            movie_year=movie_watch.movie_year,
            movie_genre=movie_watch.movie_genre,
            movie_image=movie_watch.movie_image
        )
  else:
    messages.info(request,f'"{movie_watch.movie_name}" already exists in Watchlist!')
  return redirect(f'/movies?page={page}')


def add_series_watchlist(request,series_id):
  page = request.GET.get('page', 1)
  try:
    series_watch=Series.objects.get(id=series_id)
  except Series.DoesNotExist:
    messages.error(request,"Series not Found")
    return redirect('series')
  
  if not SeriesWatchlist.objects.filter(series_name=series_watch.series_name).exists():
     SeriesWatchlist.objects.create(
            series_name=series_watch.series_name,
            series_year=series_watch.series_year,
            series_genre=series_watch.series_genre,
            series_seasons=series_watch.series_seasons,
            series_image=series_watch.series_image
        )
  else:
    messages.info(request,f'"{series_watch.series_name}" already exists in Watchlist!')
  return redirect(f'/series?page={page}')
        
def movie_watchlist(request):
    mov_watch = MovieWatchlist.objects.all()
    pag=Paginator(mov_watch,9)
    page=int(request.GET.get('page',1))
    try:
      mov_watchlist=pag.page(page)
    except (InvalidPage,EmptyPage):
      mov_watchlist=pag.page(pag.num_pages)
    return render(request, 'movie_watchlist.html', {'mov_watch':mov_watchlist})


def remove_movie_watchlist(request,wm_id):
    page = request.GET.get('page', 1)
    try:
        ws_delete = MovieWatchlist.objects.get(id=wm_id)
        ws_delete.delete()
    except MovieWatchlist.DoesNotExist:
        messages.warning(request, "No movie found on the watchlist.")
    
    return redirect(f'/movie_watchlist?page={page}')



def series_watchlist(request):
    ser_watch = SeriesWatchlist.objects.all()
    sr_watchlist=Paginator(ser_watch,9)
    page=int(request.GET.get('page',1))

    try:
      ser_watchlist=sr_watchlist.page(page)
    except (InvalidPage,EmptyPage):
      ser_watchlist=sr_watchlist.page(sr_watchlist.num_pages)
    return render(request, 'series_watchlist.html', {'sr_watch': ser_watchlist})

  
def remove_series_watchlist(request,ws_id):
  page = request.GET.get('page', 1)
  try:
    ws_delete=SeriesWatchlist.objects.get(id=ws_id)
    ws_delete.delete()
  except SeriesWatchlist.DoesNotExist:
        messages.warning(request, "No series found on the watchlist.")
  return redirect(f'/series_watchlist?page={page}')



#-------Admin-------


def admin_login(request):
  if request.method=="POST":
    user_name=request.POST['username']
    password=request.POST['password']

    user=auth.authenticate(username=user_name,password=password)
    if user is not None:
      auth.login(request,user)
      return redirect('admin_home')
    else:
      messages.info(request,"Invalid username or password!!! ")
      return redirect('admin_login')
    
  return render(request,"admin_login.html")

def admin_home(request):
  total_movies=Movie.objects.count()
  total_series=Series.objects.count()
  return render(request,'admin_home.html',{'total_movies':total_movies,'total_series':total_series})

#--------Movie------
#(Update,Delete,Add)
#--------Movie------

def add_movie(request):
    if request.method=="POST":
      movie_name=request.POST['movie_name']
      movie_year=request.POST['movie_year']
      movie_language=request.POST['movie_language']
      movie_genre=request.POST['movie_genre']
      movie_director=request.POST['movie_director']
      movie_description=request.POST['movie_description']
      movie_image=request.FILES['movie_image']
      movie_data=Movie(movie_name=movie_name,movie_year=movie_year,movie_language=movie_language,movie_genre=movie_genre,movie_director=movie_director,movie_description=movie_description,movie_image=movie_image)
      movie_data.save()
      return redirect('admin_home')
    return render(request,'add_movie.html')


def admin_manage_movies(request):
  admin_movies_list=Movie.objects.all()
  paginator=Paginator(admin_movies_list,9)
  page=request.GET.get('page',1)
  try:
    admin_movies=paginator.page(page)
  except (InvalidPage,EmptyPage):
    admin_movies=paginator.page(paginator.num_pages)
  return render(request,'admin_manage_movies.html',{'admin_movies':admin_movies})

def update_movie(request, p_id):
    m_update = Movie.objects.get(id=p_id)

    if request.method == "POST":
        m_update.movie_name = request.POST['movie_name']
        m_update.movie_year = request.POST['movie_year']
        m_update.movie_language = request.POST['movie_language']
        m_update.movie_genre = request.POST['movie_genre']
        m_update.movie_director = request.POST['movie_director']
        m_update.movie_description = request.POST['movie_description']

        
        if 'movie_image' in request.FILES:
            m_update.movie_image = request.FILES['movie_image']
        m_update.save()
        return redirect('admin_home')
    return render(request, 'update_movie.html', {'movie': m_update})

def delete_movie(request,delete_mov):
  delete=Movie.objects.get(id=delete_mov)
  delete.delete()
  return redirect('admin_manage_movies')

#--------Series------
#(Update,Delete,Add)
#--------Series------
def add_series(request):
  if request.method=="POST":
    series_name=request.POST['series_name']
    series_year=request.POST['series_year']
    series_language=request.POST['series_language']
    series_genre=request.POST['series_genre']
    series_seasons=request.POST['series_seasons']
    series_director=request.POST['series_director']
    series_description=request.POST['series_description']
    series_image=request.FILES['series_image']
    series_data=Series(series_name=series_name,series_year=series_year,series_language=series_language,series_genre=series_genre,series_seasons=series_seasons,series_director=series_director,series_description=series_description,series_image=series_image)
    series_data.save()
    return redirect('admin_home')
  return render(request,'add_series.html')




def admin_manage_series(request):
  admin_series_list=Series.objects.all()
  paginator=Paginator(admin_series_list,9)
  page=request.GET.get('page',1)
  try:
    admin_series=paginator.page(page)
  except (InvalidPage,EmptyPage):
    admin_series=paginator.page(paginator.num_pages)

  return render(request,'admin_manage_series.html',{'admin_series':admin_series})


def update_series(request, up_id):
    s_update = Series.objects.get(id=up_id)
    if request.method == "POST":
        s_update.series_name = request.POST['series_name']
        s_update.series_year = request.POST['series_year']
        s_update.series_language = request.POST['series_language']
        s_update.series_genre = request.POST['series_genre']
        s_update.series_seasons = request.POST['series_seasons']
        s_update.series_director = request.POST['series_director']
        s_update.series_description = request.POST['series_description']

        
        if 'series_image' in request.FILES:
            s_update.series_image = request.FILES['series_image']
        s_update.save()
        return redirect('admin_home')
    return render(request, 'update_series.html', {'series': s_update})



def delete_series(request,delete_ser):
  delete=Series.objects.get(id=delete_ser)
  delete.delete()
  return redirect('admin_manage_series')

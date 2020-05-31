from django.shortcuts import render
from django.views.generic import (
	ListView,
	DetailView,
	)
from .models import Song,Instrumental,Video
from .filters import SongFilter
from django.core.paginator import Paginator
from django.db.models import Q
from urllib.parse import quote_plus

# Create your views here.
def songs(request):

	songs_list = Song.objects.all().order_by('-date_posted')


	query = request.GET.get('q')
	qs = Song.objects.all().order_by('-date_posted')
	if query is not None:
		qs = qs.filter(
			Q(title__icontains=query) |
			Q(artist__icontains=query)
			)

	paginator = Paginator(qs, 3)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		qs = paginator.page(page)
	except (EmptyPage, Invalidpage):
		qs = paginator.page(paginator.num_pages)


	share_string = quote_plus(instance.songs)

	context = {
	    'songs':qs,
	    'share_string':share_string
	}
	return render(request, 'features/songs.html',context)



class SongDetailView(DetailView):
	model = Song

	

def instrumentals(request):

	query = request.GET.get('q')
	qs = Instrumental.objects.all().order_by('-date_posted')
	if query is not None:
		qs = qs.filter(
			Q(title__icontains=query) 
			)

	paginator = Paginator(qs, 1)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		qs = paginator.page(page)
	except (EmptyPage, Invalidpage):
		qs = paginator.page(paginator.num_pages)

	context = {
	    'instrumentals':qs,
	    
	}
	return render(request, 'features/instrumentals.html',context)



class InstrumentalDetailView(DetailView):
	model = Instrumental


def videos(request):

	query = request.GET.get('q')
	qs = Video.objects.all().order_by('-date_posted')
	if query is not None:
		qs = qs.filter(
			Q(title__icontains=query) |
			Q(artist__icontains=query)
			)

	paginator = Paginator(qs, 1)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		qs = paginator.page(page)
	except (EmptyPage, Invalidpage):
		qs = paginator.page(paginator.num_pages)

	context = {
	    'videos':qs,
	    
	}
	return render(request, 'features/videos.html',context)



class VideoDetailView(DetailView):
	model = Video
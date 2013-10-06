# Create your views here.
from django.shortcuts import render_to_response

def map(request):
	return render_to_response('map.html')

def geoj(request):
	pass

def search(request):
	return render_to_response("search.html")

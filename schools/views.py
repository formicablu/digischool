# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse

import json

from .models import *

def index(request):
	return render_to_response('intro.html')

def map(request):
	return render_to_response('map.html')

def mapping(request):
	ret = {m.id:m.name for m in MetricType.objects.all()}
	return HttpResponse(json.dumps(ret))

def geoj(request):
	bbox = request.REQUEST.get('bb')
	ret = { "type": "FeatureCollection",
	  "features": [
	    { "type": "Feature",
	      "geometry":json.loads(school.position.json),
	      "properties": {
	      	"name":school.name,
	      	"id":school.id,
	      	"metrics":school.all_metrics()
	      	}
	      }
	    for school in School.objects.all()]
	   } 
	return HttpResponse(json.dumps(ret))

def search(request):
	return render_to_response("search.html")

def evaluate(request):
	school = request.REQUEST.get('school')
	if school is not None:
		return render_to_response('evaluate.html', {"school":School.objects.get(id=school)})

	else:
		return render_to_response('evaluate_search.html', {"schools":School.objects.all().values('name', 'id')})

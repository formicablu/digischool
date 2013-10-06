from django.shortcuts import render_to_response

def timeline(request):
	return render_to_response("timeline.html")
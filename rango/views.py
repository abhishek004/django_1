from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

def index(request):
	context=RequestContext(request)
	context_dict={'boldmessage':"I'm bold font from context"}
	return render_to_response("index.html",context_dict,context)
	#return HttpResponse("Hello world! <a href='/rango/about'>About</a>")

def about(request):
	return HttpResponse("Page requested - About <a href='/rango'>Main</a>")
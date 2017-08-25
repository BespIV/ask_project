
from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect

def test(request, *args, **kwargs):
	return HttpResponse('OK')
# Create your views here.

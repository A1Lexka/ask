from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)

#def error(request):
#    return Http404("It's an error")

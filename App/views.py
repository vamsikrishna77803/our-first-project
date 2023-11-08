from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jampandu(request):
    return HttpResponse('<h1><marquee>hi jigelRani Em chesthunav</marquee></h1>')
def jigelrani(request):
    return HttpResponse('<h1><marquee >Iam busy with chitti-Babu</marquee></h1>')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	data_list = {'first','second','third'}
	context = { 'data_list': data_list }
	return render(request, 'cms/index.html', context)


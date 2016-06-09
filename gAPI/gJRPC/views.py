from django.shortcuts import render
from django.http import HttpResponse
from jsonrpc import jsonrpc_method
# Create your views here.

def home(request):
	return HttpResponse('Home')

@jsonrpc_method('asd')
def echo_test(request, name='Blank'):
	return name
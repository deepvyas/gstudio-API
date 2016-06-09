from django.shortcuts import render
from django.http import HttpResponse
from jsonrpc import jsonrpc_method
try:
	from bson import ObjectId
except ImportError:  # old pymongo
	from pymongo.objectid import ObjectId

from django_mongokit import get_database
from models import *
import json


def home(request):
	return HttpResponse('Home')

@jsonrpc_method('fetch')
def mongo_fetch(request):
	collections = get_database()[DataMe.collection_name]
	data_docs = collections.DataMe.find_one()
	resp = {}
	resp['name'] = data_docs['name']
	resp['surname'] = data_docs['surname']
	return json.dumps(str(resp),ensure_ascii=False)

@jsonrpc_method('save')
def mongo_add(request, name='Smit', surname='Patwa', ustr='Pingu'):
	collections = get_database()[DataMe.collection_name]
	obj = collections.DataMe()
	obj['name'] = name
	obj['surname'] = surname
	obj['ur_str'] = ustr
	obj.save()
	return 'Saved'

@jsonrpc_method('delete')
def mongo_remove(request, name, surname, ustr):
	collections = get_database()[DataMe.collection_name]
	return str(collections.remove({'name':name,'surname':surname,'ustr': ustr}))

@jsonrpc_method('asd')
def echo_test(request, name='Blank'):
	return name
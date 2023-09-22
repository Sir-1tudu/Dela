from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django.core import serializers
from . models import User_details


# Create your views here.

def home(request):
    data = User_details.objects.all()
    serialize_data = serializers.serialize('json', data)
    return JsonResponse({"data": serialize_data})

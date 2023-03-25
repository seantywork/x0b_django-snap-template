from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from ..models import models
import json

def getIndex(request):
    context = {}
    return HttpResponse(render(request,'index.html',context))

def searchWord(request):

    post_dict = json.loads(request.body)
    
    x = post_dict["query"]
    x = str(x)

    context = models.searchWord(x)

    return JsonResponse(context)




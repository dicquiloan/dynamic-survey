from django.shortcuts import render

from django.http import HttpResponse
from .models import Question

def index(request):
        dataDict = {
                'questionList': Question.objects.all(),
                }
        return render(request, 'LApoll/index.html', dataDict)
        
    
        

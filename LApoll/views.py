from django.shortcuts import render

from django.http import HttpResponse
from .models import Question

def index(request):
        dataDict = {
                'questionList': Question.objects.all(),
                }
        return render(request, 'LApoll/survey.html', dataDict)
def showResults(request):
	return HttpResponse("YOU SUBMITTED THE FORM")	 

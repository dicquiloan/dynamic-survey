from django.shortcuts import render

from django.http import HttpResponse
from .models import *

def index(request):
        dataDict = {
                'questionList': Question.objects.all(),
                }
        return render(request, 'LApoll/survey.html', dataDict)

def showResultsWithoutDB(request):
	if request.method != 'POST':
		return redirect('')

	responseList = []
	for x in range (1,21):
		responseList.append({
			'questionText': Question.objects.get(id=x).text,
			'answer': 1 if request.POST.__contains__(('answer'+str(x))) else 0,
			'rating': int(request.POST['rating'+str(x)])
		})
	dataDict = {
		'responseList':  responseList,
		'livesInLA': 1 if request.POST.__contains__(('livesInLA')) else 0
	}

	return render(request, 'LApoll/results.html', dataDict)



'''
NAME: 
	showResults
PSEUDOCODE:
	if not posting
		redirect
	
	populate list of answers from form
		question text
		answer as int
		rating as int
	
	create new participant using livesInLA from form
	save participant to db
	for each question
		generate questionResponse with participant ID and form answer/rating
		save it

'''

def showResults(request):
	if request.method != 'POST':
		return redirect('')

	responseList = []
	for x in range (1,21):
		responseList.append({
			'questionText': Question.objects.get(id=x).text,
			'answer': 1 if request.POST.__contains__(('answer'+str(x))) else 0,
			'rating': int(request.POST['rating'+str(x)])
		})
	
	
	participantLivesInLA =  1 if request.POST.__contains__('livesInLA') else 0

	p = Participant(livesInLA = participantLivesInLA)
	p.save()
	
	for x in range (0,20):
		qr = QuestionResponse(participant = p, question = Question.objects.get(pk=x+1), answer = responseList[x]['answer'], rating = responseList[x]['rating'])
		qr.save()

	#CALL MODEL GENERATING/PREDICTION ALGORITHMS HERE

	dataDict = {
		'responseList': QuestionResponse.objects.filter(participant=p),
		'livesInLA': p.livesInLA,
		#ADD VALUES TO DISPLAY HERE
	}

	return render(request, 'LApoll/results.html', dataDict)

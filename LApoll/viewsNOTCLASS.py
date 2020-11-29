from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .algorithms import *
import random

def index(request):
	dataDict = {
		'coolGuyName': 'Chen Wei',
		'questionList': Question.objects.all().order_by('?')
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
			'answer': int(request.POST['answer'+str(x)]),
			'rating': int(request.POST['rating'+str(x)])
		})
	
	
	participantLivesInLA =  int(request.POST['livesInLA'])

	p = Participant(livesInLA = participantLivesInLA)
	p.save()
	
	for x in range (0,20):
		qr = QuestionResponse(participant = p, question = Question.objects.get(pk=x+1), answer = responseList[x]['answer'], rating = responseList[x]['rating'])
		qr.save()

	#CALL MODEL GENERATING/PREDICTION ALGORITHMS HERE

	questionStatsList= [ {'avgAnswer': knn.avgQuestionAnswer(qid), 'avgRating': knn.avgQuestionRating(qid)} for qid in range(1,21) ] 	

	dataDict = {
		'responseList': QuestionResponse.objects.filter(participant=p),
		'livesInLA': p.livesInLA,
		#ADD VALUES TO DISPLAY HEREa
		'questionStatsList': questionStatsList
	}

	return render(request, 'LApoll/results.html', dataDict)


def showComparison(request):
	#default min and max IDs extend the whole range of participants
	minTrainingID = 1
	maxTrainingID = Participant.objects.count()
	minTestingID = 1
	maxTestingID = Participant.objects.count()
		
	#if the user hit submit button, use form submitted values for ID ranges
	if request.method=="POST":
		minTrainingID = int(request.POST['minTrainingID'])
		maxTrainingID = int(request.POST['maxTrainingID'])
		minTestingID = int(request.POST['minTestingID'])
		maxTestingID = int(request.POST['maxTestingID'])
		
	# if min and max are out of order, swap them 	
	if minTrainingID > maxTrainingID:
		temp = minTrainingID
		minTrainingID = maxTrainingID
		maxTrainingID = temp

	if minTestingID > maxTestingID:
		temp = minTestingID
		minTestingID = maxTestingID
		maxTestingID = temp	
	
	#set set sizes
	trainingSetSize = maxTrainingID-minTrainingID + 1
	testingSetSize = maxTestingID - minTestingID + 1 
	#get guesses for each approach
	KNNGuessedCorrectly = knn.guessedCorrectly(minTrainingID, maxTrainingID, minTestingID, maxTestingID)
	SVMGuessedCorrectly = svm.guessedCorrectly(minTrainingID, maxTrainingID, minTestingID, maxTestingID)
	#'LRGuessedCorrectly': lr.guessedCorrectly(minTrainingID, maxTrainingID, minTestingID, maxTestingID)
	#'RBMGuessedCorrectly': rbm.guessedCorrectly(minTrainingID, maxTrainingID, minTestingID, maxTestingID)
	
	dataDict = {
		'minID' : 1,
		'maxID' : Participant.objects.count(),
		'minTrainingID': minTrainingID,
		'maxTrainingID': maxTrainingID,
		'minTestingID': minTestingID,
		'maxTestingID': maxTestingID,
		'trainingSetSize': maxTrainingID-minTrainingID+1,
		'testingSetSize': maxTestingID-minTestingID +1 ,
		
		'KNNGuessedCorrectly': KNNGuessedCorrectly,
		'KNNGuessedIncorrectly': testingSetSize - KNNGuessedCorrectly,
		'KNNPercentGuessedCorrectly': KNNGuessedCorrectly / testingSetSize,
		'SVMGuessedCorrectly': SVMGuessedCorrectly, 	
		'SVMGuessedIncorrectly': testingSetSize - SVMGuessedCorrectly,
		'SVMPercentGuessedCorrectly': SVMGuessedCorrectly / testingSetSize,
		'percentFromLA': utils.participantCountFromLAInRange(minTrainingID, maxTrainingID) / trainingSetSize

	}

	return render(request, 'LApoll/compare.html', dataDict)

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

	#create model collection sets (should always include all participants except current)	
	trainingQRCollection = utilsClass.getQuestionResponsesInParticipantRange(1, p.id -1);
	testingQRCollection = utilsClass.getQuestionResponsesInParticipantRange(1, Participant.objects.count())
	participantCollection = utilsClass.getParticipantsInRange(1, Participant.objects.count())

	#generate classification probability for this participant using all previous
	KNNProb = knn.generateKNNCategorizationProbability(trainingQRCollection, testingQRCollection, participantCollection, p.id)
	brianProb = brianClass.BrianModel(trainingQRCollection, testingQRCollection,participantCollection).probabilityLivesInLA(p.id)

	#booleans for whether approaches classified correctly
	KNNGuessedCorrectly = KNNProb > .5 if p.livesInLA else knnProb <=.5
	BrianGuessedCorrectly = brianProb > .5 if p.livesInLA else brianProb <=.5

	dataDict = {
		'responseList': QuestionResponse.objects.filter(participant=p),
		'livesInLA': p.livesInLA,
		'trainingSetSize': Participant.objects.count(),
		'KNNCategorizationProbability': KNNProb,
		'KNNGuessedCorrectly' : KNNGuessedCorrectly, 
		'BrianCategorizationProbability': brianProb,
		'BrianGuessedCorrectly': BrianGuessedCorrectly 
	}

	return render(request, 'LApoll/results.html', dataDict)


def showComparison(request):
	#default min and max IDs extend the whole range of participants
	minTrainingID = 1
	maxTrainingID = Participant.objects.count()
	minTestingID = 1
	maxTestingID = Participant.objects.count()
	trainWithOnlyLA = False
		
	#if the user hit submit button, use form submitted values for ID ranges
	if request.method=="POST":
		minTrainingID = int(request.POST['minTrainingID'])
		maxTrainingID = int(request.POST['maxTrainingID'])
		minTestingID = int(request.POST['minTestingID'])
		maxTestingID = int(request.POST['maxTestingID'])
		trainWithOnlyLA = True if 'trainWithOnlyLA' in request.POST else False
		
	# if min and max are out of order, swap them 	
	if minTrainingID > maxTrainingID:
		temp = minTrainingID
		minTrainingID = maxTrainingID
		maxTrainingID = temp

	if minTestingID > maxTestingID:
		temp = minTestingID
		minTestingID = maxTestingID
		maxTestingID = temp	
	
	#get Model Arrays for test set, training set, participant set
	trainingQRCollection = utilsClass.getQuestionResponsesInParticipantRange(minTrainingID, maxTrainingID, trainWithOnlyLA)
	#whole goal is to check accuracy on predictions across the board. training can
	#be filtered by "only in la" but not testing
	testingQRCollection = utilsClass.getQuestionResponsesInParticipantRange(minTestingID, maxTestingID, False)
	participantCollection = utilsClass.getParticipantsInRange(minTestingID, maxTestingID)	

	#calculate set sizes
	#will be multiple QRs for each participant, so count only QRs with question id 1 to 
	#get number of participants 
	trainingSetSize = trainingQRCollection.filter(question__id=1).count()
	testingSetSize = testingQRCollection.filter(question__id =1).count()
	
	#make predictions
	KNNGuessedCorrectly = knn.guessedCorrectly(trainingQRCollection, testingQRCollection, participantCollection)
	#SVM algorithm needs target array with variation
	if trainWithOnlyLA:
		SVMGuessedCorrectly = 0
	else:
		SVMGuessedCorrectly = svm.guessedCorrectly(trainingQRCollection, testingQRCollection, participantCollection)

	
	brianModel = brianClass.BrianModel(trainingQRCollection, testingQRCollection, participantCollection)
	BrianGuessedCorrectly = brianModel.guessedCorrectly(.5)
		
	
	dataDict = {
		'minID' : 1,
		'maxID' : Participant.objects.count(),
		'minTrainingID': minTrainingID,
		'maxTrainingID': maxTrainingID,
		'minTestingID': minTestingID,
		'maxTestingID': maxTestingID,
		'trainingSetSize': trainingSetSize,
		'testingSetSize': testingSetSize, 	
		'KNNGuessedCorrectly': KNNGuessedCorrectly,
		'KNNGuessedIncorrectly': testingSetSize - KNNGuessedCorrectly,
		'KNNPercentGuessedCorrectly': KNNGuessedCorrectly / testingSetSize,
		'SVMGuessedCorrectly': SVMGuessedCorrectly, 	
		'SVMGuessedIncorrectly': 0 if trainWithOnlyLA else testingSetSize - SVMGuessedCorrectly, 
		'SVMPercentGuessedCorrectly': SVMGuessedCorrectly / testingSetSize,
		'BrianGuessedCorrectly': BrianGuessedCorrectly,
		'BrianGuessedIncorrectly': testingSetSize - BrianGuessedCorrectly,
		'BrianPercentGuessedCorrectly': BrianGuessedCorrectly / testingSetSize,
		'percentFromLA': utils.participantCountFromLAInRange(minTrainingID, maxTrainingID) / trainingSetSize
	}

	return render(request, 'LApoll/compare.html', dataDict)

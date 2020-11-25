from  ..models import *
import functools
import numpy

def dumpObject(inObj):
	for property, value in vars(inObj).items():
		print(property, ":", value)

def answersAsFeaturesArray(minParticipantID, maxParticipantID):
	featuresList = []
	for participant in Participant.objects.filter(id__range=(minParticipantID, maxParticipantID)):
		featuresList.append([qr.answer for qr in QuestionResponse.objects.filter(participant__id = participant.id)])
	return numpy.array(featuresList)

def answersAsFeaturesArrayAll():
	featuresList = []
	for participant in Participant.objects.all():
		featuresList.append([qr.answer for qr in QuestionResponse.objects.filter(participant__id = participant.id)])
	return numpy.array(featuresList)

def livesInLAAsTargetArray(minParticipantID, maxParticipantID):
	return numpy.array([p.livesInLA for p in Participant.objects.filter(id__range=(minParticipantID, maxParticipantID))])

def livesInLAAsTargetArrayAll():
	return numpy.array([p.livesInLA for p in Participant.objects.all()])

def answersFromParticipant(pid):
	return numpy.array([qr.answer for qr in QuestionResponse.objects.filter(participant__id = pid)]) 

def ratingsForQuestion(qid):
	return numpy.array([qr.rating for qr in QuestionResponse.objects.filter(question__id = qid)])

def getQuestionResponseRatingAverageForQuestion(qid):
	ratingsForQuestion = getQuestionResponseRatingsForQuestion(qid)
	return functools.reduce(lambda x,y : x+y, ratingsForQuestion, 0)/len(ratingsForQuestion)

def numberFromLAInRange(minPID, maxPID):
	return Participant.objects.filter(id__gte = minPID).filter(id__lte = maxPID).filter(livesInLA = 1).count()

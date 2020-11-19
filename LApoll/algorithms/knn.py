from  ..models import *
import numpy


def avgQuestionAnswer(questionID):
	total = 0
	questionResponseList = QuestionResponse.objects.filter(question__id = questionID)
	for qr in questionResponseList:
		total = total + qr.answer
	return total / len(questionResponseList)

def avgQuestionRating(questionID):
	total = 0
	questionResponseList = QuestionResponse.objects.filter(question__id = questionID)
	for qr in questionResponseList:
		total = total + qr.rating
	return total / len(questionResponseList)

def dumpObject(inObj):
	for property, value in vars(inObj).items():
		print(property, ":", value)

'''
	for each participant
		for each question Id 
			get question response answer

WE NEED TO BE REALLY CAREFUL ABOUT THE ORDERING OF QUERY RESULTS TO MATCH EVERYTHING UP
'''

def getQuestionResponseAnswersAsFeaturesArray():
	featuresList = []
	for participant in Participant.objects.all():
		featuresList.append([qr.answer for qr in QuestionResponse.objects.filter(participant__id = participant.id)])
	return numpy.array(featuresList)

def getLivesInLAAsTargetArray():
	return numpy.array([p.livesInLA for p in Participant.objects.all()])

def getQuestionResponseAnswersFromParticipant(pid):
	return numpy.array(qr.answer for qr in QuestionResponse.objects.filter(participant__id = pid)) 

def getQuestionResponseRatingsForQuestion(qid):
	return [qr.rating for qr in QuestionResponse.objects.filter(question__id = qid)]

def getAverageQuestionResponseRatingForQuestion(qid):
	ratingsForQuestion = getQuestionResponseRatingsForQuestion(qid)
	return 

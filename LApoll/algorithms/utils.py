from  ..models import *
import functools
import numpy

def dumpObject(inObj):
	for property, value in vars(inObj).items():
		print(property, ":", value)

#FEATURES ARRAYS####################################################################

def answersAsFeaturesArray(minParticipantID, maxParticipantID):
	featuresList = []
	for participant in Participant.objects.filter(id__range=(minParticipantID, maxParticipantID)):
		featuresList.append([qr.answer for qr in QuestionResponse.objects.filter(participant__id = participant.id)])
	return numpy.array(featuresList)

#TARGET ARRAYS########################################################################

def livesInLAAsTargetArray(minParticipantID, maxParticipantID):
	return numpy.array([p.livesInLA for p in Participant.objects.filter(id__range=(minParticipantID, maxParticipantID))])

#ANSWERS##############################################################################

def answersFromParticipant(pid):
	return numpy.array([qr.answer for qr in QuestionResponse.objects.filter(participant__id = pid)]) 

def answersForQuestion(qid, minPID, maxPID):
	return [qr.answer for qr in QuestionResponse.objects.filter(question__id = qid).filter(participant__id__range=(minPID, maxPID))]

def mostCommonAnswerForQuestion(qid, minPID, maxPID):
	answer0Count = len(list(filter(lambda a : a==0, answersForQuestion(qid, minPID, maxPID))))
	return 1 if (answer0Count < len(answersForQuestion(qid,minPID,maxPID))/2) else 0 

def answerForUserForQuestion(pid, qid):
	return QuestionResponse.objects.filter(participant__id = pid).filter(question__id = qid)[0].answer

#RATINGS###############################################################################

def ratingsForQuestionAll(qid):
	return numpy.array([qr.rating for qr in QuestionResponse.objects.filter(question__id = qid)])

def ratingsForQuestion(qid, minTrainingID, maxTrainingID):
	qrList = QuestionResponse.objects.filter(question__id = qid).filter(participant__id__range=(minTrainingID, maxTrainingID))
	return numpy.array([qr.rating for qr in qrList])

def ratingAvgForQuestion(qid, minTrainingID, maxTrainingID):
	ratingsArray = ratingsForQuestion(qid, minTrainingID, maxTrainingID)
	return functools.reduce(lambda x,y : x+y, ratingsArray, 0)/len(ratingsArray)

def sumOfAvgRatings(minPID, maxPID):
	return functools.reduce(lambda x,y : x+y, [ratingAvgForQuestion(x, minPID, maxPID) for x in range(1, 21)])

#PARTICIPANTS##########################################################################

def participantCountFromLAInRange(minPID, maxPID):
	return Participant.objects.filter(id__gte = minPID).filter(id__lte = maxPID).filter(livesInLA = 1).count()

from  ..models import *
import functools
import numpy

def dumpObject(inObj):
	for property, value in vars(inObj).items():
		print(property, ":", value)


#DJANGO MODEL COLLECTION GETTERS#########################################################
def getQuestionResponsesInParticipantRange(minParticipantID, maxParticipantID, onlyFromLA):
	if onlyFromLA: 
		return QuestionResponse.objects.order_by("participant__id").filter(participant__id__range = (minParticipantID, maxParticipantID)).filter(participant__livesInLA = 1)
	else:
		return QuestionResponse.objects.order_by("participant__id").filter(participant__id__range = (minParticipantID, maxParticipantID))

def getParticipantsInRange(minParticipantID, maxParticipantID, onlyFromLA):
	if onlyFromLA:
		return Participant.objects.order_by("id").filter(id__range=(minParticipantID, maxParticipantID)).filter(livesInLA = 1)
	else:
		return Participant.objects.order_by("id").filter(id__range=(minParticipantID, maxParticipantID))

#FEATURES ARRAYS####################################################################

def answersAsFeaturesArray(ParticipantCollection, QuestionResponseCollection):
	twoDimensionalFeaturesList = []
	for participant in ParticipantCollection:
		featuresList.append([qr.answer for qr in QuestionResponseCollection.filter(participant__id = participant.id)])
	return numpy.array(twoDimensionalFeaturesList)

#TARGET ARRAYS########################################################################

def livesInLAAsTargetArray(ParticipantCollection):
	return numpy.array([p.livesInLA for p in ParticipantCollection.order_by("id")])

#ANSWERS##############################################################################

def answersFromParticipant(pid, QuestionResponseCollection):
	return numpy.array([qr.answer for qr in QuestionResponseCollection.order_by("participant__id").filter(participant__id = pid)]) 

def answersForQuestion(qid, QuestionResponseCollection):
	return [qr.answer for qr in QuestionResponseCollection.order_by("participant__id").filter(question__id = qid)]

def mostCommonAnswerForQuestion(qid, QuestionResponseCollection):
	answer0Count = len(list(filter(lambda a : a==0, answersForQuestion(qid, QuestionResponseCollection))))
	return 1 if (answer0Count < len(answersForQuestion(qid,QuestionResponseCollection))/2) else 0 

def answerForUserForQuestion(pid, qid, QuestionResponseCollection):
	return QuestionResponseCollection.filter(participant__id = pid).filter(question__id = qid)[0].answer

#RATINGS###############################################################################

def ratingsForQuestion(qid, QuestionResponseCollection):
	qrList = QuestionResponseCollection.order_by("participant__id").filter(question__id = qid)
	return numpy.array([qr.rating for qr in qrList])

def ratingAvgForQuestion(qid, QuestionResponseCollection):
	ratingsArray = ratingsForQuestion(qid, QuestionResponseCollection)
	return functools.reduce(lambda x,y : x+y, ratingsArray, 0)/len(ratingsArray)

def sumOfAvgRatings(QuestionResponseCollection):
	return functools.reduce(lambda x,y : x+y, [ratingAvgForQuestion(x, QuestionResponseCollection) for x in range(1, 21)])

#PARTICIPANTS##########################################################################

def participantCountFromLAInRange(ParticipantCollection):
	return ParticipantCollection.order_by("id").filter(livesInLA = 1).count()

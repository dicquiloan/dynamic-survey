from ..models import *
import numpy

def tester():
	print("Hello RBM tester")

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

def getQuestionResponseAnswersAsFeaturesArray():
        featuresList = []
        for participant in Participant.objects.all():
                featuresList.append([qr.answer for qr in QuestionResponse.objects.filter(participant__id = participant.id)])
        return numpy.array(featuresList)

def getLivesInLAAsTargetArray():
        return numpy.array([p.livesInLA for p in Participant.objects.all()])

def getQuestionResponseAnswersFromParticipant(pid):
        return numpy.array(qr.answer for qr in QuestionResponse.objects.filter(participant__id = pid))

def getQuestionResponseAnswersAsFeaturesArray_snake():
	featuresList = []
	for participant in Participant.objects.all():
		featuresList.append([qr.answer for qr in QuestionResponse.objects.filter(participant__id = participant.id)])
	return numpy.array(featuresList)

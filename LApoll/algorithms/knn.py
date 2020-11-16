from ..models import *


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

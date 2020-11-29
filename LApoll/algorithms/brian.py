from  ..models import *
import functools
import numpy
from . import utilsClass


def ratingWeightForQuestion(qid, trainingQRCollection):
	avgRatingForThisQuestion = utilsClass.ratingAvgForQuestion(qid, trainingQRCollection)
	#this line is causing all the lag
	sumOfAvgRatingsOfAllQuestions = utilsClass.sumOfAvgRatings(trainingQRCollection)
	return avgRatingForThisQuestion / sumOfAvgRatingsOfAllQuestions

'''
#avgRating for this question / sum of avg ratings for all questions
def ratingWeightForQuestion(qid, minTrainingID, maxTrainingID):
	avgRatingForThisQuestion = utils.ratingAvgForQuestion(qid, minTrainingID, maxTrainingID)
	#this line is causing all the lag
	sumOfAvgRatingsOfAllQuestions = utils.sumOfAvgRatings(minTrainingID, maxTrainingID)
	return avgRatingForThisQuestion / sumOfAvgRatingsOfAllQuestions
'''


def adjustedValueForUserForQuestion(pid, qid, trainingQRCollection, testingQRCollection):
	userAnswer = utilsClass.answerForUserForQuestion(pid, qid, testingQRCollection)
	mostCommonAnswer = utilsClass.mostCommonAnswerForQuestion(qid, trainingQRCollection)
	if(userAnswer == mostCommonAnswer):
		return 1
	else:
	 	return -1
'''
#1 if user answered the same as most common answer for this question, -1 if they didn't  
def adjustedValueForUserForQuestion(pid, qid, minTrainingID, maxTrainingID):
	userAnswer = utils.answerForUserForQuestion(pid, qid)
	mostCommonAnswer = utils.mostCommonAnswerForQuestion(qid, minTrainingID, maxTrainingID)
	if(userAnswer == mostCommonAnswer):
		return 1
	else:
	 	return -1
'''

def probabilityLivesInLA(pid, trainingQRCollection, testingQRCollection):
	total = 0.0
	for qid in range (1, 21):
		weight = ratingWeightForQuestion(qid, trainingQRCollection) 
		value = adjustedValueForUserForQuestion(pid, qid, trainingQRCollection, testingQRCollection)
		total = total + weight * value
	return total
'''
def probabilityLivesInLA(pid, minTrainingID, maxTrainingID):
	total = 0.0
	for qid in range (1, 21):
		weight = ratingWeightForQuestion(qid, minTrainingID, maxTrainingID) 
		value = adjustedValueForUserForQuestion(pid, qid, minTrainingID, maxTrainingID)
		total = total + weight * value
	return total
'''

def guessedCorrectly(trainingQRCollection, testingQRCollection, participantCollection, cutoffProbability):
	total = 0
	livesInLAList = utilsClass.livesInLAAsTargetArray(participantCollection)
	probabilityList = [probabilityLivesInLA(x.id, trainingQRCollection, testingQRCollection) for x in participantCollection]
	livesInLAPredictionList = [(1 if x >= cutoffProbability else 0) for x in probabilityList]
	for i in range(0, len(livesInLAList)):
		if livesInLAList[i] == livesInLAPredictionList[i]:
			total = total + 1 
	return total

'''
#guessedCorrectly(minTrainingID, maxTrainingID, minTestingID, maxTestingID, cutoffProbability)
#ORDER MATTERS. make sure predictions are synched with true list
def guessedCorrectly(minTrainingID, maxTrainingID, minTestingID, maxTestingID, cutoffProbability):
	total = 0
	livesInLAList = utils.livesInLAAsTargetArray(minTestingID, maxTestingID)
	probabilityList = [probabilityLivesInLA(x, minTrainingID, maxTrainingID) for x in range(minTestingID, maxTestingID+1)]
	livesInLAPredictionList = [(1 if x >= cutoffProbability else 0) for x in probabilityList]
	for i in range(0, len(livesInLAList)):
		if livesInLAList[i] == livesInLAPredictionList[i]:
			total = total + 1 
	return total
'''


	 

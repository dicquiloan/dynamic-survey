from  ..models import *
import functools
import numpy
from . import utilsClass


class BrianModel: 
	def __init__(self, trainingQRCollection, testingQRCollection, participantCollection):
		self.trainingQRCollection = trainingQRCollection
		self.testingQRCollection = testingQRCollection
		self.participantCollection = participantCollection
		#store weights at instantiation to reduce repeated calculations
		self.avgQuestionRatings = [utilsClass.ratingAvgForQuestion(x, trainingQRCollection) for x in range(1,21)]
		self.sumOfAvgQuestionRatings = utilsClass.sumOfAvgRatings(trainingQRCollection)

	def ratingWeightForQuestion(self, qid):
		#this line is causing all the lag
		return self.avgQuestionRatings[qid-1] / self.sumOfAvgQuestionRatings


	def adjustedValueForUserForQuestion(self, pid, qid):
		userAnswer = utilsClass.answerForUserForQuestion(pid, qid, self.testingQRCollection)
		mostCommonAnswer = utilsClass.mostCommonAnswerForQuestion(qid, self.trainingQRCollection)
		if(userAnswer == mostCommonAnswer):
			return 1
		else:
			return -1

	def probabilityLivesInLA(self, pid):
		total = 0.0
		for qid in range (1, 21):
			#store weights at instantiation to reduce repeated calculations
			weight = self.ratingWeightForQuestion(qid)
			value = self.adjustedValueForUserForQuestion(pid, qid)
			total = total + weight * value
		return total

	def guessedCorrectly(self, cutoffProbability):
		total = 0
		livesInLAList = utilsClass.livesInLAAsTargetArray(self.testingQRCollection)
		probabilityList = [self.probabilityLivesInLA(x.id) for x in self.participantCollection]
		livesInLAPredictionList = [(1 if x >= cutoffProbability else 0) for x in probabilityList]
		for i in range(0, len(livesInLAList)):
			if livesInLAList[i] == livesInLAPredictionList[i]:
				total = total + 1 
		return total

		 

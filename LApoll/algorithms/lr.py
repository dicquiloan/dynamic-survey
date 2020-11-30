from sklearn.linear_model import LogisticRegression
import functools
from . import utilsClass


def generateLRModel(trainingQRCollection):
	X = utilsClass.answersAsFeaturesArray(trainingQRCollection)
	y = utilsClass.livesInLAAsTargetArray(trainingQRCollection)
	return LogisticRegression(random_state=0).fit(X,y)




def generateLRCategorizationProbability(trainingQRCollection, testingQRCollection, participantCollection, participantID):
	lrModel = generateLRModel(trainingQRCollection)
	return lrModel.predict_proba([utilsClass.answersFromParticipant(participantID, testingQRCollection)])[0][1]

def guessedCorrectly(trainingQRCollection, testingQRCollection, participantCollection):
	lrModel = generateLRModel(trainingQRCollection)
	livesInLAPredictionsList = lrModel.predict(utilsClass.answersAsFeaturesArray(testingQRCollection))
	livesInLAList = utilsClass.livesInLAAsTargetArray(testingQRCollection)
	total = 0
	for i in range(0, len(livesInLAList)):
		if livesInLAPredictionsList[i] == livesInLAList[i]:
			total = total + 1
	return total


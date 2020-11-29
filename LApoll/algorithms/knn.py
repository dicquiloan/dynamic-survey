from sklearn.neighbors import KNeighborsClassifier
import functools
from . import utilsClass


def generateKNNModel(participantCollection, trainingQRCollection):
	X = utilsClass.answersAsFeaturesArray(participantCollection, trainingQRCollection)
	y = utilsClass.livesInLAAsTargetArray(participantCollection)
	#k is 5 by default
	knnClassifier = KNeighborsClassifier()
	knnClassifier.fit(X, y)

	return knnClassifier


'''
def generateKNNModel(minParticipantID, maxParticipantID):
	X = utils.answersAsFeaturesArray(minParticipantID, maxParticipantID)
	y = utils.livesInLAAsTargetArray(minParticipantID, maxParticipantID)
	#k is 5 by default
	knnClassifier = KNeighborsClassifier()
	knnClassifier.fit(X, y)

	return knnClassifier

'''

def generateKNNCategorizationProbability(trainingQRCollection, testingQRCollection, participantCollection, participantID):
	knnModel = generateKNNModel(participantCollection, trainingQRCollection)
	return knnModel.predict_proba([utilsClass.answersFromParticipant(participantID, testingQRCollection)])[0][1]
'''
def generateKNNCategorizationProbability(minTrainingID, maxTrainingID, participantID):
	knnModel = generateKNNModel(minTrainingID, maxTrainingID)
	return knnModel.predict_proba([answersFromParticipant(participantID)])[0][1]
'''

def guessedCorrectly(trainingQRCollection, testingQRCollection, participantCollection):
	knnModel = generateKNNModel(participantCollection, trainingQRCollection)
	livesInLAPredictionsList = knnModel.predict(utilsClass.answersAsFeaturesArray(participantCollection, testingQRCollection))
	livesInLAList = utilsClass.livesInLAAsTargetArray(participantCollection)
	total = 0
	for i in range(0, len(livesInLAList)):
		if livesInLAPredictionsList[i] == livesInLAList[i]:
			total = total + 1
	return total


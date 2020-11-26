from sklearn.neighbors import KNeighborsClassifier
import functools
from . import utils 


def generateKNNModel(minParticipantID, maxParticipantID):
	X = utils.answersAsFeaturesArray(minParticipantID, maxParticipantID)
	y = utils.livesInLAAsTargetArray(minParticipantID, maxParticipantID)
	#k is 5 by default
	knnClassifier = KNeighborsClassifier()
	knnClassifier.fit(X, y)

	return knnClassifier


def generateKNNCategorizationProbability(minTrainingID, maxTrainingID, participantID):
	knnModel = generateKNNModel(minTrainingID, maxTrainingID)
	return knnModel.predict_proba([answersFromParticipant(participantID)])[0][1]


def guessedCorrectly(minTrainingID, maxTrainingID, minTestingID, maxTestingID):
	knnModel = generateKNNModel(minTrainingID, maxTrainingID)
	livesInLAPredictionsList = knnModel.predict(utils.answersAsFeaturesArray(minTestingID, maxTestingID))
	livesInLAList = utils.livesInLAAsTargetArray(minTestingID, maxTestingID)
	total = 0
	for i in range(0, len(livesInLAList)):
		if livesInLAPredictionsList[i] == livesInLAList[i]:
			total = total + 1
	return total


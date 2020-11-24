from sklearn.neighbors import KNeighborsClassifier
from .utils import *

def generateKNNModel(minParticipantID, maxParticipantID):
	X = answersAsFeaturesArray(minParticipantID, maxParticipantID)
	y = livesInLAAsTargetArray(minParticipantID, maxParticipantID)
	#k is 5 by default
	knnClassifier = KNeighborsClassifier()
	knnClassifier.fit(X, y)

	return knnClassifier


def generateKNNCategorizationProbability(minParticipantID, maxParticipantID, participantID):
	knnModel = generateKNNModel(minParticipantID, maxParticipantID)
	return knnModel.predict_proba([answersFromParticipant(participantID)])[0][1]



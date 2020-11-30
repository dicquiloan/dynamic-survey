from sklearn.svm import SVC
from . import utilsClass 




def generateSVMModel(trainingQRCollection):
	X = utilsClass.answersAsFeaturesArray(trainingQRCollection)
	y = utilsClass.livesInLAAsTargetArray(trainingQRCollection)
	svmClassifier = SVC(gamma='auto', probability = True).fit(X, y)

	return svmClassifier


def generateSVMCategorizationProbability(trainingQRCollection, testingQRCollection, participantCollection, participantID):
        svmModel = generateSVMModel(trainingQRCollection)
        return svmModel.predict_proba([utilsClass.answersFromParticipant(participantID, testingQRCollection)])[0][1]

def guessedCorrectly(trainingQRCollection, testingQRCollection, participantCollection):
        svmModel = generateSVMModel(trainingQRCollection)
        livesInLAPrediction = svmModel.predict(utilsClass.answersAsFeaturesArray(testingQRCollection))
        livesInLA = utilsClass.livesInLAAsTargetArray(testingQRCollection)
        total = 0 
        for i in range(0, len(livesInLA)):
                if livesInLAPrediction[i] == livesInLA[i]:
                        total = total + 1 
        return total

'''
def guessedCorrectly(minTrainingID, maxTrainingID, minTestingID, maxTestingID):
        svmModel = generateSVMModel(minTrainingID, maxTrainingID)
        livesInLAPrediction = svmModel.predict(utils.answersAsFeaturesArray(minTestingID, maxTestingID))
        livesInLA = utils.livesInLAAsTargetArray(minTestingID, maxTestingID)
        total = 0 
        for i in range(0, len(livesInLA)):
                if livesInLAPrediction[i] == livesInLA[i]:
                        total = total + 1 
        return total
'''

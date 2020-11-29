from sklearn.svm import SVC
from . import utils 


def generateSVMModel(minTrainingID, maxTrainingID):
	X = utils.answersAsFeaturesArray(minTrainingID, maxTrainingID)
	y = utils.livesInLAAsTargetArray(minTrainingID, maxTrainingID)
	svmClassifier = SVC(gamma='auto').fit(X, y)

	return svmClassifier

#no ability to get confidence that a particular guess is correct for this classifier

def guessedCorrectly(minTrainingID, maxTrainingID, minTestingID, maxTestingID):
        svmModel = generateSVMModel(minTrainingID, maxTrainingID)
        livesInLAPrediction = svmModel.predict(utils.answersAsFeaturesArray(minTestingID, maxTestingID))
        livesInLA = utils.livesInLAAsTargetArray(minTestingID, maxTestingID)
        total = 0 
        for i in range(0, len(livesInLA)):
                if livesInLAPrediction[i] == livesInLA[i]:
                        total = total + 1 
        return total


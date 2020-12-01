from . import utilsClass
from sklearn.neural_network import BernoulliRBM
from sklearn.preprocessing import StandardScaler
import numpy

def generateRBMModel(trainingQRCollection):
	trainX = utilsClass.answersAsFeaturesArray(trainingQRCollection)
	zScoreTrainX = StandardScaler().fit_transform(trainX)
	rbm = BernoulliRBM(n_components = 1)
	rbm.fit(zScoreTrainX)
	return rbm 

'''
train = utilsClass.getQuestionResponsesInParticipantRange(41, 80)
test = utilsClass.getQuestionResponsesInParticipantRange(1,40)
participants = utilsClass.getParticipantsInRange(1,40)	

train_X = utilsClass.answersAsFeaturesArray(train)
train_y = utilsClass.livesInLAAsTargetArray(train)

test_X = utilsClass.answersAsFeaturesArray(test)

sTrain_X = StandardScaler().fit_transform(train_X)
sTest_X = StandardScaler().fit_transform(test_X)

rbm = BernoulliRBM(n_components = 1)

rbm.fit(sTrain_X)

crazyArray = numpy.array(rbm.transform(sTest_X).flatten())

crazyPredict = utilsClass.onOffVsMean(crazyArray)
livesInLAList = utilsClass.livesInLAAsTargetArray(test)

utilsClass.displayMatchStats(crazyPredict, livesInLAList)
'''

def guessedCorrectly(trainingQRCollection, testingQRCollection, participantCollection):
	rbm = generateRBMModel(trainingQRCollection)
	livesInLAList = utilsClass.livesInLAAsTargetArray(testingQRCollection)
	testX = utilsClass.answersAsFeaturesArray(testingQRCollection)
	zScoreTestX = StandardScaler().fit_transform(testX)
	crazyArray = numpy.array(rbm.transform(zScoreTestX).flatten())
	crazyClassifierArray = utilsClass.onOffVsMean(crazyArray)
	total = 0
	for i in range(0, len(livesInLAList)):
		if livesInLAList[i] == crazyClassifierArray[i]:
			total = total + 1 
	return total


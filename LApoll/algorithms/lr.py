'''
FOR EACH FUNCTION DEFINED, ADD COMMENT, 

MAKE SURE TO MATCH FUNCTIONAL REQUIREMENTS
'''



'''
NAME:
	NAME
	generateLRModel
PARAMETERS: 
	@param datatype name meaning
	@param int      minId minimum participant database ID to generate model from
RETURNS: 
	@return LogisticRegressionObject sklearn lrmodel object that has been fit already using range 
DESCRIPTION:
	This function uses sk learn's LogisticRegression definitions to generate and 
	fit a logistic regression estimator by generating a features array 
	and target array from the database QuestionResponses in the range given. 

(ifneeded)PSEUDOCODE
'''

def generateLRModel(minID, maxID):
	#X = pull in features array
	#y = pull in target array

	lrModel = LogisticRegression(random_state=0)
	lrModel.fit(X, y)

	return lrModel

'''
def generateLogisticRegressionProbability(minID, maxID, partipantID):
	lrModel = generateLRModel(minID, maxID)

	return asdasda

'''


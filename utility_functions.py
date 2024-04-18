#==============================================================
# Various utility functions for data processing or model set up
#==============================================================

from sklearn.model_selection import train_test_split as tts
from sklearn.model_selection import KFold, GridSearchCV
from config_store import infoMappings, randomSeed, k

# Specialized mapper function to target strings that contain a key rather than being the key
def mapValues(x):
    final = "N/A"
    for key in infoMappings:
        if key in x:
            final = infoMappings.get(key)
            break
    return final

# Perfrom TTS on data set
def dataSetSplit(X, y):
    return tts(X, y, random_state = randomSeed, shuffle = True, test_size = 0.20)

# Report scores for training and testing set for given model
def score(model, XTrain, yTrain, XTest, yTest):
    print("Training score: {}".format(model.score(XTrain, yTrain)))
    print("Testing score: {}".format(model.score(XTest, yTest)))

# Performs k-fold cross validation on a given model for some X, y, k
def doKFold(model, X, y, k = k, scaler = None, randomState = randomSeed):
    kf = KFold(n_splits=k, random_state = randomState, shuffle=True)
    train_scores = []
    test_scores = []

    # Test model on each split
    for idxTrain, idxTest in kf.split(X):
        XTrain = X[idxTrain, :]
        XTest = X[idxTest, :]
        yTrain = y[idxTrain]
        yTest = y[idxTest]

        # Apply scalar if necessary
        if scaler != None:
            XTrain = scaler.fit_transform(XTrain)
            XTest = scaler.transform(XTest)

        # Fit model
        model.fit(XTrain,yTrain)

        # Record scores for fitted model
        train_scores.append(model.score(XTrain,yTrain))
        test_scores.append(model.score(XTest,yTest))
        
    # Return scores for k-fold
    return train_scores, test_scores

# Perform grid search hyperparameter optimization on some given model for some hyperparameter set
def doGridSearch(model, hyperparameters, XTrain, yTrain):
    # Set up k-fold cross validation object
    crossValidation = KFold(n_splits = k, random_state = randomSeed, shuffle = True)

    # Do grid search optimization
    grid = GridSearchCV(model, param_grid = hyperparameters, cv = crossValidation, scoring = "accuracy")
    grid.fit(XTrain, yTrain)

    return grid

import numpy as np
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, StratifiedKFold, LeaveOneOut,LeavePOut,ShuffleSplit,cross_val_score

#K-Fold is spiritually similar to bagging in the sense that you pick both will pick some data from TrainData to validate the model's accuracy
#K-Fold will split dataset in K sets. (K-1) sets will be used for training and the 1 remaining set will be used for Cross Validation.
X, y = datasets.load_iris(return_X_y=True)

print("K-Folds:")
k_Folds = KFold(n_splits=7) #Bruh you cannot use '-' sign in names apparently
classifer = DecisionTreeClassifier(random_state=9999)
scores = cross_val_score(classifer, X, y, cv=k_Folds)
print(f"Cross Validation Scores = {scores}")
print(f"Average Cross Validation Score = {scores.mean()}")
print(f"Number of Cross Validation Scores = {len(scores)}\n\n")


#Stratified 'just be better' kFolds. This will ensure equal proportionality of data distribution in each K-set
print("Stratified K-Folds:")
sk_Folds = StratifiedKFold(n_splits=7) 
classifer = DecisionTreeClassifier(random_state=9999)
scores = cross_val_score(classifer, X, y, cv=sk_Folds)
print(f"Cross Validation Scores = {scores}")
print(f"Average Cross Validation Score = {scores.mean()}")
print(f"Number of Cross Validation Scores = {len(scores)}\n\n")


#LOO -> if I have 100 rows, it will use 99 to train and 1 to validate. So there isn't a fixed K value we select like in kFolds
print("Leave-One-Out:")
LOO = LeaveOneOut()
classifer = DecisionTreeClassifier(random_state=9999)
scores = cross_val_score(classifer, X, y, cv=LOO)
print(f"Cross Validation Scores = {scores}")
print(f"Average Cross Validation Score = {scores.mean()}")
print(f"Number of Cross Validation Scores = {len(scores)}\n\n")


#LPO -> Same as LOO except you could pick how many rows to leave out for validation
print("Leave-P-Out:")
LPO = LeavePOut(p=2) #Damn so if I set p too high like p=5, there will be hundreds of millions of permuations and it will take a while to calculate all those. Crazy
classifer = DecisionTreeClassifier(random_state=9999)
scores = cross_val_score(classifer, X, y, cv=LPO)
print(f"Cross Validation Scores = {scores}")
print(f"Average Cross Validation Score = {scores.mean()}")
print(f"Number of Cross Validation Scores = {len(scores)}\n\n")


#ShuffleSplit
print("Shuffle Split:")
ss = ShuffleSplit(n_splits=7, train_size=0.7, test_size=0.25) 
classifer = DecisionTreeClassifier(random_state=9999)
scores = cross_val_score(classifer, X, y, cv=ss)
print(f"Cross Validation Scores = {scores}")
print(f"Average Cross Validation Score = {scores.mean()}")
print(f"Number of Cross Validation Scores = {len(scores)}\n\n")


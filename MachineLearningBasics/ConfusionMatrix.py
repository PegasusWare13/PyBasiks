import numpy as np
from numpy import random
from sklearn import metrics
import matplotlib.pyplot as plt

#random number to showcase functionality of confusionMatrices
actual_values = random.binomial(size=100, p=0.3, n=1)
predicted_values = random.binomial(size=100, p=0.3, n=1)

confusion_matrix = metrics.confusion_matrix(actual_values, predicted_values)
display_confusionMatrix = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix)
display_confusionMatrix.plot()

#Created Metrics
print("Created Metrics:")
print(f"Accuracy = {metrics.accuracy_score(actual_values,predicted_values)}") #Accuracy = [TruePositive + TrueNegative] / [TotalPredictions]
print(f"Precision = {metrics.precision_score(actual_values,predicted_values)}") #Precision = [TruePositive] / [TruePositives + FalsePositives]
print(f"Sensitivity = {metrics.recall_score(actual_values,predicted_values)}") #Sensitivity = [TruePositives] / [TruePositives + FalseNegatives] 
print(f"Specificity = {metrics.recall_score(actual_values,predicted_values, pos_label=0)}") #Specificity = [TrueNegatives] / [TrueNegatives + FalsePositives] The real antichrist to Sensitivity
print(f"F1 Score = {metrics.f1_score(actual_values,predicted_values)}") #f1_score = Harmonic Mean of the two antichrists Sensitivity and Specificity

plt.show() #this looks like some doctor Strange shit bro
# True Negative (Top-Left Quadrant)
# False Positive (Top-Right Quadrant)
# False Negative (Bottom-Left Quadrant)
# True Positive (Bottom-Right Quadrant)
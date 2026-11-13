import numpy as np
from numpy import random
import scipy; from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = np.array(random.randint(10, size=10))
y = np.array(random.randint(100, size=10))

#Creation of Polynomial Model
coefficients = np.polyfit(x,y,3) #fitted into higher dergeee where degree = 3
model = np.poly1d(coefficients) # www.geeksforgeeks.org/data-analysis/numpys-polyfit-function-a-comprehensive-guide/
print("Polynomial Equation obtained:\n",model)

#Okay, so r2_score is the 'reliability' of the model in my eyes. It compares true values of y to the predicted values of y
print("Reliability score:",r2_score(y,model(x)))
#It is an eligibility criterion.
if r2_score(y,model(x))>0.45:
    choice_x = random.choice(x)
    print(f"Random choice for x = {choice_x}\nPredicted Value of y from our model = {model(choice_x)}")
else: print("Model not reliable enough")

#Final Plotting
plt.scatter(x,y)
line_x = np.linspace(start=1,stop=22,num=1000)
plt.plot(line_x,model(line_x))
plt.show()

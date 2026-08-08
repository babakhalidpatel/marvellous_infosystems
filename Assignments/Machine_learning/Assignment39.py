
# Load the file using pandas, display

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


Border = "-"*40
#Loading file
df = pd.read_csv("student_performance_ml.csv")

# import decisionTreeClassifier from sklearn.tree 
# create a model object and train it using fit

feature_cols = ["StudyHours",
                "Attendance",
                "PreviousScore",
                "AssignmentsCompleted",
                "SleepHours"
                ]

X = df[feature_cols]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.5, random_state=42)


model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

# use the trained model to predict the result for X Test
# display predicted values along with actual values

y_pred = model.predict(X_test)

print("Predicted Values:", y_pred)
print("Actual Values:", Y_test.values)

# calculate the accuracy of the model using accuracy_score from sklearn.metrics
# display the result in percentage format


accuracy = accuracy_score(Y_test, y_pred) * 100
print("Accuracy: {:.2f}%".format(accuracy))

# generate a confusion matrix using sklearn.metrics.confusion_matrix
# display the ConfusionMatrixDisplay

cm = confusion_matrix(Y_test, y_pred)
print("Confusion Matrix:\n", cm)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()

# calculate training accuracy and testing accuracy using model.score() method
train_accuracy = model.score(X_train, Y_train) * 100
test_accuracy = model.score(X_test, Y_test) * 100
print("Training Accuracy: {:.2f}%".format(train_accuracy))
print("Testing Accuracy: {:.2f}%".format(test_accuracy))

# Train three decision tree models with max_depth=1, 3 and none , compare their training and testing accuracy. Display the results in a tabular format.

model1 = DecisionTreeClassifier(max_depth=1)
model2 = DecisionTreeClassifier(max_depth=3)
model3 = DecisionTreeClassifier(max_depth=None)

model1.fit(X_train, Y_train)
model2.fit(X_train, Y_train)
model3.fit(X_train, Y_train)

train_accuracy1 = model1.score(X_train, Y_train) * 100
test_accuracy1 = model1.score(X_test, Y_test) * 100

train_accuracy2 = model2.score(X_train, Y_train) * 100
test_accuracy2 = model2.score(X_test, Y_test) * 100

train_accuracy3 = model3.score(X_train, Y_train) * 100
test_accuracy3 = model3.score(X_test, Y_test) * 100

print("Model Comparison:")
print("Model\t\tTraining Accuracy\tTesting Accuracy")
print("-" * 50)
print("Max Depth = 1\t{:.2f}%\t\t{:.2f}%".format(train_accuracy1, test_accuracy1))
print("Max Depth = 3\t{:.2f}%\t\t{:.2f}%".format(train_accuracy2, test_accuracy2))
print("Max Depth = None\t{:.2f}%\t\t{:.2f}%".format(train_accuracy3, test_accuracy3))

# Use the trained model to predict the result for a new student with the following details:
# StudyHours = 6, Attendance = 85, PreviousScore = 66, AssignmentsCompleted = 7, SleepHours = 7.
#  Display the predicted result.
# will the student pass or fail based on the model's prediction?

new_student = pd.DataFrame({
    "StudyHours": [6],
    "Attendance": [85],
    "PreviousScore": [66],
    "AssignmentsCompleted": [7],
    "SleepHours": [7]
})
prediction = model.predict(new_student)
print("Predicted Result for New Student:", prediction)

if prediction[0] == 1:
    print("The student is predicted to pass.")
else:
    print("The student is predicted to fail.")

# Load the file using pandas, display
# first five records
# last five records
# total number of rows and column
# data types of each column

import pandas as pd
import matplotlib.pyplot as plt


Border = "-"*40
#Loading file
df = pd.read_csv("student_performance_ml.csv")

print(Border)
# first five records
print("first five records")
print(df.head(5))

print(Border)

# last five records
print("last five records")
print(df.tail(5))

print(Border)

# total number of rows and column
print("Total number of rows and columns",df.shape)

print(Border)
# data types of each column
print("Data types are :")
print(df.dtypes)


# Display total number of students in the dataset
print(Border)
print("Total number of sudents in the dataset",len(df))

# how many students passed
print(Border)
print("Total students passed :", df['FinalResult'].sum())


# how many students failed
print(Border)
print("Total students failed :", (df['FinalResult']==0).sum())

# average studyhours
print(Border)
print("Aaverage study hours :", int(df["StudyHours"].sum()/len(df)))

# average attendance
print(Border)
print("Aaverage Attendance :", int(df["Attendance"].sum()/len(df)))

# maximum previous scrore
print(Border)
print("Maximum previous scrore :", df["PreviousScore"].max())

# Minimum Sleep Hours
print(Border)
print("Minimum Sleep Hours :", df["SleepHours"].min())

# Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students. Is the dataset balanced? Justify your answer."
print(Border)

print("Distribution of FinalResult")
print(df["FinalResult"].value_counts())

print("Percentage of pass and fail students")
print(df["FinalResult"].value_counts(normalize=True)*100)
# it is not balanced as its proporation is 60, 40

# Based on the dataset values, analyze whether:
# Higher StudyHours increase the chance of passing.
# Higher Attendance improves FinalResult.
print(Border)

print("Average StudyHours by FinalResult")
print(df.groupby("FinalResult")["StudyHours"].mean())

print(Border)
print("Average Attendance by FinalResult")
print(df.groupby("FinalResult")["Attendance"].mean())

print(Border)
print("Correlation of StudyHours and Attendance with FinalResult")
print(df[["StudyHours","Attendance","FinalResult"]].corr())

# Plot a histogram of studyHours 
# Explain what the distribution channel tell you

print(Border)

plt.hist(df["StudyHours"], bins=8, edgecolor="black")
plt.title("Distribution of StudyHours")
plt.xlabel("StudyHours")
plt.ylabel("Number of Students")
plt.show()
print(Border)

# create a scatter plot of study hours vs previous score
plt.figure(figsize=(8,5))

# Plot Fail students (FinalResult = 0)
plt.scatter(df[df["FinalResult"]==0]["StudyHours"],
            df[df["FinalResult"]==0]["PreviousScore"],
            color="red", label="Fail", edgecolor="black")

# Plot Pass students (FinalResult = 1)
plt.scatter(df[df["FinalResult"]==1]["StudyHours"],
            df[df["FinalResult"]==1]["PreviousScore"],
            color="green", label="Pass", edgecolor="black")

plt.title("StudyHours vs PreviousScore (Pass vs Fail)")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.legend()
plt.show()

print(Border)

# draw a boxplot of attendance . identify any outliers in the dataset
plt.figure(figsize=(6,5))
plt.boxplot(df["Attendance"], vert=True, patch_artist=True,
            boxprops=dict(facecolor="lightblue"))
plt.title("Boxplot of Attendance")
plt.ylabel("Attendance")
plt.show()

print(Border)

# identify any outliers in the dataset
Q1 = df["Attendance"].quantile(0.25)
Q3 = df["Attendance"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR

outliers = df[(df["Attendance"] < lower_bound) | (df["Attendance"] > upper_bound)]
print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)
print("Outliers:")
print(outliers)

print(Border)

# Create a plot showing relationship between AssignmentsCompleted and FinalResult. Explain your observation.
plt.figure(figsize=(6,5))
plt.scatter(df["AssignmentsCompleted"], df["FinalResult"], color="purple", edgecolor="black")
plt.title("AssignmentsCompleted vs FinalResult")
plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult (0=Fail, 1=Pass)")
plt.yticks([0,1])
plt.show()

# Alternative: boxplot comparison
plt.figure(figsize=(6,5))
df.boxplot(column="AssignmentsCompleted", by="FinalResult", patch_artist=True)
plt.title("AssignmentsCompleted by FinalResult")
plt.suptitle("")
plt.xlabel("FinalResult")
plt.ylabel("AssignmentsCompleted")
plt.show()

# Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain."
plt.figure(figsize=(6,5))
plt.scatter(df["SleepHours"], df["FinalResult"], color="orange", edgecolor="black")
plt.title("SleepHours vs FinalResult")
plt.xlabel("SleepHours")
plt.ylabel("FinalResult (0=Fail, 1=Pass)")
plt.yticks([0,1])
plt.show()

# Compare average sleep hours for pass vs fail
print(df.groupby("FinalResult")["SleepHours"].mean())
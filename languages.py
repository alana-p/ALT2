import csv
import pandas
import statistics
import matplotlib.pyplot as plt

# Read the entire CSV file into a pandas DataFrame
# Calculate the Mean of each separate column by referring to the Column Heading
df = pandas.read_csv('languages.csv')
print(df.to_string())
# Filter out the column, value_eur
numoflanguagesspoken_values = df['NUM OF LANGUAGES SPOKEN']
mean_value_numlanguagesspoken= round(statistics.mean(numoflanguagesspoken_values), 2)
print("Mean Value Number of Languages Spoken:", mean_value_numlanguagesspoken)

numoflangfluent_values = df['NUM OF LANGUAGES SPOKEN FLUENTLY']
mean_value_lang_fluent = round(statistics.mean(numoflangfluent_values), 2)
print("Mean Value Number of Languages Spoken Fluently", mean_value_lang_fluent)

age_values = df['AGES OF PEOPLE BEING SURVEYED']
mean_age_values = round(statistics.mean(age_values), 2)
print("Mean Age of People Surveyed", mean_age_values)

numlanguages = [1,2]
# take in data from the screen

numlanguages[0] = input("Enter the mean of  ")
languages[1] = input("enter a second symptom ")
numlanguages[1] = input("enter how many students had the second symptom ")

# Data to plot
labels = symptoms[0], symptoms[1]
sizes = [students[0], students[1]]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.1, 0.1, 0.1)  # explode 1st slice
# Plot the Pie Chart (Do not change any code below)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
#plt.axis('equal')
plt.show()

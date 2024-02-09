import csv
import pandas
#import statistics

with open('languages.csv', 'r') as filename:
    csv_reader = csv.reader(filename)
    for row in csv_reader:
        print(row)
filename.close()
print("closed")

# Read the entire CSV file into a pandas DataFrame
# Calculate the Mean of each separate column by referring to the Column Heading
df = pandas.read_csv('languages.csv')
print(df.to_string())
# Filter out the column, value_eur
numoflanguagesspoken_values = df['Num of Languages Spoken']
mean_value_numlangspoke= round(statistics.mean(numoflanguagesspoken_values), 2)
print("Mean Value Number of Languages Spoken:", mean_value_numlangspoke)
#numoflnaguages_values = df['Noise']
#mean_value_noise = round(statistics.mean(noise_values), 2)
#print("Mean Value Noise:", mean_value_noise)
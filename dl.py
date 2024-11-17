
# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
# %matplotlib inline
import plotly.express as px

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/simulated_health_dataset.csv')
df.sample(20)

df.drop('ID', axis='columns', inplace=True)

df.dtypes

df.shape

df.isnull

df.Gender.isnull()

df[pd.isnull(df['Occupation'])]

unique_values = df['Occupation'].unique()
unique_values

#Occupation Distribution
unemployed_df=df[df.Occupation=='Unemployed'].Occupation.count()
White_df=df[df.Occupation=='White-collar'].Occupation.count()
Blue_df=df[df.Occupation=='Blue-collar'].Occupation.count()
Student_df=df[df.Occupation=='Student'].Occupation.count()

import matplotlib.pyplot as plt

categories = ['Unemployed', 'White-collar', 'Blue-collar', 'Student']
counts = [unemployed_df, White_df, Blue_df, Student_df]
plt.figure(figsize=(8, 5))
plt.bar(categories, counts, color=['skyblue','red','black','green'])
plt.xlabel('Categories')
plt.ylabel('Count')
plt.title('Bar Plot for Category Counts')
plt.show()

# Renaming specific columns
df = df.rename(columns={'Quality of Sleep': 'quality_sleep', 'Sleep Duration': 'sleep_duration','Physical Activity Level':'activity_level','Stress Level':'stress_level','BMI Category':'BMI','Blood Pressure':'BP','Heart Rate':'Heart_rate','Daily Steps':'Steps','Sleep Disorder':'Sleep_disorder'})
print(df)

poor_df=df[df.quality_sleep=='Poor'].quality_sleep.count()
Moderate_df=df[df.quality_sleep=='Moderate'].quality_sleep.count()
Good_df=df[df.quality_sleep=='Good'].quality_sleep.count()

import matplotlib.pyplot as plt

categories = ['Poor', 'Moderate', 'Good']
counts = [poor_df, Moderate_df, Good_df]
# Pie chart
plt.figure(figsize=(6, 6))
plt.pie(counts, labels=categories, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue', 'yellowgreen', 'lightpink'])
plt.title('Pie Chart for Sleep Distribution')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Box Plot
plt.figure(figsize=(8, 5))
sns.boxplot(x='stress_level', y='sleep_duration', data=df)
plt.xlabel('Stress Level')
plt.ylabel('Sleep Duration (hours)')
plt.title('Box Plot: Sleep Duration vs Stress Level')
plt.show()

# Violin Plot
plt.figure(figsize=(8, 5))
sns.violinplot(x='stress_level', y='sleep_duration', data=df)
plt.xlabel('Stress Level')
plt.ylabel('Sleep Duration (hours)')
plt.title('Violin Plot: Sleep Duration vs Stress Level')
plt.show()

# Count Plot (discretize sleep duration for better categorization)
df['Sleep_Category'] = pd.cut(df['sleep_duration'], bins=[0, 4, 5, 6, 7, 8, 10], labels=['<4', '4-5', '5-6', '6-7', '7-8', '8+'])

plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Sleep_Category', hue='stress_level')
plt.xlabel('Sleep Duration Category (hours)')
plt.ylabel('Count')
plt.title('Count Plot: Sleep Duration vs Stress Level')
plt.legend(title='Stress Level')
plt.show()

for column in df.columns:
    if df[column].dtype == 'object':
      print(f"Column '{column}':")
      print(df[column].unique())
      print



#df['Gender'] = df['Gender'].replace({'Male': 1, 'Female': 0})

#df['Occupation'] = df['Occupation'].replace({'Unemployed': 0, 'White-collar': 1, 'Blue-collar': 2, 'Student': 3})

#df['quality_sleep'] = df['quality_sleep'].replace({'Poor': 0, 'Moderate': 1, 'Good': 2})

#df['activity_level'] = df['activity_level'].replace({'Low': 0, 'Moderate': 1, 'High': 2})

#df['stress_level'] = df['stress_level'].replace({'Low': 0, 'Moderate': 1, 'High': 2})

#df['BMI'] = df['BMI'].replace({'Underweight': 0, 'Normal': 1, 'Overweight': 2, 'Obese': 3})

# df['Sleep_disorder'] = df['Sleep_disorder'].replace({'None': 0, 'Insomnia': 1, 'Sleep Apnea': 2, 'Deep Sleep Apnea': 3})

# for column in df.columns:
#     print(f"Column '{column}':")
#     print(df[column].unique())
#     print


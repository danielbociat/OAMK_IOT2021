import pandas as pd

adults = pd.read_csv('adult.data.csv')

"""
Solution obtained 10/10 in the Assignment 1 from Kaggle
"""

"""
1. How many men and women (sex feature) are represented in this dataset?
"""

print(adults["sex"].value_counts())

"""
2. What is the average age (age feature) of women?
"""

females = adults.loc[adults['sex'] == "Female"]
print(females["age"].mean())

"""
3. What is the percentage of German citizens (native-country feature)?
"""

german_citizens = adults.loc[adults["native-country"] == "Germany"]
print(german_citizens.shape[0] / adults.shape[0] * 100)

"""
4-5. What are the mean and standard deviation of age for those who earn more than 50K per year (salary feature) and 
those who earn less than 50K per year?
"""

more_than_50k = adults.loc[adults["salary"] == ">50K"]
less_than_50k = adults.loc[adults["salary"] == "<=50K"]

print("More than 50K age mean", more_than_50k["age"].mean())
print("More than 50K age standard deviation", more_than_50k["age"].std())
print("Less than 50K age mean", less_than_50k["age"].mean())
print("Less than 50K age standard deviation", less_than_50k["age"].std())

"""
6. Is it true that people who earn more than 50K have at least high school education? (education – Bachelors, 
Prof-school, Assoc-acdm, Assoc-voc, Masters or Doctorate feature)
"""

MT50KHE = more_than_50k.loc[more_than_50k["education"].isin(["Bachelors", "Prof-school", "Assoc-acdm", "Assoc-voc",
                                                             "Masters", "Doctorate"])]

# If we compare the shapes we can check if they contain the same data
print(MT50KHE.shape == more_than_50k.shape)

"""
7. Display age statistics for each race (race feature) and each gender (sex feature). Use groupby() and describe().
Find the maximum age of men of Amer-Indian-Eskimo race.
"""

print(adults.groupby(["race", "sex"])[["race", "sex", "age"]].describe())

"""
8. Among whom is the proportion of those who earn a lot (>50K) greater: married or single men (marital-status feature)?
 Consider as married those who have a marital-status starting with Married (Married-civ-spouse, Married-spouse-absent 
 or Married-AF-spouse), the rest are considered bachelors.
"""

MT50K_married = more_than_50k.loc[more_than_50k["marital-status"].isin(["Married-civ-spouse", "Married-spouse-absent",
                                                                        "Married-AF-spouse"])]

num_married = MT50K_married.shape[0]
num_single = more_than_50k.shape[0] - MT50K_married.shape[0]

print("Married: ", num_married)
print("Single: ", num_single)

"""
9. What is the maximum number of hours a person works per week (hours-per-week feature)? How many people work such a
 number of hours, and what is the percentage of those who earn a lot (>50K) among them?
"""
max_hours = adults['hours-per-week'].max()
total_people_max_hours = adults.loc[adults['hours-per-week'] == 99].shape[0]
total_people_max_hours_50K = adults.loc[(adults['hours-per-week'] == 99) & (adults['salary'] == ">50K")].shape[0]
print(max_hours)
print(total_people_max_hours)
print(total_people_max_hours_50K)
print(total_people_max_hours_50K / total_people_max_hours * 100)

"""
Count the average time of work (hours-per-week) for those who earn a little and a lot (salary) for each 
country (native-country). What will these be for Japan?
"""

print("People who earn less money by country")
print(less_than_50k.groupby('native-country')['hours-per-week'].mean())
print("People who earn more money by country")
print(more_than_50k.groupby('native-country')['hours-per-week'].mean())

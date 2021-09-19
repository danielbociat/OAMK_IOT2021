import pandas as pd

cars = pd.read_csv('Automobile_data.csv')


"""
1. From given data set print first and last five rows
"""


cars_first_5 = cars.head(5)
cars_last_5 = cars.tail(5)

print(cars_first_5)
print(cars_last_5)


"""
2. Find the most expensive car company name
"""


print(cars.iloc[cars['price'].argmax()]['company'])


"""
3. Print All Toyota Cars details
"""


print(cars.loc[cars['company'] == "toyota"])


"""
4. Count total cars per company
"""


print(cars['company'].value_counts())


"""
5. Find each company’s highest priced car
"""


print(cars.groupby('company')['price'].max())


"""
6. Find the average mileage of each car making company
"""

print(cars.groupby('company')['average-mileage'].mean())


"""
7. Sort all cars by Price column
"""

sorted_cars = cars.sort_values(by=['price'], ascending="False")
print(sorted_cars.head(5))
print(sorted_cars.tail(5))

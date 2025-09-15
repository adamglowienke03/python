import pandas
import csv

with open("./Weather/weather_data.csv") as data_file:
    # data = data_file.readlines()
    # print(data)
    data = csv.reader(data_file)
    print(data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
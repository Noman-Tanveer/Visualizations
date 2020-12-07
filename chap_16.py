# Visualizations from the downloaded data

import csv

file_name = 'sitka_weather_07-2014.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    highs = []
    for row in reader:
        high = (int(row[1]))
        highs.append(high)
    # print(highs)

from matplotlib import pyplot as plt

plt.plot(highs, c='red')
plt.title("High temp for days")
plt.xlabel('', fontsize=16)
plt.ylabel('Temp (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
plt.savefig('high_month.png')

from datetime import datetime

first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
# print(first_date)

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs = [], []
    for row in reader:
        high = (int(row[1]))
        highs.append(high)
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
plt.savefig("Highs_with_dates.jpg")

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        high = (int(row[1]))
        highs.append(high)
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        low = (int(row[3]))
        lows.append(low)

    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('Dates')
    plt.ylabel('Temp (F)')
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

    plt.savefig('High_and_low_shaded.jpg')

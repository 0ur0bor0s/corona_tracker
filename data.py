import os
import csv
from pathlib import Path
import itertools
import datetime

import matplotlib.pyplot as plt
plt.clf()
plt.cla()
plt.close()

import matplotlib.dates as dt


def parse_and_graph_data():
    script_dir = Path(os.path.dirname(__file__))
    # old dataset
    #confirm_path = os.path.join(script_dir, 'csv/time_series_2019-ncov-Confirmed.csv')
    #death_path = os.path.join(script_dir, 'csv/time_series_2019-ncov-Deaths.csv')
    #recov_path = os.path.join(script_dir, 'csv/time_series_2019-ncov-recovered.csv')

    # new dataset
    confirm_path = os.path.join(script_dir, 'csv/time_series_covid19_confirmed_global.csv')
    death_path = os.path.join(script_dir, 'csv/time_series_covid19_deaths_global.csv')
    recov_path = os.path.join(script_dir, 'csv/time_series_covid19_recovered_global.csv')    
    csv_paths = [confirm_path, death_path, recov_path]


    # [confirmed, deaths, recoveries]
    china_data = [[],[],[]]
    italy_data = [[],[],[]]
    germany_data = [[],[],[]]
    iran_data = [[],[],[]]
    us_data = [[],[],[]]

    dates = []

    """
    Parse Data
    """

    i = 0
    for path in csv_paths:
        with open(path) as file:
            reader = csv.reader(file, delimiter=',')

            # get list of dates in first iteration
            if i == 0:
                header = next(reader)
                for date in itertools.islice(header, 4, None):
                    dates.append(date)

            # confirm_case_arr = [row for idx, row in enumerate(reader) if idx in ()]
            for row in reader:
                if row[1] == 'China':
                    # initially populate cell
                    if len(china_data[i]) == 0:
                        for cell in itertools.islice(row, 4, None):
                            china_data[i].append(int(cell))
                    else:
                        # add new row to current cases
                        for j in range(4, len(row)-4):
                            china_data[i][j] += int(row[j])
                elif row[1] == 'Italy':
                    for cell in itertools.islice(row, 4, None):
                        italy_data[i].append(int(cell))
                elif row[1] == 'Germany':
                    for cell in itertools.islice(row, 4, None):
                        germany_data[i].append(int(cell))
                elif row[1] == 'Iran':
                    for cell in itertools.islice(row, 4, None):
                        iran_data[i].append(int(cell))
                elif row[1] == 'US':
                    # initially populate cell
                    if len(us_data[i]) == 0:
                        for cell in itertools.islice(row, 4, None):
                            us_data[i].append(int(cell))
                    else:
                        # add new row to current cases
                        for j in range(4, len(row)-4):
                            us_data[i][j] += int(row[j])
        
        # update index
        i += 1

    """
     Graph Data
    """
    # convert dates to Python datetime objects
    converted_dates = [datetime.datetime.strptime(d,"%m/%d/%y").date() for d in dates]

    # Graph confirmed cases over time
    plt.plot(converted_dates, china_data[0])
    plt.plot(converted_dates, italy_data[0])
    plt.plot(converted_dates, germany_data[0])
    plt.plot(converted_dates, iran_data[0])
    plt.plot(converted_dates, us_data[0])
    plt.legend(['China', 'Italy', 'Germany', 'Iran', 'USA'], loc='upper left')

    plt.xlabel('time')
    plt.ylabel('confirmed cases')
    plt.title('confirmed cases vs time')
    plt.figure()

    # Graph confirmed deaths over time
    plt.plot(converted_dates, china_data[1])
    plt.plot(converted_dates, italy_data[1])
    plt.plot(converted_dates, germany_data[1])
    plt.plot(converted_dates, iran_data[1])
    plt.plot(converted_dates, us_data[1])
    plt.legend(['China', 'Italy', 'Germany', 'Iran', 'USA'], loc='upper left')

    plt.xlabel('time')
    plt.ylabel('deaths')
    plt.title('deaths vs time')
    plt.figure()

    # Graph recovered over time
    plt.plot(converted_dates, china_data[2])
    plt.plot(converted_dates, italy_data[2])
    plt.plot(converted_dates, germany_data[2])
    plt.plot(converted_dates, iran_data[2])
    plt.plot(converted_dates, us_data[2])
    plt.legend(['China', 'Italy', 'Germany', 'Iran', 'USA'], loc='upper left')

    plt.xlabel('time')
    plt.ylabel('recovered')
    plt.title('recovered vs time')

    plt.show()
    plt.clf()
    plt.cla()
    plt.close()   



        

                
        
        
        


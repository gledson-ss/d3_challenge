import csv
import pandas as pd
import numpy as np


def create_table():
    keywords = [
        'iso_code',
        'date',
        'new_cases',
    ]

    size_keywords = len(keywords)
    dict_keywords = {}
    country_index_array = []

    for i in keywords:
        dict_keywords[i] = []

    with open('data_analyse/data/owid-covid-data.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0

        line_used = [[] for i in range(size_keywords)]
        index_line = []
        for line in csv_reader:
            count += 1

            if count == 1:
                # print(line)
                for j in range(size_keywords):
                    index_line.append(line.index(keywords[j]))
            else:
                for k in range(size_keywords):
                    dict_keywords[keywords[k]].append(line[index_line[k]])
            # break for testing only

    return pd.DataFrame(dict_keywords)


def world_cases_sum(days, index_arr_country, Table):
    # soma de casos de covid em todos os paises por um intervalo de dias

    arr = []

    for i in range(1, days + 1):
        sum = 0
        for index in index_arr_country:
            number = Table['new_cases'][index - i]

            if(len(number) > 0):
                sum += int(float(number))

        arr.append(sum)

    return arr


def log_cases(arr):
    # aplicando log transformação para o uso da formula de regressao linear para a soma de casos de covid
    return np.log(arr)


def predict(days=4):
    Table = create_table()

    index_arr_country = []
    index_country = 0
    country_list = Table['iso_code']
    country_currently = Table['iso_code'][0]
    for country in country_list:
        if country != country_currently:
            index_arr_country.append(index_country)
            country_currently = country
        index_country += 1

    world_cases_sum_per_country = log_cases(world_cases_sum(
        days, index_arr_country, Table))

    print(world_cases_sum_per_country)


predict()

import unittest
import csv
import pandas as pd
import numpy as np
import statsmodels.api as sm
import math


class Predict:
    def create_table(self):
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

    def world_cases_sum(self, days, index_arr_country, Table):
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

    def log_cases(self, arr):
        # aplicando log transformação para o uso da formula de regressao linear para a soma de casos de covid
        return np.log(arr)

    def statmodels_linear_regression(self, days, arr_cases):
        x = np.arange(days)
        x = sm.add_constant(x)

        y = arr_cases

        mod = sm.OLS(y, x).fit()

        a, b = mod.params[0], mod.params[1]

        return (a, b)

    def unlog_value(self, a, b):
        log_a = math.exp(a)
        log_b = math.exp(b)

        return (log_a, log_b)

    def predict(self, days):
        if days >= 402:
            return False

        Table = self.create_table()
        index_arr_country = []
        index_country = 0
        country_list = Table['iso_code']
        country_currently = Table['iso_code'][0]
        for country in country_list:
            if country != country_currently:
                index_arr_country.append(index_country)
                country_currently = country
            index_country += 1

        world_cases_sum_per_country = self.log_cases(self.world_cases_sum(
            days, index_arr_country, Table))

        a, b = self.statmodels_linear_regression(
            days, world_cases_sum_per_country)

        a, b = self.unlog_value(a, b)

        for day in range(1, days + 1):
            value = int(a * math.pow(b, day))
            print(day, '->', value)

        return True

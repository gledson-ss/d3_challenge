import csv
import pandas as pd


keywords = [
    'iso_code',
    'date',
    'new_cases',
    'new_cases_per_million',
    'median_age'
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

Table = pd.DataFrame(dict_keywords)

index_arr_country = []

index = 0
country_list = Table['iso_code']
country_currently = None
for country in country_list:
    if country != country_currently:
        index_arr_country.append(index)
        country_currently = country
    index += 1

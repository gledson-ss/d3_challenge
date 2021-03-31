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
            for j in range(size_keywords):
                index_line.append(line.index(keywords[j]))
        else:
            for k in range(size_keywords):
                dict_keywords[keywords[k]].append(line[index_line[k]])

        ## break for testing only.
        if(count == 2):
            break

table = pd.DataFrame({
    keywords[0]: dict_keywords[keywords[0]],
    keywords[1]: dict_keywords[keywords[1]],
    keywords[2]: dict_keywords[keywords[2]],
    keywords[3]: dict_keywords[keywords[3]],
    keywords[4]: dict_keywords[keywords[4]]
})

print(table)

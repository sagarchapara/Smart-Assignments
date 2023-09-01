import pandas
import helpers
import numpy as np
from sklearn.preprocessing import OneHotEncoder

assignedTo = "Assigned To"
resolvedBy = "Resolved By"
activatedBy = "Activated By"
closedBy = "Closed By"
title = "Title"
description = "Description"
tags = "Tags"
result = 'Result'
data = "Data"

num_labels = 8

def findAndReplace(row):
    if row[assignedTo] in names.keys():
        return int(names[row[assignedTo]])
    elif row[resolvedBy] in names.keys():
        return int(names[row[resolvedBy]])
    else:
        return int(names[row[activatedBy]])

def findAndReplaceV2(row):
    if row[assignedTo] in names.keys():
        return int(names[row[assignedTo]])
    elif row[resolvedBy] in names.keys():
        return int(names[row[resolvedBy]])
    else:
        return int(names[row[closedBy]])

names = {}

index_names = {}

def ReadData():
    df = pandas.read_csv('Smart Assignments query.csv')
    df[result] = df.apply(findAndReplace, axis=1)

    # remove unused columns
    df = df.drop(columns=['ID','Work Item Type', 'Assigned To', 'State', 'Resolved By', 'Activated By'])

    df[data] = df[title].astype(str) + "; " + df[tags].astype(str)

    df = df.drop(columns=[description, tags, title])

    # print(df[data][21])

    # df[description].replace(np.nan, '', inplace=True)
    # df[tags].replace(np.nan, '', inplace=True)

    # print(df.columns)
    # print(df['result'].unique())
    return df

def ReadDataV2():
    df = pandas.read_csv('query_new.csv')
    df[result] = df.apply(findAndReplaceV2, axis=1)

    # remove unused columns
    df = df.drop(columns=['ID','Work Item Type', 'State'])

    df[tags].replace(np.nan, '', inplace=True)

    df[data] = df[title].astype(str) + "; " + df[tags].astype(str)

    df = df.drop(columns=[description, tags, title, assignedTo, resolvedBy, closedBy])

    df[data] = df[data].apply(helpers.clean_text)

    print(df.shape)

    return df


print(ReadDataV2())







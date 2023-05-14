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

names = {
    'Abhay Mumbare <abmumbar@microsoft.com>' : 0,
    'Nirav Patel <nipa@microsoft.com>': 1,
    'Spandana Otra <spandanaotra@microsoft.com>': 2,
    'Sagar Chapara <chaparasagar@microsoft.com>': 3,
    'Villash . <villashlnu@microsoft.com>': 4,
    'Vidhu Gangwar <vidhugangwar@microsoft.com>': 5,
    'Varun Avadhani K <vavadhanik@microsoft.com>': 6,
    'Prakhar Tripathi <pratripathi@microsoft.com>': 7,
}

index_names = {
    0: 'Abhay Mumbare <abmumbar@microsoft.com>',
    1: 'Nirav Patel <nipa@microsoft.com>',
    2: 'Spandana Otra <spandanaotra@microsoft.com>',
    3: 'Sagar Chapara <chaparasagar@microsoft.com>',
    4: 'Villash . <villashlnu@microsoft.com>',
    5: 'Vidhu Gangwar <vidhugangwar@microsoft.com>',
    6: 'Varun Avadhani K <vavadhanik@microsoft.com>',
    7: 'Prakhar Tripathi <pratripathi@microsoft.com>',
}

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







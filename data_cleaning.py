# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:51:45 2020

@author: Azhagu
"""

import pandas as pd
from sys import exit

df = pd.read_csv('glassdoor_jobs.csv')

df.head()

# salary parsing

df = df[df['Salary Estimate'] != '-1'] 
df = df.reset_index(drop = True)

                      
df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: x.replace('K','').replace('₹','').replace(',','').split('\n'))                      
salary = pd.DataFrame(df['Salary Estimate'].to_list(), columns=['min_salary','max_salary'])
df = pd.concat([df,salary], axis=1)
df.drop(['Salary Estimate'], axis = 1, inplace = True)
df['min_salary'] = df['min_salary'].astype(int)
df['max_salary'] = df['max_salary'].astype(int)
df['avg_salary'] = (df.min_salary + df.max_salary)/2

# Company name text only
df['Company_txt'] = df['Company Name'].str.replace('\\n','').str[0:-3]

# Age of Company
df['age'] = df['Founded'].apply(lambda x: x if x<1 else 2020 -x)
# Parsing of job description (python, etc.,)
df['python_yn']= df['Job Description'].astype(str).apply(lambda x: 1 if 'python' in x.lower() else 0)
df['Tableau_yn']= df['Job Description'].astype(str).apply(lambda x: 1 if 'tableau' in x.lower() else 0)
# df.Tableau_yn.value_counts()
df['Excel_yn']= df['Job Description'].astype(str).apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.Excel_yn.value_counts()
# exit(0)
df.to_csv('Salary_data_cleaned.csv', index = False)
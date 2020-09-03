import webscrap as gs
import pandas as pd
path = 'C:/Users/AZHAGU/Downloads/GitPrj/ds_salary_proj/chromedriver'

df = gs.get_jobs('data_scientist', 400, False, path, 15)
df.to_csv('glassdoor_jobs.csv', index = False)
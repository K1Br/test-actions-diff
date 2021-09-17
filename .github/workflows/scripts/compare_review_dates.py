from datetime import datetime as dt
from pathlib import Path
import pandas as pd
import re
import itertools

#Read as text blob 
txt = Path('gitdiff_dates.csv').read_text()

#Split the files by where it begins to report a new file
updated_files = txt.split('diff --git')

# Retain only updated files that have review dates altered and extract the dates
reviewed_files = [i for i in updated_files if '-review_date' in i]
match = re.findall(r'\d{4}-\d{2}-\d{2}', reviewed_files[0])
print('abc')
raise ValueError("date diff to high")
#compare if the review dates are within our specified bounds
for a, b in itertools.combinations(match, 2):
    date_diff = dt.strptime(b, "%Y-%m-%d") - dt.strptime(a, "%Y-%m-%d")
    print(date_diff)
    if date_diff.days > 92: raise ValueError("date diff to high")



'''print(os.getenv('GITHUB_OLD_DATE'),"old date")
print(os.getenv('GITHUB_NEW_DATE'), "new date")

if (os.environ['GITHUB_NEW_DATE'] != ''):
    date_diff = dt.strptime(os.environ['GITHUB_NEW_DATE'], "%Y-%m-%d") - dt.strptime(os.environ['GITHUB_OLD_DATE'], "%Y-%m-%d")
    print(date_diff)
    if date_diff.days > 92: raise ValueError("date diff to high")
'''
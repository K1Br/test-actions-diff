from datetime import datetime as dt
import os
test = pd.read_csv('gitdiff_dates.csv')
print(test)
print(os.getenv('GITHUB_OLD_DATE'),"old date")
print(os.getenv('GITHUB_NEW_DATE'), "new date")

if (os.environ['GITHUB_NEW_DATE'] != ''):
    date_diff = dt.strptime(os.environ['GITHUB_NEW_DATE'], "%Y-%m-%d") - dt.strptime(os.environ['GITHUB_OLD_DATE'], "%Y-%m-%d")
    print(date_diff)
    if date_diff.days > 92: raise ValueError("date diff to high")

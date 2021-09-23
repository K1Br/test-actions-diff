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

#compare if the review dates are within our specified bounds
for outtext in reviewed_files:
    match = re.findall(r'\d{4}-\d{2}-\d{2}', outtext)
    filename= re.findall(r'(?<=- a\/)(.*)(?!.yml)',outtext)
    for a, b in itertools.combinations(match, 2):
        date_diff = dt.strptime(b, "%Y-%m-%d") - dt.strptime(a, "%Y-%m-%d")
        if date_diff.days > 92:
            error_statement = "Date difference too high: " + str(date_diff.days) + " in file: " + filename + "Needs to be under X months/ X days" + " Dates: "
            raise ValueError("Date diff too high", error_statement,match)
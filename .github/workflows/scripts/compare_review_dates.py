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
    for a, b in itertools.combinations(match, 2):
        date_diff = dt.strptime(b, "%Y-%m-%d") - dt.strptime(a, "%Y-%m-%d")
        if date_diff.days > 92:
            print(date_diff,outtext)
            raise ValueError("date diff to high")
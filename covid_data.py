import os
import git
import shutil
import tempfile
import csv
from datetime import datetime, date
import urllib.request

class CovidData:

    def __init__(self, dates):
        self.date = date

    def get_data():
        pass

# t = tempfile.mkdtemp()
# git.Repo.clone_from('https://github.com/nytimes/covid-19-data.git', t, branch='master', depth=1)
# shutil.move(os.path.join(t, 'us.csv'), '/home/chris/download-files')
# shutil.rmtree(t)

covid_data = []
download_path = "/home/chris/download-files"
path = "/home/chris/download-files/us.csv"

with open(path, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        date_obj = datetime.strptime(row[0], '%Y-%m-%d')
        covid_data.append( 
            {
                'date': date_obj.date(), 
                'cases': int(row[1]), 
                'deaths': int(row[2])
            }
        )


# url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv?opt_id=undefined"
# urllib.request.urlretrieve(url, f'{download_path}/hopkins_data.csv')
recovery_data = []
with open(f'{download_path}/hopkins_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        date_obj = datetime.strptime(row[0], '%Y-%m-%d')
        recovery_data.append( 
            {
                'date': date_obj.date(), 
                'country': row[1], 
                'recovery': row[4]
            }



    
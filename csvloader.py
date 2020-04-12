import csv
import os

path =  "/Users/bill/dev/breadlist" # Set path of new directory here
os.chdir(path) # changes the directory
from classifieds.models import Province # imports the model
with open('provinces.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
            p = Province(province_name=row['Province_name'])
            p.save()

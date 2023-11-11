# Wrangling methods
import pandas as pd

path = '../data/vehicles.csv'
acquisition_output = pd.read_csv(path)
acquisition_output

year = 1997
wrangling_output = acquisition_output[acquisition_output['Year'] == year].reset_index(drop=True)

def wrangling(desired_year, df):
    df = df[df['Year'] == desired_year].reset_index(drop=True)
    return df    

wrangling(year, acquisition_output)

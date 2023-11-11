# Imports 
from macquisition import acquisition as ac
from mwrangling import wrangling as wr
from manalysis import analysis as an
import pandas as pd

# Input
path = '../data/vehicles.csv'
input_year = input('Enter a year: ')

# Pipeline
if __name__ == '_main_':
    #Primera fase de la pipeline 
    dataframe_acquisition = ac.acquisition(path)
    #SEgunda fase de la pipeline
    dataframe_wrangling = wr.wrangling(input_year, dataframe_acquisition)
    #Tercera fase de la pipeline
    pipeline_end_message = an.analysis(dataframe_wrangling)
    print(pipeline_end_message)
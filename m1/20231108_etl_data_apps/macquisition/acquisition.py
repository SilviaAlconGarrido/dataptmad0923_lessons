# Acquisition methods
import os
from dotenv import load_dotenv 

load_dotenv('.env')
API_TOKEN = os.environ.get("API_TOKEN")

path = '../data/vehicles.csv'
df = pd.read_csv(path)
df

def acquisition(file_path):
    df_acquisition = pd.read_csv(file_path)
    return df_acquisition

acquisition(path)
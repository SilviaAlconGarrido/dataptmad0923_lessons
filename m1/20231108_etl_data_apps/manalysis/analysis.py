# Analysis methods
path = '../data/vehicles.csv'
df = pd.read_csv(path)
df

df.info()

analysis = df.groupby(['Make'])[['Combined MPG']].mean().sort_values(by='Combined MPG', ascending=False).reset_index()
analysis

def analysis(df_analysis):
    df_output = df_analysis.groupby(['Make'])[['Combined MPG']].mean()\
    .sort_values(by='Combined MPG', ascending=False).reset_index()
    df_output.to_csv('../data/combined_mpg_analysis.csv')
    return '---your file is located in the data folder---'

analysis(df)

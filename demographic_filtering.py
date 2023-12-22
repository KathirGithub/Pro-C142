import pandas as pd

# create a dataframe using final.csv file
df = pd.read_csv('articles.csv')

# sorting dataframe : wrt to weighted rating col in ascending order
df = df.sort_values('total_events' , ascending = False)

# final dataframe
output = df[['url' , 'title' , 'text', 'lang' , 'total_events' ]].head(20)

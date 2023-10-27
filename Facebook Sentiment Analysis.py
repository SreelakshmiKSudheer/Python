'''
pandas library --> provides easy to use data structers for data analysis

nltk library --> used to process human language
            --> sentiment analysis for human data
            --> ''  invloves working out whether a piece of text is positive, -ve or neutral
            
VADER --> Valence Awaere Dictionary and Sentiment Reasoner
        instensity sentiment
        
Data frame --> 2D structure in form of table'''

import pandas as pd 
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.downloader.download("vader_lexicon")
file = 'data_file.xslsx'
xl = pd.ExcelFile(file)  #Read from Excel
dfs = xl.parse(xl.sheet_names[0])       # Parsing Excel sheet to data frame
dfs = list(dfs['Timeline'])     # Remove the blank rows from the data frame
print(dfs)

sid = SentimentIntensityAnalyzer()
str1 = "UTC+05.30"

for data in dfs:
    a = data.find(str1)
    if(a == -1):
        ss = sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])
            
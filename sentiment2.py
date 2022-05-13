import pandas as pd
import datetime as dt
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.mlab as mlab

#import csv files
df_st_maud = pd.read_csv('st_maud.csv')
df_hereditary = pd.read_csv('hereditary.csv')
df_midsommar = pd.read_csv('midsommar.csv')
print(df_st_maud.columns)

# #get sentiment scores
analyzer = SentimentIntensityAnalyzer()
sentiment_st_maud = df_st_maud['Embedded_text'].apply(lambda x: analyzer.polarity_scores(x))
sentiment_hereditary = df_hereditary['Embedded_text'].apply(lambda x: analyzer.polarity_scores(x))
sentiment_midsommar = df_midsommar['Embedded_text'].apply(lambda x: analyzer.polarity_scores(x))

#put sentiment into dataframe
df_st_maud = pd.concat([df_st_maud, sentiment_st_maud.apply(pd.Series)],1)
df_hereditary = pd.concat([df_hereditary, sentiment_hereditary.apply(pd.Series)],1)
df_midsommar = pd.concat([df_midsommar, sentiment_midsommar.apply(pd.Series)],1)

#Clean up data.  Remove duplicates, decided to leave in capitalization and punctuation since Vader uses those for sentiment.
#Consider stripping special characters
df_st_maud.drop_duplicates(subset = 'Embedded_text',inplace = True)
df_hereditary.drop_duplicates(subset = 'Embedded_text',inplace = True)
df_midsommar.drop_duplicates(subset = 'Embedded_text',inplace = True)

#print and display histograms for each film:
print("Overall Sentiment for Saint Maud: ",df_st_maud['compound'].sum())
print("Overall Sentiment for Hereditary: ",df_hereditary['compound'].sum())
print("Overall Sentiment for Midsommar: ",df_midsommar['compound'].sum())

df_st_maud['compound'].hist()
plt.title('Saint Maud')
plt.show()
df_hereditary['compound'].hist()
plt.title('Hereditary')
plt.show()
df_midsommar['compound'].hist()
plt.title('Midsommar')
plt.show()

ax1 = sns.distplot(df_st_maud['compound'], bins=15, hist = False, label = 'Saint Maud', color ='blue')
ax2 = sns.distplot(df_hereditary['compound'], bins=15, hist = False, label = 'Hereditary', color ='red')
ax3 = sns.distplot(df_midsommar['compound'], bins=15, hist = False, label = 'Midsommar', color ='green')
plt.legend()
plt.title('A24 Films')
plt.show()

# save output to a .csv
df_st_maud.to_csv('stmaud_sentiment_cleaned.csv')
df_hereditary.to_csv('hereditary_sentiment_cleaned.csv')
df_midsommar.to_csv('midsommar_sentiment_cleaned.csv')

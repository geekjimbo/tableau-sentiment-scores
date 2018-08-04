from pandas import Series
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentences = input_table['reviews.text']
scores = []
analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    scores.append(vs['compound'])
    
# output_table definition 
output_table = input_table.copy()
# Append predictions
output_table['sentiment_score'] = Series(scores, index=output_table.index)

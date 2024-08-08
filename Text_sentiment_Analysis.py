from textblob import TextBlob

text = 'you are bad person'
analysis = TextBlob(text)
sentiment = analysis.sentiment.polarity

if sentiment > 0:
    print('Positive Sentiment')
elif sentiment < 0:
    print('Nagative Sentiment')
else:
    print('Neutral Sentiment')

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


'''Pass the file with the path you are using :)'''

analyzer = SentimentIntensityAnalyzer()
with open(file, 'r') as in_file:
    text = in_file.read()
    sents = nltk.sent_tokenize(text)
    for s in sents:
        snt = analyzer.polarity_scores(s)
        print("{:-<40} {}".format(s, str(snt)))

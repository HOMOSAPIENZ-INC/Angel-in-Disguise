import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import io

class Sentiment(object):

    @staticmethod
    def vader(file):
        analyzer = SentimentIntensityAnalyzer()
        with open(file, 'r') as in_file:
            text = in_file.read()
            sents = nltk.sent_tokenize(text)
            for s in sents:
                snt = analyzer.polarity_scores(s)
                print("{:-<40} {}".format(s, str(snt)))

    @staticmethod
    def naive(file):


        '''BOIS add texts followed by neg or pos for training
        since it is naive bayes it will not need more than 10 sentences to
        work well enough'''

        train = [("Had a great day, loved it", "pos"),
                 ("test 2", "neg"),
                ]
        dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))

        t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]

        classifier = nltk.NaiveBayesClassifier.train(t)

        with open(file, 'r') as in_file:
            text = in_file.read()
            sents = nltk.sent_tokenize(text)
            for s in sents:
                test_data = s
                test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}

                print (s, (classifier.classify(test_data_features)))

    @staticmethod
    def blob(file):
        with io.open(file, 'r', encoding='utf-8') as in_file:
            text = in_file.read()
            sents = nltk.sent_tokenize(text)
            for s in sents:
                q = TextBlob(s)
                print (s, q.sentiment)
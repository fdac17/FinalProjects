import boto3
from boto3.dynamodb.conditions import Key, Attr
import json
from time import sleep
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from bs4 import BeautifulSoup
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def cleanHtml (html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup .get_text()

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table("pitchfork_reviews")

response = table.scan(
        FilterExpression=Attr('genre').eq('Rock')
)

data = []

data.extend(response['Items'])

while 'LastEvaluatedKey' in response:
  try:
    response = table.scan(
          ExclusiveStartKey=response['LastEvaluatedKey'],
          FilterExpression=Attr('genre').eq('Rock')
    )
    data.extend(response['Items'])
  except:
    print("sleeping...")
    sleep(30)

body = []
tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()

sentiment = []

for d in data:
  b = cleanHtml(d['body']).lower()
  review = TextBlob(b, analyzer=NaiveBayesAnalyzer())

  sentiment.append(review.sentiment.classification)

good_reviews = sum(i is 'pos' for i in sentiment)
bad_reviews = sum(i is 'neg' for i in sentiment)

print("Good reviews: ", good_reviews)
print("Bad reviews: ", bad_reviews)

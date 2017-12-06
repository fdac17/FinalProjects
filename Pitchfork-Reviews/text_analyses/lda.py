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
        FilterExpression=Attr('rating').lt('11')
)

data = []

while 'LastEvaluatedKey' in response:
  try:
    response = table.scan(
          ExclusiveStartKey=response['LastEvaluatedKey'],
          FilterExpression=Attr('rating').lt('11')
    )
    data.extend(response['Items'])
  except:
    print("sleeping...")
    sleep(30)

body = []
tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()

for d in data:
  b = cleanHtml(d['body']).lower()
  tokens = tokenizer.tokenize(b)
  text = [p_stemmer.stem(i) for i in tokens if not i in en_stop]
  body.append(' '.join(text))

tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                max_features=10,
                                stop_words='english')
tf = tf_vectorizer.fit_transform(body)
lda = LatentDirichletAllocation(n_topics=8, max_iter=50, learning_method='online', learning_offset=10, random_state=0)
lda.fit(tf)

print("\nTopics in LDA model:")
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, 10)

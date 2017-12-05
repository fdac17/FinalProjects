from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from data_processing import *
import operator
import string

stop_words = ['about', 'of', 'a', 'i', 'the', 'on', 'up', 'had', 'with', 'for', 'is', 'that', 'they', 'was',
				'your', 'you', 'their', "they're", 'only', "youre", 'or', 'and', 'then', 'to', 'it',
				'have', 'get', 'at', 'one', 'all', "dont", 'an', 'as', 'from', 'are', '-', 'my', 'just',
				'do', 'too', 'were', 'has', 'still', 'see', 'way', 'need', 'them', 'us', 'did', 'got',
				'him', 'since', 'much', 'more', 'been', 'in', 'but', 'am', 'me', 'now', 'this', 'be', 'can',
				'out', 'know', 'u', 'if', 'there', 'we', "ive", 'like', "hes", 'than', 'her', 'by', 'go',
				'good', 'bad', '1', '2', '3', 'not', 'both', 'any', 'off', 'thing', 'back', 'should', 'things',
				"didnt", 'will', 'around', 'other', 'most', 'seen', 'doing', 'going', "doesnt", 'very',
				'which', '', 'our', 'would', 'really', 'theyre', 'into', 'when', 'where', 'so', 'its', 'shes',
				'well', 'because', "don't", 'yes', 'some', 'think']

off_list = ['league', 'legends', 'champions', 'champs', 'riot']

#todo "we" vs. "i", "you" vs "them" vs "us"

#return dictionary of word counts
def get_word_count(data):
	counts = {}
	word_sum = 0
	for d in data:
		#process the text
		if d['text'] is not None:
			for w in d['text'].split():
				translator = str.maketrans('\'', ' ', string.punctuation)
				w = w.translate(translator)
				if w not in stop_words:
					word_sum += 1
					if w not in counts:
						counts[w.lower()] = 1
					else:
						counts[w.lower()]+=1
	return counts, word_sum

def graph_word_count(data, name, filename, word_sum):
	y_pos = np.arange(len(data))
	r = plt.figure(figsize=(8,12))
	f = plt.barh(y_pos, [i[1] for i in data], align='center', alpha=0.5)
	plt.yticks(y_pos, [i[0] for i in data])
	plt.xlabel('Word Count Out of ' + str(word_sum))
	plt.title('Counts of Words in The ' + name + ' Groupme')
	plt.savefig(filename)
	plt.close()

def get_post_count(data):
	return len(data)

def graph_post_count(data):
	y_pos = np.arange(len(data.keys()))
	
	plt.bar(y_pos, data.values(), align='center', alpha=0.5)
	plt.xticks(y_pos, [group_names[name] for name in data.keys()])
	plt.ylabel('Number of Posts')
	plt.title('Number of Posts By Groupme For The Month of November')
	plt.savefig('post_count.png')
	plt.close()

def get_link_count(data):
	link_count = 0
	for d in data:
		#process the text
		if d['text'] is not None and d['text'].count('http') > 0:
			link_count += 1
	return link_count

def graph_link_count(data):
	y_pos = np.arange(len(data.keys()))
	
	plt.bar(y_pos, data.values(), align='center', alpha=0.5)
	plt.xticks(y_pos, [group_names[name] for name in data.keys()])
	plt.ylabel('Number of Links Posted')
	plt.title('Links Posted Per Groupme Chat')
	plt.savefig('link_count.png')
	plt.close()

#data is the list of entries
#specifically for the overwatch groupme
def get_user_offtopic(data):
	user_ontopic = {}
	on_topic = 0
	for d in data:
		if d['text'] is not None and d['text'].count('league') > 0:#any(substring in d['text'].lower() for substring in off_list):
			on_topic+=1
	return on_topic
	
start = datetime(2017, 11, 1, 0, 0, 0)
end = datetime(2017, 11, 30, 23,59, 59)
link_count = {}
post_count = {}
for i in groups:
	data = get_data_range(start, end, i)
	word_counts, word_sum = get_word_count(data)
	wc = sorted(word_counts.items(), key = operator.itemgetter(1), reverse=True)
	graph_word_count(wc[:20], group_names[i], i+"_word_count20.png", word_sum)
	link_count[i] = get_link_count(data)
	post_count[i] = get_post_count(data)
	#print(wc[:100])

graph_link_count(link_count)
graph_post_count(post_count)
print(get_user_offtopic(get_data_range(start, end, 'overwatch')))

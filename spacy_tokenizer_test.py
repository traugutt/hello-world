import spacy
nlp = spacy.load("en_core_web_md", disable=['textcat','ner'])
import json
with open ('C:\\Users\\olena\\PycharmProjects\\sofia-training\\test-set.json','r',encoding='UTF-8') as f:
	test_data = json.load(f)

def metric(test_data):
	tp = 0
	for sample in test_data:
		formatted_headline = format_headline(nlp(sample[0]))
		if formatted_headline == sample[1]:
			tp += 1
	return tp/len(test_data)

headline = nlp('Pondering the parable: Who is the foreman')

def is_notional(token):
	return token.tag_.startswith('NN') or \
	 	   token.tag_.startswith('VB') or \
	       token.tag_.startswith('JJ') or \
	       token.tag_.startswith('RB') or \
	       token.tag_.startswith('CD') or \
	       token.tag_.startswith('PRP') or \
	       token.tag_.startswith('MD')


def format_headline(headline):
	formatted_headline = ""
	for token in headline:
		if token.text.isupper() or token.text.lower() == "n't":
			formatted_headline += token.text
		elif len(token) > 3 or is_notional(token) or \
		    token.dep_ == 'mark' or token.i in {0, len(headline) -1}:
			formatted_headline += token.text.title()
		else:
			formatted_headline += token.text.lower()
		formatted_headline += token.whitespace_
	return formatted_headline

print(format_headline(headline))
print(metric(test_data))
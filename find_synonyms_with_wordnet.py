import nltk
from nltk.corpus import wordnet


word = 'suit'
def wordnet_get(word):
    x = wordnet.synsets(word)
    if x == []:
        print('Sorry, we can\'t find this word, you might want to check the spelling')

    definition = [i.definition() for i in x]
    pos=[p.pos() for p in x]
    # synonyms=[s.synonyms() for s in x]
    hyponyms=[h.hyponyms()for h in x]
    hypernyms=[hpr.hypernyms()for hpr in x]
    n=0
    number=[n+1 for num in x]
    intro = 'The word {} has the following meanings:'.format(word)
    everything = [definition, pos, hyponyms, hypernyms, number]
    for output in everything:
             print('{}{}\n It has the following synonyms:{}\n ' \
             'Hypernyms:{}' \
             '\n Hyponyms:{}\n'.format(number, definition,'',hypernyms,hyponyms))



    print(''.join(output))






wordnet_get(word)



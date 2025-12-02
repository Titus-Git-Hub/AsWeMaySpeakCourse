import tracery
from tracery.modifiers import base_english

import spacy
nlp = spacy.load('en_core_web_md')

text = open("../week4/test_text").read()
doc = nlp(text)
all_words = [token for token in doc if token.is_alpha]

NOUNs = [token.lemma_ for token in all_words if token.pos_ == "NOUN"]
VERBs = [token.lemma_ for token in all_words if token.pos_ == "VERB"]
ADJs  = [token.lemma_ for token in all_words if token.pos_ == "ADJ"]
ADVs  = [token.lemma_ for token in all_words if token.pos_ == "ADV"]
PRONs = [token.lemma_ for token in all_words if token.pos_ == "PRON"]
ADPs  = [token.lemma_ for token in all_words if token.pos_ == "ADP"]
DETs  = [token.lemma_ for token in all_words if token.pos_ == "DET"]
AUXs  = [token.lemma_ for token in all_words if token.pos_ == "AUX"]

# The idea was to have different sentence structures for the generator, as well as capitalizing Nouns same as the start of each sentence and ending with a period at the end of each sentence.

# Probably it does not generate the most meaningful sentences but it was somehow interesting thinking about all the aspects that need to be taken into account while creating a text corpus based generator.

rules = {
    "origin": ["#sentence_type_1#", "#sentence_type_2#", "#sentence_type_3#", "#sentence_type_4#", "#sentence_type_5#"],
    "sentence_type_1": "#Article.capitalize# #Noun.capitalize# #Verb# #Article# #Noun.capitalize#.",
    "sentence_type_2": "#Article.capitalize# #Noun.capitalize# #Verb# #Preposition# #Article# #Noun.capitalize#.",
    "sentence_type_3": "#Pronoun.capitalize# #AuxVerb# #Adverb# #Verb# #Article# #Noun.capitalize#.",
    "sentence_type_4": "#Article.capitalize# #Noun.capitalize# #Verb# #Article# #Noun.capitalize# #Preposition# #Article# #Noun.capitalize#.",
    "sentence_type_5": "#Pronoun.capitalize# #AuxVerb# #Article# #Adjective# #Noun.capitalize# #Verb#.",
    "Noun": NOUNs,
    "Verb": VERBs,
    "Adjective": ADJs,
    "Adverb": ADVs,
    "Pronoun": PRONs,
    "Preposition": ADPs,
    "Article": DETs,
    "AuxVerb": AUXs
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

for i in range(10):
    print(grammar.flatten("#origin#"))

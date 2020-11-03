import spacy
from spacy.matcher import Matcher
from .meta_patterns import *
from asgiref.sync import sync_to_async


nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)

# patterns are inside patterns.py
# there are many patterns from many meta like questions

matcher.add('META_QUES', None, meta1, meta2, meta3, meta4, meta5)
matcher.add('WHERE', None, place)
matcher.add('WHAT', None, question)

@sync_to_async
def string_match(data):

    doc = nlp(data)
    matches = matcher(doc)

    word_type = []
    word = []

    for match_id, start, end in matches:
        rule_id = nlp.vocab.strings[match_id]
        spans = doc[start:end]
        word.append(spans)
        word_type.append(rule_id)

    return word_type, word





##################### if list is empty#######################

# if not list:
#     print("Everything is normal.")




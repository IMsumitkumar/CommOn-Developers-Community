# anyone who knows python here?
meta1 = [
    {'LOWER': 'anyone'},
    {'POS': 'PRON', 'OP': '?'},
    {'LOWER': 'knows'},
    {'POS': 'PROPN', 'OP': '?'},
    {'POS': 'ADV', 'OP': '?'}
]

# do you know / do you know me
meta2 = [
    {'LOWER': 'do'},
    {'LOWER': 'you'},
    {'POS': 'VERB','OP':'?'},
    {'POS': 'PRON', 'OP': '?'}
]

# any user of $x here?
meta3 = [
    {'LOWER': 'any'},
    {'LOWER': 'user'},
    {'POS': 'ADP', 'OP': '?'},
    {'POS': 'PROPN', 'OP': '?'},
    {'POS': 'ADV', 'OP': '?'}
]

# Hello! I need some help on $x.
meta4 = [
    {'LOWER': 'need'},
    {'POS': 'DET','OP':'?'},
    {'LOWER': 'help'},
]

#please help me
meta5 = [
    {'LOWER': 'please'},
    {'LOWER': 'help'},
    {'POS': 'PRON', 'OP': '?'}
]

# where are you from ?
place = [
    {'LOWER': 'where'},
    {'POS': 'AUX'},
    {'POS': 'PRON','OP':'?'},
    {'POS': 'ADP', 'OP': '?'},
]

# what is $x?
question = [
    {'LOWER': 'what'},
    {'POS': 'AUX'},
    {'POS': 'NOUN', 'OP': '?'},
]


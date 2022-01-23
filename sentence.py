def sentence_type(s):
    if s.endswith('!'): 
        return 'exclamatory'
    elif s.endswith('?'):
        return 'interrogative'
    elif s.endswith('.'):
        return 'declarative'
    else:
        return 'bad ending'

print(sentence_type('This is a sentence!'))
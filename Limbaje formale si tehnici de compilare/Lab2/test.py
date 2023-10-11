import re

#token='"multiplu3"'
token='"nuEsteMultiplu_3"'
result = re.search('^[0-9]$|^\'[0-9]\'$|^[1-9]+[0-9]*$|^\"[1-9]+[0-9]+\"$|^\'[A-Za-z]\'$|^\"[A-Za-z]+\w*\"$', token)
print(len(token))
print(result)
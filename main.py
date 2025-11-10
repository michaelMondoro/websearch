from search import *

engine = SearchEngine()
engine.search("va gov elections", 3, 'd')

print(engine.results[0].text)
print(engine)
[![Test](https://github.com/michaelMondoro/websearch/actions/workflows/test.yaml/badge.svg)](https://github.com/michaelMondoro/websearch/actions/workflows/test.yaml)
# websearch

python package for searching the web - using [DuckDuckGo HTML](https://html.duckduckgo.com/html/)

### Usage
```python
from Search import *

engine = SearchEngine()
engine.search("hello world", 3)
print(engine)


# Ouptut
2025-11-22 10:33:53,661 - INFO - Processing web result: https://en.wikipedia.org/wiki/%22Hello,_World!%22_program
2025-11-22 10:33:54,565 - INFO - Processing web result: https://www.howtogeek.com/hello-world-universal-first-step-for-programming/
2025-11-22 10:33:55,266 - INFO - Processing web result: https://www.geeksforgeeks.org/dsa/hello-world-program-first-program-while-learning-programming/
Engine(results=3, logging=enabled)

```
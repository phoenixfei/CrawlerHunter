with open('news/news.txt', 'r') as f:
    source = f.read().split('\n')
    print(source)
from collections import Counter
print(Counter(source))
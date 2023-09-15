from googlesearch import search

for j in search('python for security engineers', tld="co.in", num=10, stop=10, pause=2):
    print(j)
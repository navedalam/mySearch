#alam
#Wikipedia Crawler

import urllib

print "Enter search term:"
search = raw_input()
terms = search.split(" ")

response = urllib.urlopen("http://en.wikipedia.org/wiki/Special:Export/"+search)
response_page = response.read()
print response_page

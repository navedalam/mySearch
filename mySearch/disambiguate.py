#alam
#Word Sense Disambiguator

import urllib2

def disambiguate(term):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    
    infile = opener.open('http://en.wikipedia.org/wiki/Special:Export/' + term)
    
    #infile = opener.open('http://en.wikipedia.org/wiki/Special:Export/Apple_(disambiguation)')
    page = infile.read()
    if ('{{disambig}}' not in page) and ('{{Disambig}}' not in page):
        infile = opener.open('http://en.wikipedia.org/wiki/Special:Export/' + term + '_(disambiguation)')
        page = infile.read()
        #print page
    
    if ('{{disambig}}' not in page) and ('{{Disambig}}' not in page):
        print "Only one context available"
        page=""
        
    #print page
    context=[]
    
    while('===' in page):
        page=page.partition('===')[2] #Page becomes part after first '=='
        tcontext=page.partition('\n')[0][:-3].strip().lower()
        if 'in ' in tcontext:
            tcontext=tcontext[3:]
        if (tcontext!="") and ('also' not in tcontext) and ('other' not in tcontext):
            context.append(tcontext)
    
    while('==' in page):
        page=page.partition('==')[2] #Page becomes part after first '=='
        tcontext=page.partition('\n')[0][:-2].strip().lower()
        if 'in ' in tcontext:
            tcontext=tcontext[3:]
        if (tcontext!="") and ('also' not in tcontext) and ('other' not in tcontext):
            context.append(tcontext)
            
    while(';' in page):
        page=page.partition(';')[2] #Page becomes part after first '=='
        tcontext=page.partition('\n')[0].strip().lower()
        if 'in ' in tcontext:
            tcontext=tcontext[3:]
        if (tcontext!="") and ('also' not in tcontext) and ('other' not in tcontext):
            context.append(tcontext)

    return context

if __name__ == '__main__':
    for i in ['apple', 'cricket', 'arm', 'python', 'bat', 'bowl']:
        print "Word:", i, " Contexts:", disambiguate(i)

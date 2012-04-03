#@Phoenix
#Similarity Score Calculator

from nltk.corpus import wordnet as wn
from nltk.tokenize import WordPunctTokenizer
from fbcrawler import getsocialinformation
from disambiguate import disambiguate

def mysearch(input_string="python"):
    sources=['likes', 'geographic', 'education', 'work']
    socialinformation=getsocialinformation(sources)
    
    #input_string="python rocks"
    wiki_contexts=disambiguate(WordPunctTokenizer().tokenize(input_string)[0])
    outputdata=[]
    
    #wiki_contexts=['programming', 'language', 'IT', 'lion']
    #socialinformation={'interests':['programming', 'language', 'computer'], 'fields_of_interest':['biology', 'snake', 'reptile'], 'geography':[], 'work':[]}
    
    for wiki_context in wiki_contexts:
        similarity_scores=[]
        for category in socialinformation.keys():
            t_sims=[0]
            #print category
            for item in socialinformation[category]:
                for i in wn.synsets(wiki_context):
                    for j in wn.synsets(item):
                        #print i, j, i.wup_similarity(j)
                        t_sims.append(i.wup_similarity(j))
            #print t_sims
            t_sims.sort()
            t_sims[-1]
            print "MS for", wiki_context, category, "is ", t_sims[-1]
            similarity_scores.append(t_sims[-1])
            
        temp1=[wiki_context]
        temp1.extend(similarity_scores)
        outputdata.append(temp1)
    
    return outputdata

if __name__ == '__main__':
    print mysearch(input_string="python")




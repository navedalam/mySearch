import wordnet
import gui
contextlist=[]
prediction=[]
ax=[]
score=[]
source=[]
v='' 
z=[]
totalweights=0



#[["sdasda",0.4,0.2,0.2],["msdsadsamdasmo",0.3,0.5,0.6]]


def searchterm(name):
    return wordnet.mysearch(name)
    

def findmax(b):
    maxx=b[0]
    k=0
    for i in range(1,len(score)):
        if(b[i]>maxx):
            maxx=b[i]
            k=i
    return k
            

def enterweights():
    for i in range(0,(len(weights)-1)):
        source.append(weights[i])


    
def categoryprediction():
    print len(source)
    print len(listcon)
    for i in range(1,len(source)+1):
        print i
        highest=listcon[0][i]
        print"sadasdas"
        con=listcon[0][0]
        maxlist=[]
        for j in range(1,len(listcon)):
            if(listcon[j][i]>highest):
                highest=listcon[j][i]
                con=listcon[j][0]
        maxlist.append(con)
        maxlist.append(highest)
        prediction.append(maxlist)
    #print 'p', prediction

def calcontext():
    for j in range(len(listcon)):
        x=0
        for i in range(1,len(source)+1):
            x=x+listcon[j][i]
        
        ax.append(x)
    for j in range(len(listcon)):
        for i in range(1,len(source)+1):
            if(ax[j]!=0):
                listcon[j][i]=listcon[j][i]/float(ax[j])
    
    for i in range(len(listcon)):
        scorex=0
        for j in range(1,len(source)-1):
            scorex=scorex+listcon[i][j]*float(source[j-1])
        score.append(scorex)
    result=findmax(score)
    print listcon[result][0]
    return listcon[result]

def expectation():
    enterweights()
    categoryprediction()
    z=calcontext()
    #print 'z', z
    contextlist.append(z[0])
    print contextlist
    for i in range(len(listcon)):
        if(listcon[i][0]!=contextlist[0]):
            contextlist.append(listcon[i][0])
    #print contextlist
    return z, contextlist

def maximisation(q):
    #print len(source)
    #print 'q', q
    totalweight=int(weights[-1])
    #print totalweight
    for i in range(len(source)):
        #print prediction[i][0]
        #print q[0]
        if(prediction[i][0]==q[0]):
            source[i]=float(source[i])+(1.0/(totalweight**2)*((1-float(source[i]))/2))
        else:
            source[i]=float(source[i])-(1.0/(totalweight**2)*((1-float(source[i]))/2))
    print source
    f=open("weights.txt",'w')
    for i in range(len(source)):
        f.write(str(source[i]))
        f.write('\n')
    totalweight=totalweight+1
    f.write(str(totalweight))
    f.close()

def em(lista):
    listcon=lista
    f=open("weights.txt",'r')
    weights=f.readlines()
    #print weights
    f.close()
    z, ab=expectation()
    gui.predicted_context(ab)
    v=gui.correct_context()
    for i in range(len(listcon)):
        if(listcon[i][0]==v):
            z=listcon[i]
    maximisation(z)
listcon=wordnet.mysearch("apple")
em(listcon)

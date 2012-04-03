#from em import searchterm
from Tkinter import *
import Tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import time
import wordnet
cont=''


def correct_context():
    return cont
def exit(event):
    root.destroy()

def search(event):

    def predicted_context(list1):
        print list1,'ydyd'
        def button_press(context):
            root1.destroy()
            cont=str(context)
            #print("The context is " + str(context))
            
        def dest(event):
            root1.destroy()
        
        num=len(list1)
        print "lits1", list1
        root1 = Tk()
        root1.title("MySearch")
        root1.overrideredirect(1);
        #root1.mainloop()
        imageFile = "header2.gif"
        image1 = ImageTk.PhotoImage(Image.open(imageFile))


        panel1 = Label(root1, image=image1)
        panel1.pack(side='top', fill=X, expand='no')
        
        w1=400
        h1=max(len(list1)*50,150)

        ws = root1.winfo_screenwidth()
        hs = root1.winfo_screenheight()

        x = (ws/2) - (w1/2) - 7
        y = (hs/2) - (h1/2) - 2

        root1.geometry('%dx%d+%d+%d' % (w1,h1,x,y))

        for i in range(0,num):
            print "i", i
            fram = "fra" + str(i)
            lab = "label" + str(i)
            but = "label" + str(i)
            
            fram = Frame(root1)
            fram.pack(fill=X)
            
            lab = Label(fram, text = list1[i])
            lab.pack(side=LEFT,padx=5)

            but = Button(fram, text=">>", justify=CENTER,command=lambda a=list1[i]: button_press(a))
            but.pack(side=RIGHT,padx=5)
            
        '''
        fra1 = Frame(root1)
        fra1.pack(fill=X)
        
        label2 = Label(fra1, text = "Programming")
        label2.pack(side=LEFT,padx=5)

        button1 = Button(fra1, text=">>", justify=CENTER,command=lambda a="Programming": button_press(a))
        button1.pack(side=RIGHT,padx=5)

        fra2 = Frame(root1)
        fra2.pack(fill=X)
        
        label3 = Label(fra2, text = "Snake")
        label3.pack(side=LEFT,padx=5)
        
        button = Button(fra2, text=">>", justify=CENTER,command=lambda a="Snake": button_press(a))
        button.pack(side=RIGHT,padx=5)
        '''
        print"PSPS"
        #root1.focus_set()
        #root1.bind("<Escape>", dest)
        root1.mainloop()
        print "hi"

    


    contextlist=[]
    prediction=[]
    ax=[]
    score=[]
    source=[]
    #v='' 
    z=[]
    totalweights=0
    f=open("weights.txt",'r')
    weights=f.readlines()
    #print weights
    f.close()

    listcon=[]
    #=wordnet.mysearch("python")
    #[["sdasda",0.4,0.2,0.2],["msdsadsamdasmo",0.3,0.5,0.6]]

    cont = ""


    def searchterm(name):
        return wordnet.mysearch(name)
        

    def findmax(b):
        print b
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
        return source

        
    def categoryprediction(rt):
        
        print len(source)
        listcon=rt
        print listcon
        for i in range(1,len(source)+1):
            print i
            highest=listcon[0][i]
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

    def calcontext(ty,l):

        listcon=ty
        print listcon
        source=l

        '''for j in range(len(listcon)):
         
            x=0
            for i in range(1,len(source)+1):
                print listcon[j][i]
                x=x+listcon[j][i]
                print x
            
            ax.append(x)
        print ax,'ax'
        for j in range(len(listcon)):
        
            for i in range(1,len(source)+1):
                if(ax[j]!=0):
                    listcon[j][i]=listcon[j][i]/float(ax[j])
        '''
        print listcon,'please chal jaa'
        for i in range(len(listcon)):
            scorex=0
            for j in range(1,len(source)-1):
                scorex=scorex+listcon[i][j]*float(source[j-1])
            score.append(scorex)
        print score,'score'
        result=findmax(score)
        print listcon[result][0]
        return listcon[result]

        
        '''
        listcon=ty
        source=l
        print(len(source))
        #print len(listcon)
        for j in range(len(listcon)):
            x=0
            for i in range(1,len(source)+1):
                x=x+listcon[j][i]
            
            ax.append(x)
        print ax,'ax'
        for j in range(len(listcon)):
            for i in range(1,len(source)+1):
                if(ax[j]!=0):
                    listcon[j][i]=listcon[j][i]/float(ax[j])
        print listcon,'jg'
        for i in range(len(listcon)):
            scorex=0
            for j in range(1,len(source)-1):
                scorex=scorex+listcon[i][j]*float(source[j-1])
            score.append(scorex)
            print score,'score'
        result=findmax(score)
        #print listcon[result][0]
        #print listcon[result],'result'
        return listcon[result]
'''
    def expectation(qw):
        k=enterweights()
        categoryprediction(qw)
        z=calcontext(qw,k)
        #print 'z', z
        contextlist.append(z[0])
        print qw,'dfdf'
        for i in range(len(qw)):
            if(qw[i][0]!=contextlist[0]):
                contextlist.append(qw[i][0])
        print contextlist
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
        z, ab=expectation(listcon)
        predicted_context(ab)

        v=correct_context()
        for i in range(len(listcon)):
            if(listcon[i][0]==v):
                z=listcon[i]
        maximisation(z)





    root.destroy()
       
    if(v.get()==""):
        print("Empty Search Term")
        print("v = " + v.get())

    else:
        addr='http://www.google.co.in/search?hl=en&q='+v.get()
        webbrowser.open(addr)
        x=v.get()
        listcontext=searchterm(x)
        em(listcontext)
        

    

'''    
def sel():
    print(context.get())
'''

root = Tk()
root.title("MySearch")
root.overrideredirect(1);
root.configure(background='white')

imageFile = "header.gif"
image1 = ImageTk.PhotoImage(Image.open(imageFile))

w=400
h=155

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2) - 7
y = (hs/2) - (h/2) - 2

root.geometry('%dx%d+%d+%d' % (w,h,x,y))

back = Canvas(root, width=400, height=155, bg='black')
back.pack(fill=BOTH)

panel1 = Label(back, image=image1)
panel1.pack(side='top', fill=X, expand='no')

#textFrame = Frame(panel1)

'''
entry = Label(root)
entry["text"] = "Enter the Search Term:  "
entry.pack(side=LEFT,pady=5)
'''

v = StringVar()

search_entry = Entry(back,justify=CENTER,width=65,textvariable=v)
search_entry.pack()
search_entry.focus_set()

#textFrame.pack()
root.bind("<Escape>", exit)

root.bind("<Return>", search)


'''
button1 = Button(root, text="Quit", command=root.destroy)
button1.pack(side=RIGHT)

button = Button(root, text="Search", command=search)
button.pack(side=RIGHT)
context = StringVar()
'''

root.mainloop()
'''
root1 = Tk()
root1.title("MySearch")
root1.overrideredirect(1);
w1=500
h1=200
ws = root1.winfo_screenwidth()
hs = root1.winfo_screenheight()
x = (ws/2) - (w1/2) - 7
y = (hs/2) - (h1/2) - 2
root1.geometry('%dx%d+%d+%d' % (w1,h1,x,y))

label1 = Label(root1, text = "Thank You for using MySearch.\nPlease pick your intended search context\n")
label1.pack()
R1 = Radiobutton(root1, text="Programming", variable=context, value="Programming")
R1.pack(anchor = W)
R2 = Radiobutton(root1, text="Snake", variable=context, value="Snake")
R2.pack(anchor = W)
button2 = Button(root1, text="Submit", command=root1.destroy)
button2.pack(side=RIGHT)
label2 = Label(root1, text = "    ")
label2.pack(side=RIGHT)
root1.mainloop()
'''

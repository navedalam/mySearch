#@Phoenix
#Facebook Crawler

import urllib
import facebook

def check_token(access_token):
    '''Check if the access token given is valid.'''
    
    url="https://graph.facebook.com/me/"
    data={'access_token':access_token}
    data = urllib.urlencode(data)
    try:
        temp=str(url+"?access_token="+access_token)
        response=urllib.urlopen(temp)
        response_page = response.read()
        #print response_page
        response_data=response_page
        #response_data=eval(response_page)
    except IOError:
        print '''Exception occurred while contacting Facebook servers.
        Check your internet connection and login information.'''
        return False
    
    if response_data[:8] == '{"error"':
        print '''Exception occurred while checking the access token given'''
        return False
    
    if response_data[:5] == '{"id"':
        return True
    
    print "Unknown error occurred while checking access token."
    return False

def fb_request(url, access_token):
    '''Request data from URL with access token.'''
    
    data={'access_token':access_token}
    data = urllib.urlencode(data)
    response_page=""
    response_data=""
    
    try:
        temp=str(url+"?access_token="+access_token)
        response=urllib.urlopen(temp)
        response_page = response.read()
    except:
        print "Exception occurred in requesting/reading data from URL:", url
        return
    
    try:
        response_page=response_page.replace("true", "True")
        response_data=eval(response_page)
    except:
        print "Exception occurred in evaluating received data from URL:", url
        print "Data Received -------- \n", response_page, "\n--------"
        return

    if 'data' in response_data.keys():
        return response_data['data']
    
    return response_data 

def get_access_token(verbose=True):

    if verbose:
        print "Searching for saved access token..."

    try:
        #REMOVE!
        #raise IOError
        token_file=open("token.dat", 'r')
        access_token=token_file.read()
        print "Found saved access token."
        token_file.close()
        
        if check_token(access_token) == False:
            if verbose:
                print "The program will attempt to request a new token"
            
            raise IOError            
        
        if verbose:
            print "Access token saved is valid!"
        
        return access_token
    
    except IOError:
        print "Could not find/use saved access token."
        pass

    if verbose:
        print "Attempting to create new login token..."

    fb=facebook.Facebook('090dd0f4c5839154585b8c4677500884','6a405f5ace42dc49eb6f8eb730da8382')

    try:
        fb.auth.createToken()
    except:
        print "Could not get session. This is likely because your internet connection failed."
        exit(0)

    if verbose:
        print "Token created."
        print "Please log in."

    fb.login(popup=True)

    print 'After logging in, press enter...'
    raw_input()

    if verbose:
        print "Logged in."
        print "Getting session..."
        
    try:
        fb.auth.getSession()
    except:
        print "Could not get session. This is likely because your internet connection failed."
        exit(0)
            
    if verbose:
        print 'Session Key:   ', fb.session_key
        print 'Your UID:      ', fb.uid
        print "\nRequesting key exchange..."

    url = 'https://graph.facebook.com/oauth/exchange_sessions'
    values = {'client_id' : '353754194907',
              'client_secret' : '6a405f5ace42dc49eb6f8eb730da8382',
              'sessions' : fb.session_key }

    data = urllib.urlencode(values)
    response = urllib.urlopen(url, data)
    response_page = response.read()
    response_data=eval(response_page)

    if verbose:
        print "Key exchange complete."

    access_token=response_data[0]['access_token']

    if verbose:
        print "Saving access token to disk..."

    try:
        token_file=open("token.dat", 'w')
        token_file.write(access_token)
        print "Saved access token successfully."
        token_file.close()
    
    except:
        print "Could not save access token."
        pass

    print "Access token downloaded successfully!"
    return access_token

def categorize(likes):
    '''Split likes into categories so that they can be appended to the information database, like everything else'''
    
    info={}
    for like in likes:
        if like['category'] in info:
            info[like['category']]=info[like['category']]+[like['name']]
        else:
            info[like['category']]=[like['name']]
    
    return info
        
def getsocialinformation(sources, limit=True):
    '''Get information from the sources specified and return a dictionary with keys as category names and values as the contents'''
    access_token=get_access_token()
    info={}
    if 'likes' in sources:
        likes=fb_request("https://graph.facebook.com/me/likes", access_token)
        info.update(categorize(likes))
    
    personal_data = fb_request("https://graph.facebook.com/me/", access_token)
    #print personal_data
    
    if 'geographic' in sources:
        if 'location' in personal_data.keys():
            temp=personal_data['location']['name']
            info.update({'SPL_Geographic':[temp]})
    
    if 'work' in sources:
        if 'work' in personal_data.keys():
            temp=personal_data['work'][0]['employer']['name']
            info.update({'SPL_Employer':[temp]})
    
    if 'education' in sources:
        if 'education' in personal_data.keys():
            educationdata=[]
            for stage in personal_data['education']:
                temp=stage['school']['name']
                educationdata.append(temp)
                if 'concentration' in stage.keys():
                    temp=stage['concentration'][0]['name']
                    educationdata.append(temp)
            info.update({'SPL_Education':educationdata})
    
    if limit:
        categories=['SPL_Employer', 'Interest', 'Field of Study', 'Company', 'University', 'SPL_Geographic', 'SPL_Education', 'Sport', 'City']
        x={}
        for category in categories:
            if category in info.keys():
                x.update({category:info[category]})
            else:
                x.update({category:[]})
        
        info=x
        
    return info

if __name__ == '__main__':
    sources=['likes', 'geographic', 'education', 'work']
    info=getsocialinformation(sources)
    print "Your social information follows:\n"
    for i in info.keys():
        print i, ":", info[i]

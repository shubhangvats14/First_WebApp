from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'key1':'This text came from the python code'}) # in this way we connect our full html file inplace of just a html statement, render is used because now we have the whole html page and we just have to render it
#here we should check that in our settings.py , in dirc of templates we have the address of templates or not(in older versions it is nor default written) this is done to ensure that our file knows about index.html file

'''
def downloads(request): #called from urls.py to print a line when only the basic domain is given with space following
    return HttpResponse("<h1>Welcome to My  page</h1>") #only we can return a httpresponse(that is we can only give html code) thats why we wrote it and imported it from above library
'''
from . import counter

def result(request):
    '''
    age = request.GET['user_age'] #this request.Get func. is used to retrievw the value of var. user_age reeturned from index.html
    name = request.GET['user_name']
    message = f"Hi..You are {name} and you are {age} years old."
    '''


    #Django Article Analyser
    article = request.GET['article']
    word_count, dict_words = counter.count(article)


    return render(request, 'result.html', {'article': article, 'word_count':word_count, 'dict_words' : dict_words})


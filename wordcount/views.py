from django.http import HttpResponse
from django.shortcuts import render
import operator 

def homepage(request):
    return render(request, "home.html")

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    #Checking for the word that occurs the most
    worddict = {}
    for word in wordlist:
        #if in dictionary increment by 1 
        if word in worddict:
            worddict[word] += 1
        else:
            #If word not in dictionary then add it in 
            worddict[word]= 1
    sorted_words = sorted(worddict.items(), key= operator.itemgetter(1), reverse = True)
        

    return render(request, "count.html", {'fulltext': fulltext, 'count': len(wordlist), 'Sorted_words': sorted_words})

def about(request):
    return render(request, 'about.html')
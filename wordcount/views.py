from django.http import HttpResponse
from django.shortcuts import render
import operator

# homepage
def home(request):
    return render(request, 'home.html')

# process word count form
def count(request):
    fulltext = request.GET['fulltext'] # store the text
    wordsList = fulltext.split() # split words into list
    wordDictionary = {}
    for word in wordsList:
        if word in wordDictionary:
            # increase
            wordDictionary[word] += 1
        else:
            # add to wordDictionary
            wordDictionary[word] = 1
    # sort list of words using their values (itemgetter 1)
    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordsList),'sortedWords':sortedWords})

# about page
def about(request):
    return render(request, 'about.html')

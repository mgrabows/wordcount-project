from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
  return render(request, 'home.html', {'hithere':'This is me'})

def about(request):
  return render(request, 'about.html')

def eggs(request):
  return HttpResponse('Eggs are great!')

def count(request):
  fulltext = request.GET['fulltext']  
  wordlist = fulltext.split()
  
  wordsdict = {}
  for word in wordlist:
    if word in wordsdict:
      wordsdict[word] += 1
    else:
      wordsdict[word] = 1  
  
  sortedwords = sorted(wordsdict.items(), key=operator.itemgetter(1), reverse=True)
  
  return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
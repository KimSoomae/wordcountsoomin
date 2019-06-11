from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    words_dictionary = {}
    for word in words:
        if word in words_dictionary.keys():
            words_dictionary[word] +=1
        else:
            words_dictionary[word] = 1

    return render(request,"result.html", {'count':len(words),'text':text, 'countlist': words_dictionary.items()})
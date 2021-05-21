#I have created this file--khushboo
from django.http import HttpResponse
from django.shortcuts import render

djtext=''
def index(request):
    return render(request,'index.html',{ djtext : 'djtext'})

def about(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contactus.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    params={ }

    removepunc = request.POST.get('removepunc')
    captilize = request.POST.get('captilize')
    newlineremover = request.POST.get('newlineremover')
    spaceremover = request.POST.get('spaceremover')
    swapcase = request.POST.get('swapcase')

    if djtext=="" or djtext==" ":
        return HttpResponse("Please Enter some text to analyze")

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Analyzed Text: ', 'analyzed_text': analyzed}
        djtext = analyzed

    if(captilize=="on"):
        analyzed = ""
        analyzed=djtext.upper()

        params = {'purpose': 'Analyzed Text: ', 'analyzed_text': analyzed}
        djtext = analyzed

    if(spaceremover=="on"):
        analyzed = ""
        analyzed=djtext.replace(' ','')
        params = {'purpose': 'Analyzed Text: ', 'analyzed_text': analyzed}
        djtext = analyzed

    if (swapcase == "on"):
        analyzed = ""
        analyzed=djtext.swapcase()
        params = {'purpose': 'Analyzed Text: ', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Analyzed Text:  ', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover != "on" and spaceremover != "on" and captilize != "on" and swapcase!="on") :
        return HttpResponse("please select any operation and try again")
    return render(request, 'analyze.html', params)








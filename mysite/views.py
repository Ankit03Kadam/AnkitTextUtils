# I have created this file - ANkit KAdam
#lec_1:views and urls
#lec_2:personal navigator using HttpResponse,Html(achor tag,list tag)
#lec_3:Laying the pipline creating multiple pages and connecting to Home page
#lec_4:Creating template for using html externally by importing templates
#lec_5:creating frontend of website that remove punctuations using html forms get text from user and print it on remove punc
#lec_6:creating backend of website that remove punctuations
#lec_7(12):DJango Exercise 1  solution + shortcuts
#lec_8(13):adding more features to TextUtils
#lec
#lec
#lec
#lec
#lec
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings




def index(request):
    return render(request, 'index.html')
    
def analyze(request):
    
    djtext=request.POST.get('text','default')
    removepunch=request.POST.get('removepunc','default')
    uppercaps=request.POST.get('uppercaps','default')
    newlineremove=request.POST.get('newlineremove','default')
    extraspaceremove=request.POST.get('extraspaceremove','default')
    charcount=request.POST.get('charcount','default')
    punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
   
    
    
    if removepunch=="on":
      
      analyzed=''
      for char in djtext :
          if char not in punctuation or char == '\n':
              analyzed=analyzed+char
      params={'purpose':'Removed Punctions','analyzed_text':analyzed}
      djtext=analyzed
      
    
    if uppercaps=='on':
      
      analyzed=''
      for char in djtext:
        analyzed=analyzed+char.upper()
      params={'purpose':'Changed to uppercase','analyzed_text':analyzed}
      djtext=analyzed
      
    
    if newlineremove=='on':
      analyzed=''
      for char in djtext:
        if char!="\n" and char!="\r":
         analyzed=analyzed+char 
      params={'purpose':'Remove new line','analyzed_text':analyzed}
      djtext=analyzed
     
    
    if extraspaceremove=='on':
      analyzed=''
      for index,char in enumerate(djtext):
        if not (djtext[index] ==" " and djtext[index+1]==" "):
         analyzed=analyzed+char
      params={'purpose':'Remove Extra Space','analyzed_text':analyzed}
      djtext=analyzed
     
    
    '''if charcount=='on':
      analyzed=''
      count=0
      for char in djtext:
        if (char!=" " and char!="\n" and char not in punctuation):
         count=count+1
      params1={'purpose1':'Count number of Character','analyzed_text1': count ,'caption':'The number of charater in given text is = '}
      #djtext=analyzed
      #return render(request,'analyze.html',params)'''
    
    if(removepunch != "on" and uppercaps!='on' and newlineremove!='on' and extraspaceremove!='on' and charcount!='on'):
      return HttpResponse("Error")
    
    return render(request,'analyze.html',params)
   
    
def contact(request):
    return render(request,'contactus.html')
  
def about(request):
    return render(request,'aboutus.html')
  

  
       



    

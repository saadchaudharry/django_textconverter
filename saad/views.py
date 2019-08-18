from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def analyzed(request):
    djr=request.GET.get('text','Default')
    print(djr)
    remve=request.GET.get('remve','off')
    upper=request.GET.get('upper','off')
    count=request.GET.get('count','off')
    space=request.GET.get('spac','off')

    if remve=='on':
        punc = '''@#$%^&*_-"':<>'''
        anall=""
        for char in djr:
            if char not in punc:
                anall=anall+char
        dic={'baja':'remove punctuation','anal':anall}
        return render(request,'analyzer.html',dic)

    elif upper=='on':
        uppper=""
        for item in djr:
            uppper=djr.upper()
        dicc={'souf':uppper}
        return render(request,'upper.html',dicc)

    elif count=='on':
        # for char in djr:
        countt=len(djr)
        DIC={'soufF':countt}
        return render(request,'char.html',DIC)
    # elif space=='on':
    #     print(djr,end="")
    #     vic={'spaac':djr}
    #     return render(request,'spac.html',vic)

    elif space=='on':
        laal = ""
        for item in djr:
            if item !="\n":
                laal = laal+item
        vic={'spaac':laal}
        return render(request,'spac.html',vic)


    else:
        return HttpResponse('<h1 style{color:blue;font-size:50px}>Error</h1>')


    # djr = request.GET.get('text', 'default')
    # remve=request.GET.get('remve','off')
    # print(djr)
    # print(remve)
    # if remve=='on':
    #     anall=""
    #     punc='''@#$%^&*_-"':<>'''
    #     for char in djr:
    #          if char not in punc:
    #              anall=anall+char
    #              dic = {'baja': 'remove punctutaion', 'anal': anall}
    #     return render(request,'analyzer.html',dic)
    # else:
    #     return HttpResponse('Error')

#if removepunc == "on":
    #     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #     analyzed = ""
    #     for char in djtext:
    #         if char not in punctuations:
    #             analyzed = analyzed + char
    #     params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
    #     return render(request, 'analyze.html', params)
    #
    # else:
    #     return HttpResponse("Error")

# def Newline(request):
#     return HttpResponse("Newline <a href='http://127.0.0.1:8000'> back </a>")
#
#
# def SpaceRemove(request):
#     return HttpResponse("SpaceRemove <a href='http://127.0.0.1:8000'> back </a>")
#
#
# def captilize(request):
#     return HttpResponse("captilize <a href='http:s//127.0.0.1:8000'> back </a>")
#
#
# def charcout(request):
#     return HttpResponse("charcout <a href='http://127.0.0.1:8000'> back </a>")

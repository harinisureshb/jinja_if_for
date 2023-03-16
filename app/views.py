from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':106}
    return render(request,'conditional.html',d)
def ifelse(request):
    d={'a':100,'b':200}
    return render(request,'ifelse.html',d)
def elifconditon(request):
    d={'a':100,'b':500,'c':200}
    return render(request,'elif.html',d)
def nestedif(request):
    d={'a':100,'b':300,'c':400}
    return render(request,'nestedif.html',d)
def forloop(request):
    d={'name':'harini'}
    return render(request,'forloop.html',d)
from django.shortcuts import render
from django.http import HttpResponse

data=[
        {'id': 1, 'name': 'os'},
        {'id': 2, 'name': 'IOT'},
        {'id': 3, 'name': 'React'}
    ]


# Create your views here.

def hello(request):
    return render(request,'Home.html')
    
def home(req):
    return render(req,'Home.html')

def alltracks(req):
    context={'data':data}
    return render(req,'Tracks.html',context)

def mytrack(request,id):
    print('okok')
    trackinfo=list(filter(lambda t:t['id']==id,data))
    if(trackinfo):
        context={'trackdata':trackinfo[0]}
        return render(request,'TrackDetails.html',context)
    else:
        return HttpResponse(f'<h1> track not found</h1>')

def about(req):
    return render(req,'About.html')

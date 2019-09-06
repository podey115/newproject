from django.shortcuts import HttpResponse,render
def home(request):
    context={
        'c':10,
        'a':[1,2,3,4,5,6,7]
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')

def signup(request):
    return render(request,'signup.html')
def signin(request):
    return  render(request,'login.html')
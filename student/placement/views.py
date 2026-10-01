from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
import joblib
from django.urls import reverse
from placement.models import Student

def home(req):
    return render(req,'home.html')

def register(r):
    return render(r,'register.html')

def registerForm(r):
    s1 = Student()
    s = Student.objects.filter(si=r.POST['si'])
    if not s:
        s1.si = r.POST['si']
        s1.sn = r.POST['sn']
        s1.sp = r.POST['sp']
        s1.se = r.POST['se']
        s1.save()
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(r,'register.html',{'errormsg':"Student already exists"})
    

def login(r):
    return render(r,'login.html')

def loginForm(r):
    try:
        s1=Student.objects.get(si=r.POST['si'],sp=r.POST['sp'])
        r.session['si']=s1.si
        r.session['sp']=s1.sp
        return HttpResponseRedirect(reverse('dashboard'))
    except Student.DoesNotExist:
        return render(r,'login.html',{'erg':"Invalid Student Name or Password"})
    
def result(r):
    return render(r,'result.html')
    
def dashboard(r):
    return render(r,'dashboard.html')



def predict(request):
    scaler = joblib.load('scalermodel.pkl')
    mlmodel = joblib.load('mlmodel.pkl')

    iq = float(request.POST['iq'])
    cgpa = float(request.POST['cgpa'])
    profile = int(request.POST['profile'])
    
    lis = [iq, cgpa, profile]

    # Scale input
    scaled_input = scaler.transform([lis])

    # Prediction
    ans = mlmodel.predict(scaled_input)

    # Convert prediction into readable result
    if ans[0] == 1:
        result = "Eligible for Placement"
        message = "Based on the provided information, you are predicted to be eligible for placement."
    else:
        result = "Not Eligible for Placement"
        message = "Based on the provided information, you are predicted to be not eligible for placement."

    # Send result to result.html
    return render(
        request,
        'result.html',
        {
            'result': result,
            'message': message,
            'iq': iq,
            'cgpa': cgpa,
            'profile': profile
        }
    )

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('login'))
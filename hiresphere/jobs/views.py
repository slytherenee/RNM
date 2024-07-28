from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Company
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import CompanySignUpForm, UserSignUpForm

def index(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/hack2.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

def create_job(request):
    if request.method == 'POST':
        # Add logic to handle job creation form submission
        return HttpResponse("Job created")
    return render(request, 'jobs/create_job.html')

def sign_up(request):
    return render(request, 'jobs/signup.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        account_type = request.POST['account_type']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            if account_type == 'user':
                return redirect('user_dashboard')  # replace 'user_dashboard' with your user dashboard URL name
            elif account_type == 'company':
                return redirect('company_dashboard')  # replace 'company_dashboard' with your company dashboard URL name
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request, 'jobs/login.html') 

def sign_up(request):
    if request.method == 'POST':
        account_type = request.POST.get('account_type')
        
        if account_type == 'company':
            form = CompanySignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')  # Change to your home page URL
                
        else:
            form = UserSignUpForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')  # Change to your home page URL

    else:
        form = UserSignUpForm()  # Default to user form

    return render(request, 'jobs/signup.html', {
        'form': form,
    })
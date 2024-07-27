from django.shortcuts import render, get_object_or_404
from .models import Job, Company
from django.http import HttpResponse

def job_list(request):
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

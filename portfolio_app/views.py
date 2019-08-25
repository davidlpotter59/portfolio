from django.shortcuts import render, get_object_or_404
from .models import Job
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    jobs = Job.objects
    context = {
        'jobs':jobs,
    }
    return render(request, 'portfolio_app/home.html', context)

def detail(request, job_id):
    # print("My job number is {}".format(job_id))
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'portfolio_app/detail.html', {'job': job_detail})

@login_required
def dave(request):
    return render(request, 'portfolio_app/dave.html')
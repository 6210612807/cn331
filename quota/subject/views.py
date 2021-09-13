from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import Subject

def index (request):
    data = Subject.objects.all()
    return render(request, "subject/index.html", {
        'subjects': data
    })
    
def course (request,subject_id):
    subject = get_object_or_404(Subject,pk=subject_id)
    return render(request, "subject/subject.html",{
        "subject":subject
    })
    
import os

# from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.template import loader



from Newbie.models import Allcourses, details

current_path = os.path.realpath('.')

def courses(request):
    ac=Allcourses.objects.all()
    # view_path = current_path + '/Newbie/templates/Newbie/courses.html'
    #img_path = r'/Newbie/templates/img/my-passport-photo.jpg'
    context = {
        'ac': ac,
        #'imgsrc' : img_path
    }
    template = loader.get_template('newbie_templates/courses.html')
    return HttpResponse(template.render(context, request))
    # return render(request, 'newbie_templates/courses.html', context)

def details(request,course_id):
    course=get_object_or_404(Allcourses, pk = course_id)
    return render(request, 'newbie_templates/details.html', {'course': course})



def your_choice(request, course_id):
    course = get_object_or_404(Allcourses, pk = course_id)
    try:
        selected_ct = course.details_set.get(pk = request.POST['choice'])
    except(KeyError, Allcourses.DoesNotExist):
        return render(request, '/newbie_templates/details.html', {
            'course':course,
            'error message':"Select a valid Option"
        })
    else:
        selected_ct.your_choice = True
        selected_ct.save()
        return render(request, 'newbie_templates/details.html', {'course': course})
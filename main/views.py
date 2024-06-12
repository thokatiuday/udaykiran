from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from . import models
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def education(request):
    template = loader.get_template('education.html')
    data = {
        'courses' : [
            {'name' : 'Samskruthi eng. College','course' : 'B Tech (Data science) (2021-2025)','percentage' : '7.0',},
            {'name' : 'SriSandepani jr. college','course' : 'Intermediate (2019-2021)','percentage' : '6.5',},
            {'name' : 'Kanthi high school','course' : 'SSC (2009-2019)','percentage' : '9.8',},
        ]
    }
    return HttpResponse(template.render(data,request))

def learning(request):
    template = loader.get_template('learning.html')
    learning = models.learning_path.objects.all()[::-1]
    data = {
        'learnings' : learning,
    }
    return HttpResponse(template.render(data,request))

def projects(request):
    template = loader.get_template('projects.html')
    project = models.project.objects.all()[::-1]
    data = {
        'projects' : project,
        }
    return HttpResponse(template.render(data,request))

def project(request,project_name):
    template = loader.get_template('project.html')
    project_details = models.project.objects.get(project_id=project_name)
    skills = models.project_skills.objects.filter(project_id = project_details).all()
    points = models.project_points.objects.filter(project_id = project_details).all()
    data = {'project' : project_details,
            'skills' : skills,
            'points' : points,
        }
    try:
        media = models.project_media.objects.get(project_id = project_details)
        data['image'] = media
    except:
        media = ""
    return HttpResponse(template.render(data,request))

def resume(request):
    template = loader.get_template('resume.html')
    return HttpResponse(template.render())

def skills(request):
    template = loader.get_template('skills.html')
    data = {
        'skills' : [
                    'py','django',
                    'html','css','js','bootstrap',
                    'git','github','githubactions',
                    'mysql','postgres','sqlite','mongodb',
                    'opencv','pandas','numpy','pytorch',
                    'php','c','cpp','java',
                    'docker','aws',
                    'react',
                    'vercel','netlify',
                ],
        'soft_skills' : [
                    'speaking english',
                    'Teamwork',
                    'Dedication',
                ]
    }
    return HttpResponse(template.render(data,request))

def social(request):
    template = loader.get_template('social.html')
    social = models.social_links.objects.all()
    data = {
        'social' : social,
    }
    return HttpResponse(template.render(data,request))
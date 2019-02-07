from django.shortcuts import render
from django.views.generic import View
from .models import Upload
from django.http import HttpResponsePermanentRedirect,HttpResponse
import random
import string
import json
import datetime


class HomeView(View):
    def get(self,request):
        print("get request come")
        return render(request,"base.html",{})

    def post(self,request):
        print("post request come")
        if request.FILES:
            file = request.FILES.get("file")
            name = file.name
            size = int(file.size)
            with open('static/file/'+name,'wb')as f :
                f.write(file.read())
            code = ''.join(random.sample(string.digits, 8))
            from django.utils import timezone
            u = Upload(
                path = 'static/file/'+name,
                name=name,
                Filesize=size,
                code = code,
                PCIP=str(request.META['REMOTE_ADDR']),
                Datatime=timezone.now(),
            )
            print("u values="+str(type(u)))
            print("timezone.now="+str(timezone.now()))
            u.save()
            return HttpResponsePermanentRedirect("/s/"+code+"/")


class DisplayView(View):
    def get(self,request,code):
        u = Upload.objects.filter(code=str(code))
        if u :
            for i in u :
                i.DownloadDocount +=1
                i.save()
        return render(request,'content.html',{"content":u})


class DisplayView_detail(View):
    def get(self,request,code):
        u = Upload.objects.filter(code=str(code))
        if u :
            return render(request,'content_detail.html',{"content":u})
        else:
            print("code is not exist,ERROR")


class MyView(View):
    def get(self,request):
        IP = request.META['REMOTE_ADDR']
        u = Upload.objects.filter(PCIP=str(IP))
        for i in u :
            i.DownloadDocount +=1
            i.save()
        return render(request,'content.html',{"content":u})


class SearchView(View):
    def get(self,request):
        code = request.GET.get("kw")
        print("code="+str(code))
        u = Upload.objects.filter(name=str(code))
        print("len(u)"+str(len(u)))
        data = {}
        if u :
            for i in range(len(u)):
                u[i].DownloadDocount +=1
                u[i].save()
                data[i]={}
                data[i]['download'] = u[i].DownloadDocount
                data[i]['filename'] = u[i].name
                data[i]['id'] = u[i].id
                data[i]['ip'] = str(u[i].PCIP)
                data[i]['size'] = u[i].Filesize
                data[i]['time'] = str(u[i].Datatime.strftime('%Y-%m-%d %H:%M:%S'))
                data[i]['key'] = u[i].code
        return HttpResponse(json.dumps(data),content_type="application/json")

class delete_file(View):
    def get(self, request,code):
        print("code="+str(code))
        IP = request.META['REMOTE_ADDR']
        u = Upload.objects.filter(PCIP=str(IP))
        for i in u:
            i.DownloadDocount += 1
            i.save()
        return render(request, 'content.html', {"content": u})


# Create your views here.

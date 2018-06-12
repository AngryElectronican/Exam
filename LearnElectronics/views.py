from django.shortcuts import render
from django.http import JsonResponse
from .models import User_model
# Create your views here.

def Registration(request):
    if(request.method=="GET"):
        nick=request.GET["nick"]
        #print("First")
        if(User_model.objects.first()):#if db exsists
                if(User_model.objects.filter(user=nick).exists()):
                    #print("Second")
                    return JsonResponse({"msg":"ERROR"})
                else:
                    #print("Third")
                    last_id=User_model.objects.last().id
                    user_obj=User_model.objects.create(user=nick,id=last_id+1)
                    return JsonResponse({"msg":user_obj.id})
        else:
            #print("Four")
            user_obj=User_model.objects.create(user=nick,id=1)
            #user_obj.save()
            return JsonResponse({"msg":user_obj.id})

    #print("Five")
    return JsonResponse({"msg":"NOT GET REQUEST OR INTERNAL ERROR"})

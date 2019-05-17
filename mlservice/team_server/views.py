from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import sys
import os

# Create your views here.
from django.http import HttpResponse
from django.template import loader 

def index(request):
    return HttpResponse("Hello! World ")


current_path = os.path.dirname( os.path.abspath( __file__ ) )#team_server
print( current_path )
mlservice_path = os.path.abspath(os.path.join(current_path, os.pardir))
print( mlservice_path )
web_start_path = os.path.abspath(os.path.join(mlservice_path, os.pardir))
print( web_start_path )
video_module_path=os.path.join(web_start_path, 'VideoModule')
print( video_module_path )
sys.path.append(video_module_path)

'''
#add path of video_module's codes
video_module_path=os.path.join(os.path.dirname( os.path.abspath( __file__ ) ), 'code')
video_module_path=os.path.join(video_module_path, 'VideoModule')
sys.path.append(video_module_path)
'''
#videos_path = os.path.join(video_module_path, 'videos')
#sys.path.append(videos_path)

#CNN_model_path=os.path.join(video_module_path, 'models')
#sys.path.append(CNN_model_path)

#detection_model_path = os.path.join(video_module_path, 'haarcascade_files')
#detection_model_path = os.path.join(detection_model_path, 'FaceDetect')
#sys.path.append(detection_model_path)

#print(sys.path)
#for each in sys.path:
#    print(each)


def test_form(request):
    template = loader.get_template('team_server/test_form.html')
    #template = loader.get_template('team_server/index.php')
    #template = loader.get_template('team_server/test.php')
    context = {
    #    'index_test': ['Index Testing Page', 'Is it working?'],
    }
    return HttpResponse(template.render(context, request))



def test_form2(request):
    template = loader.get_template('team_server/shiyan.html')
    context = {
    #    'index_test': ['Index Testing Page', 'Is it working?'],
    }
    return HttpResponse(template.render(context, request))

def webcam(request):
    return render(request, 'team_server/webcam.html')

@csrf_exempt
def sending(request):
    if request.method == 'POST': # If the form has been submitted
        print(request.POST)
        '''
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # 

            print (form.cleaned_data['video'])

        else:
            print("here1")
        '''
    else:
        print("here2")
    context = {}#return format : {'pred_str':pred_str}
    return HttpResponse(json.dumps(context), "application/json")



    '''
    print('@@@@@@@@sending is called@@@@@@@@@@@@@@@@@@@@@')
    #data = request.POST
    print(request.POST)
    context = {}#return format : {'pred_str':pred_str}
    return HttpResponse(json.dumps(context), "application/json")
    '''


#from Commander import Commander
#global commander
#commander = Commander()

@csrf_exempt
def video_face_analysis(request):
    from Commander import Commander
    commander = Commander()
    print("Button has been pushed!!! service start from here")
    data = request.POST['msg']
    #commander.mainLogic(data)
    commander.secondLogic(data)
    context = {}#return format : {'pred_str':pred_str}
    return HttpResponse(json.dumps(context), "application/json")






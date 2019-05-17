
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
from django.http import HttpResponse
from django.template import loader 

def index(request):
    template = loader.get_template('numberOracle/index.html')
    
    context = {
        'index_test': ['Index Testing Page', 'Is it working?'],
    }
    
    return HttpResponse(template.render(context, request))


@csrf_exempt
def oracle_handwritten(request):
    template = loader.get_template('numberOracle/oracle_handwritten.html')
    context = {'test_message_list': ['hello, there?', 'my name is Hong.', 'How are you, today?'],}

    #import pickle

    #model_filename = 'mnist_model.pkl'
    #model_filename = '/home/vagrant/shared/lab11/mlservice/static/mnist_model.pkl'
    # Load model from file
    #global mnist_model
    #with open(model_filename, 'rb') as file:
    #    mnist_model = pickle.load(file)





    return HttpResponse(template.render(context,request))


def ajaxform(request):
    template = loader.get_template('numberOracle/test_form.html')
    context = {'test_message_list': ['hello, there?', 'my name is Hong.', 'How are you, today?'],}
    return HttpResponse(template.render(context,request))








'''
import pickle
model_filename = '/home/vagrant/shared/lab11/mlservice/static/mnist_model.pkl'
#Load model from file
#global mnist_model
with open(model_filename, 'rb') as file:
    mnist_model = pickle.load(file)
'''






def testAI(pic):
    import numpy as np
    #pic = pic_list[0]

    

    
    import pickle

    #model_filename = 'mnist_model.pkl'
    model_filename = '/home/vagrant/shared/lab11/mlservice/static/mnist_model.pkl'


    # Load model from file
    print('bad&&&&&&&&&&&&&&&&&&&&&&&&&&')
    with open(model_filename, 'rb') as file:
        mnist_model = pickle.load(file)
    print('good@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(np.shape(pic))
    pred = mnist_model.predict_classes(pic.reshape((1, 28, 28, 1)))
    print('pred: ',pred)   
    ''''''

    from keras import backend as K
    #K.clear_session()


    del mnist_model
    K.clear_session()
    import gc
    #mnist_model.clear_session()
    gc.collect()
    #print(mnist_model)
    





#import pickle

#model_filename = 'mnist_model.pkl'
#model_filename = '/home/vagrant/shared/lab11/mlservice/static/mnist_model.pkl'
# Load model from file
#global mnist_model
#with open(model_filename, 'rb') as file:
#    mnist_model = pickle.load(file)


@csrf_exempt
def oracleNumber(request):
    import numpy as np
    from PIL import Image

    data = request.POST['msg']
    pixel = data.split('/')[:-1]

    #print(len(data))

    pixel_list = []

    for i in range(280):
        tmp_list = []
        for j in range(280):
            tmp_list.append(int(pixel[i*280 + j]))#maybe wrong
        pixel_list.append(tmp_list)


    resized_pixel_list = []
    for i in range(0, 280, 10):
        tmp_list = []
        for j in range(0,280, 10):
            avg = 0
            for k in range(10):
                for l in range(10):
                    avg +=  pixel_list[i+k][j+l]
            avg /= 100
            #if avg != 255:
            #    avg=0
            #else:
            #    avg=255
            #else:
            #    avg= 0
            tmp_list.append(avg)
        resized_pixel_list.append(tmp_list)

    #print(resized_pixel_list)
    #print(len(resized_pixel_list[0]))
    #print(len(resized_pixel_list))

    #pic = np.array(resized_pixel_list).astype('uint8')
    pic = np.array(resized_pixel_list)/255

    #pic_img = Image.fromarray(pic)

    #pic_img.save("result.png","PNG")

    #pic_img = pic_img.resize((28,28))

    #import os.path
    #BASE = os.path.dirname(os.path.abspath(__file__))

    #data = open(os.path.join(BASE, "mnist_model.pkl"))

    ''''''
    import pickle

    #model_filename = 'mnist_model.pkl'
    model_filename = '/home/vagrant/shared/lab11/mlservice/static/mnist_model.pkl'
    # Load model from file
    with open(model_filename, 'rb') as file:
        mnist_model = pickle.load(file)

    pred = mnist_model.predict_classes(pic.reshape((1, 28, 28, 1)))
    print(pred)
    
    from keras import backend as K

    K.clear_session()
    del mnist_model
    import gc
    #mnist_model.clear_session()
    gc.collect()
    #print(mnist_model)


    
    #testAI([pic])

    
    #pred = mnist_model.predict_classes(pic.reshape((1, 28, 28, 1)))
    #print(pred)
    #pred = 1# dummy
    #print(mnist_model)
    #print('good') 


    ''''''
    #import threading
    #t = threading.Thread(target=testAI, args=([pic]))
    #t.start()



    #pred = 1#dummy
    
    context = {'returned': str(pred),}
    return HttpResponse(json.dumps(context), "application/json")












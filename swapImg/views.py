from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *

import cv2
import matplotlib
matplotlib.use('Agg')  # Specify the Agg backend - this line resolves the error
import matplotlib.pyplot as plt
import insightface
from insightface.app import FaceAnalysis
from django.views.decorators.csrf import csrf_exempt


import torch 
from PIL import Image

import os
import dlib
import collections
from typing import Union, List
import numpy as np

import matplotlib.pyplot as plt

import PIL.Image
import PIL.ImageFile

import scipy.ndimage

import requests
from io import BytesIO



def avatarView(request):
  if request.method == 'POST':
    form = UserInfoForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/listing')
  else:
    form = UserInfoForm()
  return render(request, 'UserInfoForm.html', {'form' : form})
  
  
def uploadok(request):
  return HttpResponse(' upload successful')



def DisplayRegisteredUser(request,plot_after=True):    
  if request.method == 'GET':
    User = UserInfo.objects.all().order_by('-id')[:1]
    
    swapper = insightface.model_zoo.get_model('./media/modals/inswapper_128.onnx',download=False, download_zip=False)
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0)
  
    img1 = cv2.imread("./media/"+str(User[0].userAnimeAvatar))
    img2 = cv2.imread("./media/"+str(User[0].userAvatar)) 
    
    # Do the swap
    face1 = app.get(img1)[0]
    face2 = app.get(img2)[0]
    
    img1_ = img1.copy()
    img2_ = img2.copy()

    if plot_after:
      img1 = swapper.get(img1_, face1, face2, paste_back=True)
      img2 = swapper.get(img2_, face2, face1, paste_back=True)
      fig, axs = plt.subplots(1, 2, figsize=(10, 5))
      axs[0].imshow(img1_[:,:,::-1])
      axs[0].axis('off')
      axs[1].imshow(img2[:,:,::-1])
      axs[1].axis('off')
      cv2.imwrite("./media/output/change.png", img1)

    return render(request, 'UserInfoList.html',{'UserInfoDetail': img2_})
  

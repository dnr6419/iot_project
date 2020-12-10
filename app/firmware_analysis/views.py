from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, View
from django.views.generic.edit import FormView
from django.core.files.storage import FileSystemStorage
from .forms import UploadFirmwareForm
from .utils import *


# / , main page
class MainTV(TemplateView):
  template_name = 'base/main.html'
  def get(self, request, *args, **kwargs):
    ctx = {'message':'Hello123'}
    return self.render_to_response(ctx)

class FileUploadFV(View):
  form_class = UploadFirmwareForm
  template_name = "firm/upload.html"
  success_url = '/upload_success'
  def get(self, request, *args, **kwargs):
    form = self.form_class()
    return render(request, self.template_name, {'form': form})
  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST, request.FILES)
    
    if form.is_valid():
      firmware = request.FILES['firmware']
      fs = FileSystemStorage()
      fs.save(firmware.name, firmware)
      file_hash=Hash256(firmware)
      return HttpResponse(file_hash) #redirect(self.success_url)
    else:
      form = UploadFirmwareForm()
      return render(request, template_name, {'form': form})

      
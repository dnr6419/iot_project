from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, View
from django.views.generic.edit import FormView
from django.db import connection
from net_scan.models import *
from .forms import s_r_form

# Create your views here.

class MainTV(TemplateView):
  template_name = 'net_scan/main.html'
  def get(self, request, *args, **kwargs):
    #t_r(ip = '192.168.123.101',port = 8080,device='test').save()
    ctx = {'message':'this is test'}
    return self.render_to_response(ctx)

class listLV(ListView):
  template_name = 'net_scan/main.html'
  context_object_name = 'scans'
  model = t_r

class setLV(FormView):
  template_name = 'net_scan/settings.html'
  #context_object_name = 'scans'
  form_class = s_r_form
  # model = s_r
  success_url = '/scan/success'
#  def form_valid(self,form):
#    s_r_form.updateDB(self.requestrequest)
#    return super().form_valid(form)
  


#    
#    if form.is_valid():
#      firmware = request.FILES['firmware']
#      fs = FileSystemStorage()
#      fs.save(firmware.name, firmware)
#      file_hash=Hash256(firmware)
#      return HttpResponse(file_hash) #redirect(self.success_url)
#    else:
#      form = UploadFirmwareForm()
#      return render(request, template_name, {'form': form})
#


    
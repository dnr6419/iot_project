from django import forms
from net_scan.models import s_r
 
class s_r_form(forms.ModelForm):
    class Meta:
        model = s_r
        fields = ['setting_ip_band', 'setting_port_band','setting_option']
    #def updateDB(request):
    #    if request.method == 'POST':
    #        form = NameForm(request.POST)

        

# """
#    setting_ip_band = models.CharField(max_length= 30)
#    setting_port_band = models.CharField(max_length= 30)
#    setting_option = models.CharField(max_length= 30)
#
#"""
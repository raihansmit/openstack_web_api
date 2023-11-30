from django import forms
from openstack.models import instance

class instanceForm(forms.ModelForm):
    class Meta:
        model = instance
        fields = '__all__'

class instanceFormMahasiswa(forms.ModelForm):
    class Meta:
        model = instance
        fields = ['name', 'fk_flavor','fk_images', 'tujuan']
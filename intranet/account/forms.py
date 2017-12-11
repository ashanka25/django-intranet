from django.forms import ModelForm
from .models import Employee, Skill, Role, Document
from django.core.files.images import get_image_dimensions
from django import forms


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['user','employee_id','date_of_birth','date_of_joining','role','pan_number','bank_account_number','emergency_contact_number','project','skill']


class ProfileImageViewMF(ModelForm):
    class Meta:
        model = Employee
        fields = ['image']

class ProfileImageForm(forms.Form):
    image = forms.FileField(label='Select a profile Image')
    

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['docfile','description']

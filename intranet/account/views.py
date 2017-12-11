from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django.db.models import Count
from .models import Employee, Project, Skill, ProfileImage, Role, Document, Report
from .forms import  ProfileImageForm, ProfileImageViewMF, DocumentForm
from graphos.sources.model import ModelDataSource
from graphos.renderers import gchart

class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = ['user',
              'date_of_birth',
              'pan_number',
              'bank_account_number',
              'emergency_contact_number',
              'project',
              'skill',
             ]

    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect_to_login(request.get_full_path())
        return super(EmployeeUpdate, self).dispatch(
            request, *args, **kwargs)

class EmployeeDetail(DetailView):
    model = Employee

class EmployeeHome(LoginRequiredMixin, DetailView):
    model = Employee

    def get_object(self, queryset=None):
        return self.request.user.employee

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'description']

class ProjectList(ListView):
    model = Project

class DocumentCreate(LoginRequiredMixin, CreateView):
    model = Document
    fields = ['docfile', 'description']
    
class DocumentList(ListView):
    model = Document

class SkillCreate(LoginRequiredMixin, CreateView):
    model = Skill 
    fields = ['name']

class SkillList(ListView):
    model = Skill 

class RoleCreate(LoginRequiredMixin, CreateView):
    model = Role
    field = ['name']

class RoleList(ListView):
    model = Role

class ProfileImageView(FormView):
    template_name = 'account/profile_image_form.html'
    form_class = ProfileImageForm

    def form_valid(self, form):
        profile_image = ProfileImage(
            image=self.get_form_kwargs().get('files')['image'])
        profile_image.save()
        self.id = profile_image.id
        return HttpResponseRedirect('.')

    def show_files(request):
        objects = MyModel.objects.all()
        return render_to_response('show_files.html', {'objects': objects},context_instance=RequestContext(request))

def model_form_upload(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileImageViewMF(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('account:home')
    else:
        form = ProfileImageViewMF(instance=employee)
    return render(request, 'account/profile_image_form.html', {'form': form, 'employee': employee})


     
def doc_form_upload(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('account:home')
    else:
        form = DocumentForm(instance=employee)
    return render(request, 'account/document_upload_form.html', { 'form': form, 'employee':employee})

class ReportList(ListView):
    model = Report

def report_list(request):
    return render_to_response('account/report_list.html')

def role_report(request):
    print("ROLE")
    queryset = Employee.objects.all().values('role__name').annotate(total=Count('role')).order_by('total')
    data_source = ModelDataSource(queryset,fields=['role__name','total'])
    chart = gchart.PieChart(data_source)
    return render_to_response('account/graph.html', {"chart": chart})

def skill_report(request):
    queryset = Employee.objects.all().values('skill__name').annotate(total=Count('skill')).order_by('total')
    data_source = ModelDataSource(queryset,fields=['skill__name','total'])
    chart = gchart.PieChart(data_source)
    return render_to_response('account/graph.html', {"chart": chart})
 
def project_report(request):
    queryset = Employee.objects.all().values('project__name').annotate(total=Count('project')).order_by('total')
    data_source = ModelDataSource(queryset,fields=['project__name','total'])
    chart = gchart.PieChart(data_source)
    return render_to_response('account/graph.html', {"chart": chart})

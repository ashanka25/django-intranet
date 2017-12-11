from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from account import views
from .views import EmployeeUpdate, EmployeeDetail, ProjectCreate, ProjectList, SkillList, SkillCreate, ProfileImageView, RoleCreate, RoleList, DocumentList, DocumentCreate, \
        EmployeeHome, ReportList

app_name = 'account'

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'account/login.html'}, name='login'),
    #url(r'^$', TemplateView.as_view(template_name='account/home.html'), name='home'),
    url(r'^$', EmployeeHome.as_view(), name='home'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'account/logged_out.html'}, name='logout'),
    url(r'^password_reset/$', auth_views.password_reset, {'post_reset_redirect':'account:password_reset_done',
                                                    'from_email':'it@broadcom.com',
                                                    }, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'employee/(?P<pk>[0-9]+)/$', EmployeeUpdate.as_view(), name='employee-update'),
    url(r'employee/info/(?P<pk>[0-9]+)/$', EmployeeDetail.as_view(), name='employee-detail'),

    url(r'project/$', ProjectList.as_view(), name='project-list'),
    url(r'project/add/$', ProjectCreate.as_view(), name='project-create'),

    url(r'skill/$', SkillList.as_view(), name='skill-list'),
    url(r'skill/add/$', SkillCreate.as_view(), name='skill-create'),

    url(r'role/$', RoleList.as_view(), name='role-list'),
    url(r'role/add/$', RoleCreate.as_view(), name='role-create'),   

    url(r'^upload/', ProfileImageView.as_view(), name='profile-image-upload'),
    url(r'^uploadmf/(?P<pk>[0-9]+)/$', views.model_form_upload, name='model_form_upload'),
    
    url(r'^document/(?P<pk>[0-9]+)/$',views.doc_form_upload, name='doc_form_upload'), 

    #url(r'document/$', Document2List.as_view(), name='document-list'),
    url(r'^document/add/$', DocumentCreate.as_view(), name='document-create'),
    url(r'^report/$', views.report_list, name ='report-list'),
    url(r'^role_report/$',views.role_report, name = 'role-report'),
    url(r'^project_report/$',views.project_report, name = 'project-report'),
    url(r'^skill_report/$',views.skill_report, name = 'skill-report'),

]

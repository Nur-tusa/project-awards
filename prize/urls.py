from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectCreateView,ProjectListView,ProjectDetailView,UserProjectListView

urlpatterns=[
    path('welcome', views.welcome, name = 'awwards-welcome'),
    path('', views.home, name = 'home'),
    path('review/(\d+)',views.review,name='review'),
    path('rate/(\d+)',views.rate,name='rate'),
    path('accounts/profile', views.profile, name = 'profile'),
    path('api/profiles', views.ProfilesList.as_view()),
    path('api/profile/profile-id/(?P<pk>[0-9]+)',views.ProfileDescription.as_view()),
    path('api/projects', views.ProjectsList.as_view()),
    path('api/project/project-id/(?P<pk>[0-9]+)',views.ProjectDescription.as_view()),
    path('project/list$', ProjectListView.as_view(), name = 'awwards-home'),
    path('project/new',ProjectCreateView.as_view(), name='project-create'),
    path('user/(?P<username>\w+)', UserProjectListView.as_view(), name='user-projects'),
    path('project/(?P<pk>\d+)/',ProjectDetailView.as_view(), name='project-detail'),
    path('search/', views.search_results, name='search_results'),
    path('project/(?P<pk>\d+)/rating', views.rating, name='awwards-rating'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

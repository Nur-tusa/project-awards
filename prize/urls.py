from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import views
# from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import ProjectCreateView,ProjectListView,ProjectDetailView,UserProjectListView

urlpatterns=[
    path('welcome', views.welcome, name = 'awwards-welcome'),
    path('', views.home, name = 'home'),
    path('review/',views.review,name='review'),
    path('rate/',views.rate,name='rate'),
    path('accounts/profile', views.profile, name = 'profile'),
    path('api/profiles', views.ProfilesList.as_view()),
    path('api/profile/profile-id/<pk>',views.ProfileDescription.as_view()),
    path('api/projects', views.ProjectsList.as_view()),
    path('api/project/project-id/<pk>',views.ProjectDescription.as_view()),
    path('project/list', ProjectListView.as_view(), name = 'awwards-home'),
    path('project/new',ProjectCreateView.as_view(), name='project-create'),
    path('user/<username>', UserProjectListView.as_view(), name='user-projects'),
    path('project/<pk>/',ProjectDetailView.as_view(), name='project-detail'),
    path('search/', views.search_results, name='search_results'),
    path('project/<pk>/rating', views.rating, name='awwards-rating'),
    path('profile-list/', views.profilelist, name='profile-list'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

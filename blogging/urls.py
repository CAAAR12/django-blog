"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # <-- Make sure you have both of these imports.
from django.contrib.auth.views import LoginView, LogoutView
from blogging.views import BloggingListView, BloggingDetailView
# from blogging.views import list_view, detail_view
# from blogging.views import list_view, DeatilListView
urlpatterns = [
    path('posts/<int:pk>/',BloggingDetailView.as_view(),name="blog_detail"),
    path('', BloggingListView.as_view(), name="blog_index"),
]
# urlpatterns = [
#     path('polling/', include('polling.urls')),  
#     path('', include('blogging.urls')),  
#     path('admin/', admin.site.urls),
#     path('login/', LoginView.as_view(template_name='login.html'), name="login"),
#     path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
#     ]

#POLLING UPDATED
# urlpatterns = [
#     path('', PollListView.as_view(), name="poll_index"),
#     path('polls/<int:pk>/', PollDetailView.as_view(), name="poll_detail"),
# ] #since pk was not defined, it will be defined in the address (hence using the pk reference to the variable)

#OLD BLOGGING
# urlpatterns = [
#     path('posts/<int:post_id>/',detail_view,name="blog_detail"),
#     path('', list_view, name="blog_index"),
# ]
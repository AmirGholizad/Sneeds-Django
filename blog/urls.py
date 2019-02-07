"""sneeds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.PostPages.as_view()),
    path('comment/create', views.CreateUserComment.as_view()),
    path('comment/<str:post_slug>', views.GetPostComments.as_view()),
    path('post/<str:topic_slug>', views.TopicDetail.as_view(), name="topic"),  # Topic
    path('post/<str:topic_slug>/<str:post_slug>', views.PostDetail.as_view(), name='post'),  # Post
    path('topics-list/', views.TopicList.as_view(), name='topic_list'),  # Returns all topics as a list
    path('hello/', views.Hello.as_view(), name='hello'),  # Returns all topics as a list

]

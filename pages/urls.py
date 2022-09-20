from django.urls import path
from .views import homePageView
from .views import pathView
from .views import queryView
from .views import bodyView

urlpatterns = [
    path("", homePageView, name="home"),
    path('path/<str:count>/', pathView, name = "path"),
    path('query/', queryView, name = "query"),
    path('body/', bodyView, name = "body"), #зачем нам нужен name везде?
]
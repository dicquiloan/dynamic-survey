from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
	#path('results', views.showResultsWithoutDB, name='showResultsWithoutDB'),
	path('results', views.showResults, name='showResults')
        ]

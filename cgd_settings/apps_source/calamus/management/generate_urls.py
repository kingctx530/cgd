import os

from django.core.management.templates import TemplateCommand


class CalamusUrlsApp(TemplateCommand):

    def __init__(self,cPath):
        super(CalamusUrlsApp, self).__init__()
        self.cPath = cPath

    def display_information(self, info, app_name):
        self.stdout.write(info)
        os.chdir(os.path.join(self.cPath, app_name))

    @classmethod
    def generate_urls(self, app_name, cPath=os.getcwd()):
        self(cPath).display_information("-------- Generate urls.py for {} --------".format(app_name), app_name)
        urls_example = '''
"""ATSCenter URL Configuration

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
from django.urls import path, include

app_name = "{app_name}"
urlpatterns = [

]
    '''.format(app_name=app_name)
        # urls_example = urls_example.split("\n")
        with open("urls.py", "w", encoding="utf-8") as file:
            file.write(urls_example)
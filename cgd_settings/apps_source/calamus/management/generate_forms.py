import os

from django.core.management.templates import TemplateCommand


class CalamusFormsApp(TemplateCommand):

    def __init__(self,cPath):
        super(CalamusFormsApp, self).__init__()
        self.cPath = cPath

    def display_information(self, info, app_name):
        self.stdout.write(info)
        os.chdir(os.path.join(self.cPath, app_name))

    @classmethod
    def generate_forms(self, app_name, cPath=os.getcwd()):
        self(cPath).display_information("-------- Generate forms.py for {} --------".format(app_name), app_name)
        # os.makedirs(os.path.join(os.getcwd(), "locale"))
        forms_example = '''
from django import forms
"""
Examples:

    class NameForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)
        
"""            
'''
        with open("forms.py", "w", encoding="utf-8") as file:
            file.write(forms_example)

import os

from django.core.management.templates import TemplateCommand


class CalamusTemplatesApp(TemplateCommand):

    def __init__(self,cPath):
        super(CalamusTemplatesApp, self).__init__()
        self.cPath = cPath

    def display_information(self, info, app_name):
        self.stdout.write(info)
        os.chdir(os.path.join(self.cPath, app_name))

    @classmethod
    def generate_templates(self, app_name, cPath=os.getcwd()):
        self(cPath).display_information("-------- Generate templates folder for {} --------".format(app_name), app_name)
        os.makedirs(os.path.join(os.getcwd(), "templates"))
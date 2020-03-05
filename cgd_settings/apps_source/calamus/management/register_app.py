import os

from django.conf import settings
from django.core.management.templates import TemplateCommand


class CalamusRegisterApp(TemplateCommand):
    def __init__(self,cPath):
        super(CalamusRegisterApp, self).__init__()
        self.cPath = cPath

    def display_information(self,info,app_name):
        self.stdout.write(info)
        os.chdir(os.path.join(self.cPath, app_name))

    @classmethod
    def register_app(self,app_name,cPath=os.getcwd()):
        self(cPath=cPath).display_information("register app : {}".format(app_name), app_name)
        BASE_DIR = getattr(settings, "BASE_DIR", self(cPath=cPath).cPath)
        os.chdir(os.path.join(BASE_DIR,os.path.basename(BASE_DIR)))
        begin = False
        ALL_DATA = []
        with open("settings.py","r",encoding="utf-8") as file:
            for f in file:
                # if begin:
                ALL_DATA.append(f)
                if "TEST_APP = [" in f:
                    begin = False
                    ALL_DATA.append("    '{}',\n".format(app_name))

                # else:
                #     if "INSTALLED_APPS" in f:
                #         begin = True
                #     ALL_DATA.append(f)

        with open("settings.py", "w", encoding="utf-8") as file:
            for data in ALL_DATA:
                file.write(data)
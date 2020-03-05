import os
import re

import sys
from django.conf import settings
from django.core import management
from django.core.management.templates import TemplateCommand


class CalamusI18nApp(TemplateCommand):
    def __init__(self,cPath):
        super(CalamusI18nApp, self).__init__()
        self.cPath=cPath

    def display_information(self,info,app_name):
        self.stdout.write(info)
        os.chdir(os.path.join(self.cPath, app_name))

    def build_i18n_list(self,data):
        if "-" in data:
            return (" {}_{}".format(data.split("-")[0], data.split("-")[-1].capitalize()))
        else:
            return (data)

    def generate_i18n(self,app_name):
        self.display_information("-------- Generate i18n language for {} --------".format(app_name),app_name)
        os.makedirs(os.path.join(os.getcwd(),"locale"))
        i18n_gen = []
        for idx, data in enumerate(getattr(settings, "LANGUAGES", ('en', ('English')))):
            i18n_gen.append("-l")
            i18n_gen.append(self.build_i18n_list(data[0]))
        management.execute_from_command_line(['django-admin','makemessages', '-l', 'zh_Hant', '-l', 'zh_Hans', '-l', 'en'])

    def apps_read_update(self,app_name):
        rat = r"\S*\W*\("
        self.appconfig = ""
        import_data = "from django.utils.translation import ugettext_lazy as _"
        verbose_name = "    verbose_name = _('{} APP')".format('{}'.format(app_name).upper())
        app_data = []

        with open("apps.py", "r", encoding="utf-8") as file:
            for f in file:
                app_data.append(f)
                if re.search(rat, f):
                    self.appconfig = re.search(rat, f).group().strip("(")

        app_data.insert(1, import_data)
        app_data.append(verbose_name)

        with open("apps.py", "w", encoding="utf-8") as file:
            for ad in app_data:
                file.writelines("{}".format(ad))

    def generate_app_i18n(self,app_name):
        self.display_information("-------- Generate app {} i18n --------".format(app_name),app_name)
        self.app_path = os.getcwd()

        self.apps_read_update(app_name)  #read app information and add i18n format

        if sys.path[0] == self.cPath:
            BASE_DIR = self.cPath
        else:
            BASE_DIR = getattr(settings,"BASE_DIR",self.cPath)

        real_app_path = self.app_path.split(BASE_DIR)
        if len(real_app_path) > 1:
            real_app_path = real_app_path[-1].split(os.sep)
            real_app_path.remove('')
            real_app_path.append("apps")
        else:
            self.stderr.write("app path analysis error: {}".format(real_app_path))

        real_app_path.append(self.appconfig)
        final_set = '.'.join(real_app_path)
        with open("__init__.py","w",encoding="utf-8") as file:
            file.write("default_app_config = '{}'\n".format(final_set))

        self.generate_i18n(app_name)
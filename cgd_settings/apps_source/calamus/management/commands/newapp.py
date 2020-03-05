import os
import re

import sys
from django.conf import settings
from django.core.management.templates import TemplateCommand
from django.core import management

from calamus.apps import CalamusConfig
from calamus.management.generate_forms import CalamusFormsApp
from calamus.management.generate_templates import CalamusTemplatesApp
from calamus.management.generate_urls import CalamusUrlsApp
from calamus.management.i18n_app import CalamusI18nApp
from calamus.management.register_app import CalamusRegisterApp


class Command(TemplateCommand):
    help = (
        "Glider custom Creates a Django app directory structure for the given app name in "
        "the current directory or optionally in the given directory."
    )
    missing_args_message = "You must provide an application name."

    # def add_arguments(self, parser):
    #     parser.add_argument('hello')


    def handle(self, *args, **options):
        self.stdout.write("create app ...")
        app_name = options.pop('name')
        target = options.pop('directory')
        super().handle('app', app_name, target, **options)
        self.stdout.write("custom app ...")
        self.cPath = os.getcwd()
        CalamusRegisterApp.register_app(app_name,cPath=self.cPath)
        CalamusI18nApp(cPath=self.cPath).generate_app_i18n(app_name)
        CalamusUrlsApp.generate_urls(app_name,self.cPath)
        CalamusTemplatesApp.generate_templates(app_name,cPath=self.cPath)
        CalamusFormsApp.generate_forms(app_name,cPath=self.cPath)
        self.stdout.write("All function successfully!")



import os
import shutil
import time

from cgd_settings.settings_update_source import SettingsUpdateSource
from public_fun import PublicFun


class SettingsUpdate(PublicFun, SettingsUpdateSource):
    def __init__(self):
        super(SettingsUpdate, self).__init__()
        SettingsUpdateSource.__init__(self)
        self.new_souce = []

    def update_settings(self,channels=None):
        for i, s in enumerate(self.source):
            self.new_souce.append(s)
            if "import os" in s:
                for t in self.import_data:
                    self.new_souce.append('\r\n')
                    self.new_souce.append(t)
            if "BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))" in s:
                for t in self.sys_data:
                    self.new_souce.append('\r\n')
                    self.new_souce.append(t)
                    # self.new_souce.append('\r\n')
                    # self.new_souce.append(self.insert_data.pop(0))
            if i + 1 < len(self.source):
                if 'MIDDLEWARE = [' in self.source[i + 1]: #install TEST_APP,SYS_APP funciont

                    for t in self.test_apps_data:  # TEST APP
                        self.new_souce.append('\r\n')
                        self.new_souce.append(t)

                    for t in self.sys_apps_data:   # SYS APP
                        self.new_souce.append('\r\n')
                        self.new_souce.append(t)

                    for t in self.install_apps_data:   #INSTALL = TEST APP + SYS APP + INSTALLED APP
                        self.new_souce.append('\r\n')
                        self.new_souce.append(t)
                    self.new_souce.append('\r\n')
                    self.new_souce.append('\r\n')


            if "'DIRS': []," in s:
                self.new_souce[-1] = self.template_data[0]
                self.new_souce.append('\r\n')
            if "'context_processors': [" in s:
                tmp = self.new_souce[-1]
                self.new_souce[-1] = self.templatetags
                self.new_souce.append('\r\n')
                self.new_souce.append(tmp)

            if "WSGI_APPLICATION" in s:
                if channels:
                    self.new_souce.append('\r\n')
                    for t in self.asgi_data:  # ASGI
                        self.new_souce.append('\r\n')
                        self.new_souce.append(t)

                    for t in self.channel_data:  # Redis setting
                        self.new_souce.append('\r\n')
                        self.new_souce.append(t)


        self.new_souce.append(self.static_data)
        print("》》》 Update to setting.py 《《《")
        tmp_filename = "{}_settings.py".format(time.time())
        self.file_operation(tmp_filename, mode="w", data=self.new_souce)

        shutil.move(tmp_filename, self.last_filename)
        # for n in self.new_souce:
        #     print(n.strip())

    def auto_building_folder(self):
        print("》》》 Auto building folder 《《《")
        self.project_root = os.path.dirname(os.path.abspath(os.path.dirname(self.last_filename)))
        os.makedirs(os.path.join(self.project_root, 'staticfiles'), exist_ok=True)
        os.makedirs(os.path.join(self.project_root, 'public/static'), exist_ok=True)
        os.makedirs(os.path.join(self.project_root, 'public/media'), exist_ok=True)
        os.makedirs(os.path.join(self.project_root, 'template'), exist_ok=True)
        os.makedirs(os.path.join(self.project_root, 'apps'), exist_ok=True)
        os.makedirs(os.path.join(self.project_root, 'locale'), exist_ok=True)

    def copy_app(self):
        print("》》》 Auto building folder 《《《")
        # print(os.path.join(os.path.dirname(os.path.abspath(__file__))))
        shutil.copytree(os.path.join(os.path.dirname(os.path.abspath(__file__)),"apps_source","calamus"),os.path.join(self.project_root, 'apps','calamus'))
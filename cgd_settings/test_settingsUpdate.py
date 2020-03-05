from unittest import TestCase

from cgd_settings.settings_update import SettingsUpdate


class TestSettingsUpdate(TestCase):
    def setUp(self) -> None:
        self.su = SettingsUpdate()
        self.su.file_operation(r"tt/mytest/mytest/settings.py")

    def test_insert_data(self):
        self.su.update_settings()
        self.su.auto_building_folder()
        self.su.copy_app()

    def tearDown(self) -> None:
        del self.su

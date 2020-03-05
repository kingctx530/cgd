from unittest import TestCase

from public_fun import PublicFun


class TestPublicFun(TestCase):
    def setUp(self) -> None:
        self.pf = PublicFun()
    def test_open_target(self):
        self.pf.file_operation(r"tt/mytest/mytest/settings.py")
        print(self.pf.source)
    def tearDown(self) -> None:
        del self.pf

class PublicFun:
    def __init__(self):
        self.source = []
        self.last_filename = None

    def detect_os(self):
        from sys import platform
        if platform == "linux" or platform == "linux2":
            return "utf-8"
        elif platform == "darwin":
            return "utf-8"
        elif platform == "win32":
            return "latin"

    # Windows...

    def file_operation(self, filename, mode="r",data=[]):
        if self.last_filename is None:
            self.last_filename = filename
        encoding = self.detect_os()
        with open(filename, mode, encoding=encoding) as files:
            if mode == "r":
                for f in files:
                    self.source.append(f)
            elif mode == "w":
                for d in data:
                    files.write(d)

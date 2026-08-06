
class Rule:
    def __init__(self, extensions=None, destination=""):
        self.extensions = [ext.lower() for ext in (extensions or [])]
        self.destination = destination

    def match(self, extension)->bool:
        return extension.lower() in self.extensions
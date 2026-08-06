from pathlib import Path

class FileInfo:
    def __init__(self, archive : Path):
        self.name = archive.name
        self.extension = archive.suffix.lower()
        self.path = archive
        self.size = archive.stat().st_size
        self.is_file = archive.is_file()
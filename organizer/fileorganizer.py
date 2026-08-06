from pathlib import Path
import shutil
from organizer.statistics import Statistics
from organizer.fileinfo import FileInfo
from organizer.logger import Logger
from organizer.rules import Rule

class FileOrganizer:
    def __init__(self, folder: Path, rules : list[Rule], logger: Logger):
        self.folder = folder
        self.files: list[FileInfo] = []
        self.rules: list[Rule] = rules
        self.stats: Statistics = Statistics()
        self.logger: Logger = logger

    def load_files(self):
        self.files = [FileInfo(path) for path in self.folder.iterdir() if path.is_file()]
        self.stats.total_files = len(self.files)
        return self.files

    def find_rule(self, file: FileInfo) -> Rule | None:
        for rule in self.rules:
           if rule.match(file.extension):
               return rule
        return None

    def organize(self):
        self.load_files()

        for file in self.files:
            rule = self.find_rule(file)

            if rule is None:
                self.stats.add_ignored()
                continue

            destination = self.folder / rule.destination

            if not destination.exists():
                destination.mkdir(parents=True)
                self.stats.add_folder()

            try:
                shutil.move(file.path, destination / file.name)
                self.stats.add_moved()
                self.logger.log_move(file.path, destination / file.name)
            except Exception as error:
                self.stats.add_error()
                print(f"Erro ao mover {file.name}: {error}")

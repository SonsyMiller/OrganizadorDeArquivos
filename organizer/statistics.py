
class Statistics:

    def __init__(self):
        self.total_files = 0
        self.moved_files = 0
        self.ignored_files = 0
        self.errors = 0
        self.created_folders = 0

    def add_moved(self):
        self.moved_files += 1

    def add_ignored(self):
        self.ignored_files += 1

    def add_error(self):
        self.errors += 1

    def add_folder(self):
        self.created_folders += 1

    def report(self):
        return f"""
    Arquivos analisados: {self.total_files}
    Arquivos movidos: {self.moved_files}
    Arquivos ignorados: {self.ignored_files}
    Pastas criadas: {self.created_folders}
    Erros: {self.errors}
    """
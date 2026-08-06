from organizer import *
from pathlib import Path

def main():
    path = Path("teste")

    loader = ConfigLoader()
    rules = loader.load_rules(Path("config/config.json"))

    project_root = Path(__file__).parent
    logger = Logger(project_root / "logs")

    organizer = FileOrganizer(path,rules,logger)
    organizer.organize()

    print(organizer.stats.report())


if __name__ == "__main__":
    main()
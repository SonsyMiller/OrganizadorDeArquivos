from datetime import datetime
from pathlib import Path

class Logger:
    def __init__(self, log_folder: Path, filename: str = "organizer.log"):
        self.log_folder = log_folder
        self.log_folder.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        self.file = self.log_folder / f"{timestamp}.log"

    def write(self, message: str):
        with open(self.file, "a", encoding="utf-8") as log:
            log.write(message + "\n")

    def log_move(self, origin: Path, destination: Path):
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        message = f"""
    [{time}]
    MOVIDO:
    {origin}

    DESTINO:
    {destination}

    ________________________
    """

        self.write(message)
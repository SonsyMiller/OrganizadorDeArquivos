import json
from organizer.rules import Rule
from pathlib import Path

class ConfigLoader:

    def load_rules(self, file_path: Path) -> list[Rule]:
        with open(file_path, "r", encoding="utf-8") as arquivo:
            configs = json.load(arquivo)
        rules = []
        for destination,extensions in configs.items():
            rule = Rule(extensions, destination)
            rules.append(rule)
        return rules


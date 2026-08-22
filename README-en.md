# File Organizer

A file organizer developed in Python using Object-Oriented Programming (OOP).

The program analyzes all files in a folder, identifies their types through configurable rules, and automatically moves them into specific directories. It also generates execution statistics and records all file movements in log files.

## Features

* Automatic file organization by extension.
* Configurable rules through a JSON file.
* Automatic creation of destination folders.
* Logging of all file movements.
* Execution statistics.
* Architecture based on Object-Oriented Programming.

---

## Project Structure

```text
OrganizadorDeArquivos/

├── config/
│   └── config.json
│
├── logs/
│   └── *.log
│
├── organizer/
│   ├── __init__.py
│   ├── organizer.py
│   ├── fileinfo.py
│   ├── rules.py
│   ├── statistics.py
│   ├── logger.py
│   └── config_loader.py
│
├── teste/
│
├── main.py
└── README.md
```

## Technologies Used

* Python 3.11+
* pathlib
* shutil
* json
* datetime

All libraries used are part of Python's standard library.

## Configuration

Organization rules are defined in `config/config.json`.

Example:

```json
{
    "Images": [".png", ".jpg", ".jpeg"],
    "PDFs": [".pdf"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi"]
}
```

Each key represents a destination folder, while the list contains the file extensions that will be moved into that folder.

## How to Run

1. Clone this repository.
2. Enter the project folder.
3. Configure the rules in `config/config.json`.
4. Define the folder to be organized in `main.py`.
5. Run the project.

## Example

### Before organization

```text
Downloads/
├── photo.png
├── document.pdf
├── music.mp3
└── file.txt
```

### After organization

```text
Downloads/

├── Images/
│   └── photo.png
│
├── PDFs/
│   └── document.pdf
│
├── Music/
│   └── music.mp3
│
└── file.txt
```

Files without a matching rule remain in their original location.

## Logs

Each execution automatically generates a log file inside the `logs/` folder.

Example:

```text
[05/08/2026 20:35:10]

MOVED:
Downloads/photo.png

DESTINATION:
Downloads/Images/photo.png
```

## Statistics

At the end of the execution, the program displays a report similar to the following:

```text
Files analyzed: 15
Files moved: 12
Files ignored: 2
Folders created: 3
Errors: 0
```

## Architecture

The project was developed following Object-Oriented Programming principles.

| Class           | Responsibility                                |
| --------------- | --------------------------------------------- |
| `FileOrganizer` | Coordinates the entire organization process.  |
| `FileInfo`      | Represents a file in the file system.         |
| `Rule`          | Represents an organization rule.              |
| `ConfigLoader`  | Loads rules from the JSON configuration file. |
| `Logger`        | Records the file movements performed.         |
| `Statistics`    | Stores execution statistics.                  |

## Future Improvements

* Graphical user interface.
* Progress bar.
* Organization by creation date.
* Organization by file size.
* Automatic folder monitoring.
* Executable generation.

## License

This project was developed for study purposes and to practice Object-Oriented Programming.

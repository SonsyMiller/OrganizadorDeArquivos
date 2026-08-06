# Organizador de Arquivos

Um organizador de arquivos desenvolvido em Python utilizando Programação Orientada a Objetos (POO).

O programa analisa todos os arquivos de uma pasta, identifica seu tipo através de regras configuráveis e os move automaticamente para diretórios específicos. Além disso, gera estatísticas da execução e registra todas as movimentações em arquivos de log.

## Funcionalidades ##

> Organização automática de arquivos por extensão.
> Regras configuráveis através de um arquivo JSON.
> Criação automática das pastas de destino.
> Registro de todas as movimentações em arquivos de log.
> Geração de estatísticas da execução.
> Arquitetura baseada em Programação Orientada a Objetos.

---

## Estrutura do Projeto ##

1-OrganizadorDeArquivos/

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
|   └── config_loader.py
│
├── teste/
│
├── main.py
└── README.md


## Tecnologias Utilizadas ##

> Python 3.11+
> pathlib
> shutil
> json
> datetime

Todas as bibliotecas utilizadas fazem parte da biblioteca padrão do Python.



## Configuração ##

-> As regras de organização são definidas no arquivo "config/config.json"

Exemplo:

{
    "Imagens": [".png", ".jpg", ".jpeg"],
    "PDFs": [".pdf"],
    "Musicas": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi"]
}

-> Cada chave representa uma pasta de destino, enquanto a lista contém as extensões que serão movidas para essa pasta.


## Como Executar ##

1-Clone este repositório

2-Entre na pasta do projeto.

3-Configure as regras em `config/config.json`.

4-Defina a pasta que será organizada no arquivo `main.py`.

5-Execute o projeto.


## Exemplo ##

>>Antes da organização:

Downloads/
    foto.png
    documento.pdf
    musica.mp3
    arquivo.txt


>>Depois:

Downloads/

Imagens/
    foto.png

PDFs/
    documento.pdf

Musicas/
    musica.mp3

arquivo.txt


## Logs ##

-> Cada execução gera automaticamente um arquivo de log na pasta `logs/`

Exemplo:

[05/08/2026 20:35:10]

MOVIDO:
Downloads/foto.png

DESTINO:
Downloads/Imagens/foto.png


## Estatísticas ##

-> Ao final da execução, o programa apresenta um relatório semelhante ao exemplo abaixo:

Arquivos analisados: 15
Arquivos movidos: 12
Arquivos ignorados: 2
Pastas criadas: 3
Erros: 0


## Arquitetura ##

-> O projeto foi desenvolvido seguindo princípios de Programação Orientada a Objetos.

| Classe          | Responsabilidade                            |
| --------------- | ------------------------------------------- |
| "FileOrganizer" | Coordena todo o processo de organização.    |
| "FileInfo"      | Representa um arquivo do sistema.           |
| "Rule"          | Representa uma regra de organização.        |
| "ConfigLoader"  | Carrega as regras a partir do arquivo JSON. |
| "Logger"        | Registra as movimentações realizadas.       |
| "Statistics"    | Armazena as estatísticas da execução.       |



## Melhorias Futuras ##

> Interface gráfica
> Barra de progresso
> Organização por data de criação
> Organização por tamanho
> Monitoramento automático de pastas
> Geração de executável


## Licença ##

>>Este projeto foi desenvolvido para fins de estudo e prática de Programação Orientada a Objetos<<
"# OrganizadorDeArquivos"
"# OrganizadorDeArquivos"

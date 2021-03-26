# Meme Generator
Command line and Flask web application to generate memes.

## Overview
Software written in Python that allows users to interact via command line interface and a webpage running on a Flask framework to generate memes. Memes can be generated randomly from images contained in the ./\_data/photos/ directory and with files containing quotes in various file types found in the  ./\_data/DogQuotes directory. In the webapp users can input a url for an image location and enter a quote and an author. In the command line users can also enter their own quote and author.

## Interface

### app.py
By executing app.py the script will be run on a flask server and will allow the user access a webpage form. The user can access the content that is located on the webserver by navigating to http://127.0.0.1:5000/ in their web browser. The landing page will generate a randomly chosen image and quote file and present that as a meme. The user can navigate to create and enter a url for an image, a quote, and author into the webform to generate that as a meme.

### meme.py
By executing meme.py the user will be to use the Command Line Interface with arguments: -h, --help --path --body --author. 
If no arguments are given the script will run and generate a random meme from the images and quote files found within the proper directories.

The command line interface requires pdftotext.exe to be installed on the users system, which can be downloaded from https://www.xpdfreader.com/download.html.
dfvw 
### QuoteEngine Library
The QuoteEngine consists of a modules used for encapsulating a quote object , and ingesting data from different file types to be encapsulated as a quote object.

#### QuoteModel.py
Used to define the QuoteModel class which contains two string attributes, body and author.

#### IngestorInterface.py
An abstract base class used as the parent class for CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor, and Ingestor. It contains two class methods, can_ingest which checks to see if a file type can be parsed by the child class strategy object and an abstract method, parse, which is defined in the child class.

#### CSVIngestor.py
Child class that is used as a strategy object to parse .csv files. The class method parse is overloaded in this child class. It requires Pandas and list from typing to be imported in order to execute. Returns a list of QuoteModel objects.

#### DocxIngestor.py
Child class that is used as a strategy object to parse .docx files. The class method parse is overloaded in this child class. It requires Document from docx and list from typing to be imported in order to execute. Returns a list of QuoteModel objects.

#### PDFIngestor.py
Child class that is used as a strategy object to parse .pdf files, by converting them to .txt. the class method parse is overloaded in this child class. It requires os, subprocess, and random and list from typing to be imported in order to execute. Additionally it requires pdftotext.exe to be installed. Returns a list of QuoteModel objects.

#### TextIngestor.py
Child class that is used as a strategy object to parse .txt files. The class method parse is overloaded in this child class. Requires list from typing to be imported in order to execute. Returns a list of QuoteModel objects.

#### Ingestor.py
Child class that is used to detemine which strategy object to use to parse files depending on the file type. The class method parse is overloaded in this child class. Requires list from typing to be imported in order to execute. Returns a list of QuoteModel objects.

### MemeEngine Library
The MemeEngine Library consists of a module that defines the MemeEngine class which consists of methods that are used for editing an image

#### MemeEngine.py
This class is used to resize and add text to an image that is either passed in by the user in one of the interfaces or in the CLI, or chosen at random. the three methods are resize, write_text, and make_meme. It requires Image, ImageDraw, and ImageFont from the Pillow library, and random.

## Requirements
All of the libraries that need to be installed can be installed by running `pip install requirements.txt` in the src directory.

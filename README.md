# Meme Generator

This project is a **Meme Generator** that allows users to create memes by overlaying quotes onto images. Users can provide a quote (body and author), and the program will add it to a randomly selected image or a user-specified image. The generated meme is then saved as an output image file.

## Overview

The Meme Generator is a tool that automates the process of creating memes. It resizes images, adds text, and saves the result in an output directory. The project is built using Python and utilizes several sub-modules, such as a module for image manipulation and text handling. The tool also supports ingestion of quotes from multiple file formats (e.g., `.txt`, `.csv`, `.docx`, `.pdf`) and places the caption at a random location on the image.

## Setup and Instructions for Running the Program

### Prerequisites

Ensure you have the following installed on your machine:

- `pip3 install -r requirements.txt`

Run the **app.py** to create a localhost webserver, we can create memes from images and quotes are stored in **./src/_data/** and also from URL image link.
- `python3 app.py`


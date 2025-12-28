# Document Converter Tools

A simple set of tools to convert PDF and Word documents to images and PDFs.

## Features
- **PDF to JPG**: Converts every page of a PDF file into a high-quality JPG image.
- **Word to PDF**: Converts Microsoft Word documents (`.docx`, `.doc`) to PDF.
- **Word to JPG**: Converts Word documents directly to JPG images.

## Prerequisites
1.  **Python 3.10+**: Make sure Python is installed and added to your PATH.
2.  **Microsoft Word**: Required for Word document conversions.

## Installation
1.  Open the project folder in a terminal.
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
You can run the tools effortlessly by double-clicking the provided batch files:

### 1. Convert PDF to JPG
- Place your PDF files in the `input_pdfs` folder.
- Double-click **`run_converter.bat`**.
- Find your images in the `output_jpgs` folder.

### 2. Convert Word to PDF
- Place your Word files in the `input_word` folder.
- Double-click **`run_word_to_pdf.bat`**.
- Find your PDFs in the `output_word_pdfs` folder.

### 3. Convert Word to JPG
- Place your Word files in the `input_word` folder.
- Double-click **`run_word_to_jpg.bat`**.
- Find your images in the `output_word_jpgs` folder.

## Project Structure
- `scripts/`: Contains the Python source code.
- `input_...`: Drop your source files here.
- `output_...`: Collect your converted files here.

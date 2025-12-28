import os
import sys
from docx2pdf import convert

def convert_word_to_pdf(input_dir, output_dir):
    """
    Converts all Word files in the input_dir to PDF in the output_dir.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    word_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.docx', '.doc'))]

    if not word_files:
        print(f"No Word files found in {input_dir}")
        return

    print(f"Found {len(word_files)} Word file(s) in {input_dir}. Starting conversion...")

    for word_file in word_files:
        word_path = os.path.join(input_dir, word_file)
        # Output PDF name
        pdf_name = os.path.splitext(word_file)[0] + ".pdf"
        output_path = os.path.join(output_dir, pdf_name)
        
        print(f"Processing: {word_file}")
        try:
            convert(word_path, output_path)
            print(f"  Saved: {pdf_name}")
        except Exception as e:
            print(f"Error processing {word_file}: {e}")

    print("All Word to PDF conversions complete!")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    input_folder = os.path.join(project_root, "input_word")
    output_folder = os.path.join(project_root, "output_word_pdfs")
    
    # Ensure input directory exists
    if not os.path.exists(input_folder):
        print(f"Input directory '{input_folder}' does not exist. Creating it...")
        os.makedirs(input_folder)
        print("Please put your Word files in the 'input_word' folder and run this script again.")
    else:
        convert_word_to_pdf(input_folder, output_folder)

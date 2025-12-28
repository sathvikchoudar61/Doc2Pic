import os
import shutil
from docx2pdf import convert
import fitz  # PyMuPDF

# Import our existing PDF to JPG logic
# We need to make sure converter.py can be imported without running its main block
# (This is handled by the if __name__ == "__main__" block in converter.py)
from converter import convert_pdfs_to_jpgs

def convert_word_to_jpg(input_dir, output_dir):
    """
    Converts Word files to JPG by first converting to a temp PDF, then to JPG.
    """
    temp_pdf_dir = os.path.join(input_dir, "temp_pdfs_for_conversion")
    
    if not os.path.exists(temp_pdf_dir):
        os.makedirs(temp_pdf_dir)

    print("Step 1: Converting Word to temporary PDF...")
    
    word_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.docx', '.doc'))]
    
    if not word_files:
        print(f"No Word files found in {input_dir}")
        # Cleanup
        if os.path.exists(temp_pdf_dir):
            os.rmdir(temp_pdf_dir)
        return

    # Convert Word to Temp PDF
    for word_file in word_files:
        word_path = os.path.join(input_dir, word_file)
        pdf_name = os.path.splitext(word_file)[0] + ".pdf"
        temp_output_path = os.path.join(temp_pdf_dir, pdf_name)
        
        try:
            print(f"  Converting doc: {word_file}")
            convert(word_path, temp_output_path)
        except Exception as e:
            print(f"  Error converting {word_file} to PDF: {e}")

    print("\nStep 2: Converting temporary PDFs to JPG...")
    # Use our existing logic
    convert_pdfs_to_jpgs(temp_pdf_dir, output_dir)
    
    print("\nStep 3: Cleaning up temporary files...")
    try:
        shutil.rmtree(temp_pdf_dir)
        print("Cleanup complete.")
    except Exception as e:
        print(f"Error cleaning up temp folder: {e}")

    print("All Word to JPG conversions complete!")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    input_folder = os.path.join(project_root, "input_word")
    output_folder = os.path.join(project_root, "output_word_jpgs")
    
    if not os.path.exists(input_folder):
        print(f"Input directory '{input_folder}' does not exist. Creating it...")
        os.makedirs(input_folder)
        print("Please put your Word files in the 'input_word' folder.")
    else:
        convert_word_to_jpg(input_folder, output_folder)

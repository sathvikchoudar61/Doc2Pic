import os
import fitz  # PyMuPDF

def convert_pdfs_to_jpgs(input_dir, output_dir, dpi=300):
    """
    Converts all PDF files in the input_dir to JPG images in the output_dir.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return

    print(f"Found {len(pdf_files)} PDF(s) in {input_dir}. Starting conversion...")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_dir, pdf_file)
        print(f"Processing: {pdf_file}")
        
        try:
            doc = fitz.open(pdf_path)
            pdf_name = os.path.splitext(pdf_file)[0]
            
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                # Zoom matrix for higher quality (dpi)
                zoom = dpi / 72  # 72 is standard PDF dpi
                mat = fitz.Matrix(zoom, zoom)
                
                pix = page.get_pixmap(matrix=mat)
                output_filename = f"{pdf_name}_page_{page_num + 1}.jpg"
                output_path = os.path.join(output_dir, output_filename)
                
                pix.save(output_path)
                print(f"  Saved: {output_filename}")
                
            doc.close()
            print(f"Finished processing: {pdf_file}")
            
        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")

    print("All conversions complete!")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    input_folder = os.path.join(project_root, "input_pdfs")
    output_folder = os.path.join(project_root, "output_jpgs")
    
    # Ensure input directory exists
    if not os.path.exists(input_folder):
        print(f"Input directory '{input_folder}' does not exist. Creating it...")
        os.makedirs(input_folder)
        print("Please put your PDF files in the 'input_pdfs' folder and run this script again.")
    else:
        convert_pdfs_to_jpgs(input_folder, output_folder)

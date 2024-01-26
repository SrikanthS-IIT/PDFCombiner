import PyPDF2
import os

def combine_pdfs(input_folder, output_file):
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Get a list of all PDF files in the input folder
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]

    # Sort the PDF files to maintain order
    pdf_files.sort()

    # Iterate through each PDF file and add its pages to the output PDF
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        pdf_reader = PyPDF2.PdfReader(pdf_path)

        # Add each page to the writer object
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    # Write the combined PDF to the output file
    with open(output_file, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    print(f'Combined {len(pdf_files)} PDFs into {output_file}')

# Example usage:
input_folder = '\source\folder\path'
output_file = '\destination\folder\path\combined.pdf'
combine_pdfs(input_folder, output_file)

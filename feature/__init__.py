import pdfplumber
import os

def check_file(filename, path):
    filepath = str()
    dirs = {'home': os.path.expanduser,
           'downloads': os.path.expanduser('/Downloads'),
           'documents': os.path.expanduser('/Documents')
    }
    if path in dirs.keys():
        src_dir = os.path.dirname(os.path.abspath(filepath))
        print('src_dir:\t', src_dir)
        filepath = src_dir + '\\' + filename
        print('File found:\t', filepath)
        return filepath

def read_content(filepath):
    pdf_text = ''
    with pdfplumber.open(filepath) as pdf:
        pages = pdf.pages
        for page in pages:
            pdf_text = page.extract_text()
        return pdf_text


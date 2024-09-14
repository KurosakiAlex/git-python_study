import PyPDF2
import sys

def merge_pdfs(pdf_list, output_path):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()

def main():

    output_path = sys.argv[1]
    pdf_list = sys.argv[2:]
    merge_pdfs(pdf_list, output_path)


if __name__ == '__main__':
    main()























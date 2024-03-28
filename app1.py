from PyPDF2 import PdfFileReader
import os

pdf_folder = './pdfs'
bulan = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']

def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        # get the first page
        page = pdf.getPage(1)
        print(page)
        print('Page type: {}'.format(str(type(page))))
        text = page.extractText()
        print(text)
if __name__ == '__main__':
    for (root, dirs, file) in os.walk(pdf_folder):
        if len(dirs)>0:
            company_name = dirs[0] 
        for f in file:
            if '.pdf' in f:
                if 'Laporan-Keuangan-Desember-2023.pdf' in f:
                    arr_f = f.split('.')[0].split('-')
                    year = arr_f[-2]
                    month = arr_f[-1]
                    print(year,month)
                    print(root)
                    _f = os.path.abspath(os.path.join(root, f))
                    print('file: ',_f)
                    text_extractor(_f)
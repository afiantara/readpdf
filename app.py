import camelot.io as camelot
import os
import pandas as pd

pdf_folder = './pdfs'
bulan = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']


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
                tables = camelot.read_pdf(_f)
                print("Total tables extracted:", tables.n)
                df=tables[0].df
                print(df.head())
                tables[0].to_csv("{}.csv".format(company_name))

    print(company_name)
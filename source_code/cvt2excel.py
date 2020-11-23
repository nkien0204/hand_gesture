import pandas as pd
name = 'kien'
sample = 'an_com'
txt_folder_path = 'C:/Users/LENOVO/Documents/Arduino/log_files/' + name + '/' + 'text_files' + '/' + sample
excel_foler_path = 'C:/Users/LENOVO/Documents/Arduino/log_files/' + name + '/' + 'excel_files' + '/' + sample

def convert2excel(txt_folder, excel_folder):
	for i in range(1, 6):
		txt_file = txt_folder + '/' + sample + '_' + str(i) + '.txt'
		excel_file = excel_folder + '/' + sample + '_' + str(i) + '.xlsx'
		txt_file = pd.read_table(txt_file, sep = ',')
		txt_file.to_excel(excel_file, 'Sheet1')

convert2excel(txt_folder_path, excel_foler_path)
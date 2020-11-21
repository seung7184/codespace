#!\C:\Users\rokbatt-coo\AppData\Local\Microsoft\WindowsApps\python.exe

#Things to import
import glob, os, datetime, shutil, ctypes
from datetime import date, timedelta

#Setting Dates
yesterday = date.today() - timedelta(days=1)
yesterday = yesterday.strftime('%d-%m-%Y')
today = datetime.date.today().strftime("%d-%m-%Y")

#List of xlsx files
list_of_files = glob.glob(r'C:\Users\rokbatt-coo\Desktop\DUTY\test\*'+yesterday+'.xlsx')
latest_file = max(list_of_files, key=os.path.getctime)

#Copy the latest file
original = latest_file
target = r'C:\Users\rokbatt-coo\Desktop\DUTY\test\CDRS_.xlsx'
shutil.copyfile(original, target)
newname = 'CDRS_'+today+'.xlsx'

try:
    os.rename(target, newname)
except FileExistsError:
	print('The file already exists.')
	os.remove(r'C:\Users\rokbatt-coo\Desktop\DUTY\test\CDRS_.xlsx')
	ctypes.windll.user32.MessageBoxW(0, "The file already exists.", "Warning", 1)

#Open the Copied file
copied_file = glob.glob(r'C:\Users\rokbatt-coo\Desktop\DUTY\test\*'+today+'.xlsx')
result_file = max(copied_file, key=os.path.getctime)

os.startfile(result_file)
#python script to produce summary of all the python files

#scan all the file present in the parent directory
import glob,xlsxwriter
workBook=xlsxwriter.Workbook('final.xlxs')
workSheet=workBook.add_worksheet()
summary=(
    ['FileName','Details','Libraries Used'],
)
row=0
col=0
summary1=[]
for FILENAME, DETAILS, LIBS in (summary):
    workSheet.write(row, 0, FILENAME)
    workSheet.write(row, 1, DETAILS)
    workSheet.write(row, 2, LIBS)
    row += 1


temp=glob.glob('../*.py')
for temps in temp:
#search for all the lines in string  with import text and store the line number in line variable
    findString='import '
#open all file and read the file and pass that to a string
    myFile=open(temps)
    tempFile=myFile.read()
    libString=tempFile
    libsUsedLength=libString.find(findString)
    tempString1=libString[libsUsedLength+7:].split('\n',1)[0]
    tempStringLength=tempFile.find(findString)-1

#search the above lines for # comments and save that in a string
    if tempStringLength > -1:
        tempString=tempFile[:tempStringLength]
    elif tempStringLength <= -1:
        tempString=' '
        tempString1=' '
    elif tempString1 == -2:
        tempString1=' '
    tempString=tempString.replace('#','')
#append the file with text

    summary1.append([str(myFile.name),str(tempString),str(tempString1)])
  #  summary1=(
   #     [str(myFile.name),str(tempString),str(tempString1)]
   # )

    for FILENAME, DETAILS, LIBS in (summary1):
        workSheet.write(row, 0, FILENAME)
        workSheet.write(row, 1, DETAILS)
        workSheet.write(row, 2, LIBS)
    row += 1
workBook.close()

print('SAVE DONE')
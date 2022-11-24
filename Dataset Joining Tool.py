# This program multiple .txt datasets into one .csv file
# WRITTEN BY: Austin Daigle
# DATE: 11/24/2022
# VERSION: 1.0v


#===========================================================================
# IMPORTS
import tkinter as tkr
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
#===========================================================================
# FUNCTIONS

# This functions returns the filenames from the file from the directory path
def getFileNameFromPath(filePath):
      #if the filepath parameter is not a string then return a null
      if(type(filePath) != str):
            return
      # return the last element from a list using a split parsing using "/" as the delimiter
      # basically the split return a list of the broken and the [-1] return the last item (the filename)
      # of the broken list.
      return filePath.split('/')[-1]   

# This function return a matrix of all of the data
# that was red from the file within the filepath
# parameter.
def readFileData(filePath):
      # create a matrix to store all of the file data
      rawFileData = []
      #create a file reading object with the filepath as a parameter
      with open(filePath) as fp:
            #create a string to store the result from the file reader
            line = fp.readline()
            #create a count variable for the file readering to process from
            count = 1
            # while there is a readable line present
            while line:
                  #update the rawFileData matrix with the current scanned/red line
                  rawFileData.append((line.strip()))
                  #update string to store the result from the file reader
                  line = fp.readline()
                  #increment the count variable to push the line reading forward
                  count += 1
      #create a matrix for storing all of the parsed and processed rawFileData
      parsedFileData = []
      #for every entry with rawFileData
      for x in range(0,len(rawFileData)):
            #update parsedFileData matrix with tab dilimited split function list from
            # the current line being read from the rawFileData[] matrix
            parsedFileData.append(rawFileData[x].split("\t"))
      # return the parsed data matrix
      return parsedFileData

# filter the all of the rows on weather if they
# have any of the keywords from the keywordList
# if a list (row) has a keyword, it is kept, otherwise
# that row filtered-out.
def filterByKeyWordList(fileContents,keyWordList):     
      #create a matrix to store the filteredContent
      filteredContents = []
      # add the first line to the filteredContents matrix to establish the header.
      # Headers are always kept and never selected out.
      filteredContents.append(fileContents[0])
      # for every element in fileContents
      for x in range(0, len(fileContents)):
            # if the current row (list) has a keyword from the keyWordList parameter
            if any(item in keyWordList for item in fileContents[x]):
                  # update the filteredContents list with the current element of fileContents at x
                  filteredContents.append(fileContents[x])
      # return the filtered result
      return filteredContents

# return a string list with a list of strings from the input min and max years
def getStringYearList(minYear,maxYear):
      # using expressions: convert_list_into_string_list(create_int_list_between_min_&_max)
      return [str(x) for x in [i for i in range(minYear, maxYear+1)]]

# This function merged all matrices in matrix by row 
def mergeAllFileData(matrix):
      mergedContent = []
      # for the (equal) lenght of all of the matrix content in the allDataFromFile list
      for x in range(0,len(matrix[0])):
            # create a list for combining matrices
            combinedList = []
            # for every element in the length of matrix
            for y in range(0,len(matrix)):
                  # merge the current list with the next list
                  combinedList = combinedList + matrix[y][x] 
            # update the merged content
            mergedContent.append(combinedList)
            # clear combinedList list
            combinedList = []
      # return mergedContent
      return mergedContent
      
# return a list containing all of the data from a single column
def getColumnFromMatrix(columnNo,allDataFromFiles):
      # create an empty list to store all of the column data
      column = []
      # for x in range from 0 to the length of allDataFromFiles
      for x in range(0,len(allDataFromFiles)):
            # append the column list with the current elemnt
            #  in the column for the given row and column
            column.append(allDataFromFiles[x][columnNo])
      # return the column list
      return column


# save the contents of the matrix into a file
# using the filename and directory data
# from the filechooser GUI.
def saveToFile(Matrix):
      # create a filedialog to ask the user to choose the location
      # and name of where to save.
      file = filedialog.asksaveasfilename(
      # define the only supported file type as a .csv
      filetypes=[("CSV (comma delimited)", ".csv")],
      # define the default file exetension as a .csv
      defaultextension=".csv")
      # open a file writer using the parameters from the filechooser GUI
      f = open(file,'w')
      # from x in range to the lenght of combinedContent
      for x in range(0,len(combinedContent)):
            # rejoin the list of the current content matrix into a string with
            # with a newline and write that into the file.
            f.write(str(",".join(combinedContent[x])+"\n"))
      # close the file writer resource
      f.close()


#===========================================================================

# This is the list of countries for the dataset keyword filter
countriesFilterList = ["United States","Canada","Mexico","Brazil","Peru"]

# Store the selected dir data in the format: <filename> <directory path>
fileDirAndName = []
# All data from all selected files
allDataFromFiles = []

# Create a file chooser dialog that allows for multiple files to be choosen
# Only enter Text (Tab delimited) (.txt) .txt files ONLY
root = tkr.Tk()
root.withdraw()
selectedFilePaths = filedialog.askopenfilenames(filetypes=[("Tab delimited Text ONLY (.txt)", "*.txt")])

# Abort execution of script if no files have been choosen
if(selectedFilePaths == ""):
      print("[Error] File(s) not selected. Terminating Script")
      raise SystemExit  

# print out all of the directories and filenames
print("Printing all selected files with corresponding directories")
print("===========================================================")
for x in selectedFilePaths:
      print("PATH: "+str(x)+"\n\tFILENAME: "+str(getFileNameFromPath(x)))
      fileDirAndName.append([str(getFileNameFromPath(x)),str(x)])
print("===========================================================")


# Create and add a new matrix for the contents of each 
# Selected file in the selectedFilePaths list and
# filter out the rows that do not have the 
# matched countries and/or within the required date range
# of 1990 to 2013.
for x in range(0,len(selectedFilePaths)):
      allDataFromFiles.append(
            filterByKeyWordList(filterByKeyWordList(
                  readFileData(selectedFilePaths[x]),countriesFilterList),getStringYearList(1990,2013)))

# Trim by an offset of three (Entity, Code, Year)
for x in range(0,len(allDataFromFiles)):
      for y in range(0,len(allDataFromFiles[x])):
            if(x != 0):
                  #print(allDataFromFiles[x][y])
                  allDataFromFiles[x][y] = allDataFromFiles[x][y][3:]

#merge all of the files into one matrix 
combinedContent = mergeAllFileData(allDataFromFiles)

#take all of the data and processes it into a file
saveToFile(combinedContent)


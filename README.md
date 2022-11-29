# Python Dataset Joining Tool

**General Introduction**
This Python script was written to automate the merging of multiple select datasets from 
[(https://ourworldindata.org/)](https://ourworldindata.org/) into a single comma-separated value
file (.csv) with similar row and column dataset formats regarding health and dietary data.

This Python script was written on an "as-is" basis and can be modified to fit alternative use-cases
using the built-in filtering functions/mering functions.

# Description
write this

# Installation and Environment Setup
Ensure that your environment has the following requirements:
* Python 3.0 or above (this script is NOT compatible with 2.0 without refactoring) (also, this script was written in Python 3.11.0)
* Environment path(s) to the correct Python build within your environment
* A Python 3.0 Compatible IDE or terminal/command line that can execute Python scripts

# Pre-Merge Dataset formating "Cleaning" Process:
* Download the datasets from ourworlddata.org
* Open each dataset separately into Excell (do not merge the dataset in Excel)
* Open the "File" tab from the ribbon and Select the "Export" tab
* Select the "Change file type" function
* Within the change file type menu, under "other file types," select "Text (Tab delimited) (*.txt)" and save the file as the same name as the original file name.
* Perform this action separately for each dataset

# Execution:

*IMPORTANT NOTE: The data within the datasets from our from ourworldindata.org have been verified to have been "clean data" (there are no "null" or data mismatches). however, there is a data format issue. Some of the entries have double/single quotes and commas in entries, and .csv reading functions within most python regex functions become unreliable without the use of additional non-standard libraries/dependencies. Therefore each dataset must be converted into a tab-delimited text file for the script to read, parse and process the datasets into a .csv file.  
failing to do this .csv to text file conversion process before auto-merging may result in the parser not functioning correctly or becoming unstable. Please see the section above for steps on how to process this data.

* Download the Python script from the repository or copy the code into an IDE/python file
* Interpret and execute the Python script
* A File Chooser Dialog will appear along with a terminal (or console printout if executed in an IDE)

* Select the desired supported datasets from the file chooser dialog box and select "Open."
* The console output/terminal will printout the directories and files selected within selection order and process notes
* A File Save Dialog will appear and ask you where and what to save the .csv merged output file.

*Keep in mind that the country/code/and year data past the first dataset are removed in the row auto-merging operation to properly merge the datasets. Also, a larger datasets may take more processing time to read, parse, compile, and save.


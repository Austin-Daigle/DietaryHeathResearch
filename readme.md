# README: Python Dataset Joining Tool

**Geneneral Introduction**
This Python script was written to automate the merging of multiple select datasets from 
[(https://ourworldindata.org/)](https://ourworldindata.org/) into a single comma-separated value
file (.csv) with similar row and column dataset formats regarding health and dietary data.

This Python script was written on a "as-is" basis and can be modified to fit alternative use-cases
using the built in filering functions/mering functions.

# Installation and Environment Setup
Ensure that your environment has the following requirements:
* Python 3.0 or above (this script is NOT compatable with 2.0 without refactoring) (also this script was written in Python 3.11.0)
* Environment path(s) to the correct Python build within your environment
* A Python 3.0 Comptable IDE or terminal/commandline that can execute Python scripts

# How to Use:
* Download the Python script from the repository or copy the code into a IDE/python file
* Interpret and execute the Python script
* A File Chooser Dialog will appear along with a terminal (or console printout if executed in a IDE)
* **INPORTANT: Ensure that each of the dataset from ourworldindata.org has been converted into tab-dilimited text file (.txt) otherwise the file chooser 
will not show the datasets as options (also if the text file are not in the correct format the parser will not function correctly and may become unstable). 
* Select the desired supported datasets from the filechooser dialog box and select "Open"
* The console output/terminal will printout the directories and files selected within selection order and process notes
* A File Save Dialog will appear and ask you where and what the save the .csv merged output file as.

*Keep in mind that the country/code/and year data past the first dataset are removed in the row auto-merging operation in order to properly merge the datasets.


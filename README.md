# Python Dataset Joining Tool

**Geneneral Introduction**
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

# Execution:
* Download the Python script from the repository or copy the code into an IDE/python file
* Interpret and execute the Python script
* A File Chooser Dialog will appear along with a terminal (or console printout if executed in an IDE)
*IMPORTANT: Ensure that each of the datasets from ourworldindata.org has been converted into a tab-delimited text file (.txt); otherwise, the file chooser 
will not show the datasets as options (also if the text file is not in the correct format, the parser will not function correctly and may become unstable). 
* Select the desired supported datasets from the file chooser dialog box and select "Open."
* The console output/terminal will printout the directories and files selected within selection order and process notes
* A File Save Dialog will appear and ask you where and what to save the .csv merged output file.

*Keep in mind that the country/code/and year data past the first dataset are removed in the row auto-merging operation to properly merge the datasets. Also, a larger datasets may take more processing time to read, parse, compile, and save.


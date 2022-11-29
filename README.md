# Data and Visual Analytics Project: Dietary Selection and Heath Research

This project aims to analyze the impact of dietary trends in The United State, Canada, Mexico, Peru, and Brazil during the years of 1990 to 2013 to Death and disease data regarding cardiac episodes and cancers.

**How to combine all of the datasets into one:**

* Download the [Dataset Joining Tool.py](https://github.com/Austin-Daigle/DietarySelectionsAndHealthResearch/blob/main/Dataset%20Joining%20Tool.py) Python script or copy the source code into a file/IDE and execute that Python script. All of the resources ([converted tab-dilimited text files](https://github.com/Austin-Daigle/DietarySelectionsAndHealthResearch/tree/main/ConvertedDatasets)) used to create the final [combined dataset](https://github.com/Austin-Daigle/DietarySelectionsAndHealthResearch/blob/main/Combined%20Dietary%20Dataset.csv) can be found [here](https://github.com/Austin-Daigle/DietarySelectionsAndHealthResearch/tree/main/ConvertedDatasets)

* When executed, a file dialog prompt will appear asking which tab-delimited text (.txt) files should be selected (please
remember to convert your dataset into tab-delimited text files using Microsoft Excel or another tool)

* Once the files have been chosen, the program will print out the file directories and names into the terminal 
and will ask you via a save dialog prompt where to save the comma-separated file (.csv) and what to name it. Once
that has been selected, the program will autosave the compiled into into the selected directory with the given name.

* The completed dataset may take a few minutes to fully compiled and appear if large dataset are being processed.

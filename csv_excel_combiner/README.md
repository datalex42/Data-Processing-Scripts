Description:
The csv_excel_combiner.py script is designed to streamline the process of merging multiple CSV and Excel files located in different folders. It reads each file, combines them into a single DataFrame, and logs various stages of the processing for transparency and debugging purposes.

Features:
Input: Reads CSV and Excel files from user-specified directories.
Logging: Detailed logs of each processing step, including file paths, row and column counts, and missing values.
Data Cleaning: Fills missing values with 'is_NULL' and provides an option to deduplicate data based on specified columns.
Output: Saves the combined data as both CSV (encoded in UTF-16) and Excel files.
Error Handling: Catches and logs errors, ensuring that processing can continue even if individual files fail.
User Interaction: Asks the user whether to perform deduplication on the combined data.

How to Use:
Run the script and provide the path to the folder containing the data files.
Follow the prompts to choose whether to deduplicate the data.
Check the output files and logs in the specified directory.

Dependencies:
pandas
logging
os
time

To install the necessary Python packages, run:

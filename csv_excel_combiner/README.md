### <center><p align = "left">`Description`</p> </center>
The csv_excel_combiner.py script is designed to streamline the process of merging multiple CSV and Excel files located in different folders. It reads each file, combines them into a single DataFrame, and logs various stages of the processing for transparency and debugging purposes. This script is ideal for users needing to consolidate and clean data from multiple sources into a single dataset, making subsequent data analysis more straightforward.

<hr>

### <center><p align = "left">`Features`</p> </center>
- Input: Reads CSV and Excel files from user-specified directories.
- Logging: Detailed logs of each processing step, including file paths, row and column counts, and missing values.
- Data Cleaning: Fills missing values with 'is_NULL' and provides an option to deduplicate data based on specified columns.
- Output: Saves the combined data as both CSV (encoded in UTF-16) and Excel files.
- Error Handling: Catches and logs errors, ensuring that processing can continue even if individual files fail.
- User Interaction: Asks the user whether to perform deduplication on the combined data.

<hr>

### <center><p align = "left">`How to Use`</p> </center>
- Run the script and provide the path to the folder containing the data files.
- Follow the prompts to choose whether to deduplicate the data.
- Check the output files and logs in the specified directory.

<hr>

### <center><p align = "left">`Customizable Sections in the Script`</p> </center>
1. Subset for Duplicate Checking:
Adjust the subset argument in the drop_duplicates function to specify the relevant columns for duplicate checking.
```
dedup_df = new_df.drop_duplicates(subset=['XXX'], keep='first')  # Replace XXX with relevant column names or remove subset
dups_df = new_df[new_df.duplicated(subset=['XXX'], keep=False)]  # Replace XXX with relevant column names or remove subset
```

2. Optional Addition of datafile or system Columns:
Add columns like datafile or system to capture additional metadata if necessary.
```
new_df['Datafile'] = f'{file}'  # Enable if necessary to include file path in the dataframe
new_df['System'] = f'{folder}'  # Enable if necessary to include folder name in the dataframe
```
3. File Paths and Formats:
Adjust paths and formats as needed.
```
new_df.to_excel(os.path.join(base, f'{folder}.xlsx'), index=False, header=True)
new_df.to_csv(os.path.join(base, f'{folder}.csv'), index=False, header=True, encoding='utf-16', sep='|')
```
<hr>

### <center><p align = "left">`Dependencies`</p> </center>
- pandas
- logging
- os
- time
- warnings

To install the necessary Python packages, run:

```
pip install pandas
```

<hr>

### <center><p align = "left">`Example Usage`</p> </center>

```
python csv_excel_combiner.py
```

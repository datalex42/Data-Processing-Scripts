### <center><p align = "left">`Description`</p> </center>
This Python script connects to a database, processes CSV and Excel files from a specified directory, and loads the data into a specified table. It includes logging for tracking the data processing and supports batch loading of data to optimize performance.

<hr>

### <center><p align = "left">`Features`</p> </center>
- Input: Reads CSV and Excel files from a user-defined directory.
- Database Connection: Connects to a specified database using user credentials.
- Data Conversion: Converts Excel files to CSV format.
- Table Creation: Creates a new table in the database with dynamic column definitions based on the CSV files.
- Batch Loading: Loads data into the database in batches to handle large datasets efficiently.
- Error Handling: Captures and logs errors during database connection and data processing.

<hr>

### <center><p align = "left">`Usage`</p> </center>
1. Download the script and navigate to its directory.
```
cd path_to_script_directory
```
2. Run the script:
```
python database_csv_loader.py
```
3. Follow the prompts:
```
Enter the security informations when prompted.
Choose tablename and enter the path to the directory containing the data files.
```

<hr>

### <center><p align = "left">`Customizable Sections`</p> </center>
1. Batch Size:
Adjust the batch size for loading data into the database.
```
batches = [data[i:i+999] for i in range(0, len(data), 999)]
```

<hr>

### <center><p align = "left">`Dependencies`</p> </center>
- pandas
- pymssql
- os
- time
- getpass
- logging

### <center><p align = "left">`Install Dependencies`</p> </center>
```
pip install pandas pymssql
```
<hr>

### <center><p align = "left">`Example Usage`</p> </center>
```
python database_csv_loader.py
```

<p align="right">(<a href="#top">⬆️ back to top</a>)</p>

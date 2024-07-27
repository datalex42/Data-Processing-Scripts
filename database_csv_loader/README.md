Description:
This Python script connects to a database, processes CSV and Excel files from a specified directory, and loads the data into a specified table. It includes logging for tracking the data processing and supports batch loading of data to optimize performance.

<hr>

Features:
- Input: Reads CSV and Excel files from a user-defined directory.
- Database Connection: Connects to a specified database using user credentials.
- Data Conversion: Converts Excel files to CSV format.
- Table Creation: Creates a new table in the database with dynamic column definitions based on the CSV files.
- Batch Loading: Loads data into the database in batches to handle large datasets efficiently.
- Error Handling: Captures and logs errors during database connection and data processing.

<hr>

Usage:
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
Enter the database password when prompted.
Enter the path to the directory containing the data files.
```

<hr>

Customizable Sections:
1. Server and User Credentials:
Adjust the server, user, and database variables as needed.
```
server = r'Server'
user = r'User'
database = 'Db'
```
2. Data Path:
Modify the data_path to specify the directory containing your data files.
```
data_path = input('Insert Datapath: ')
```
3. Batch Size:
Adjust the batch size for loading data into the database.
```
batches = [data[i:i+999] for i in range(0, len(data), 999)]
```

<hr>

Dependencies:
- pandas
- pymssql
- os
- time
- getpass
- logging

Install Dependencies:
```
pip install pandas pymssql
```
<hr>

Example Usage:
```
python database_csv_loader.py
```

import os
import pandas as pd
import pymssql
import time
from getpass import getpass
import logging

# Configure logging
logging.basicConfig(filename='database_loader.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_db():
    server = r'Server'
    user = r'User'
    database = 'Db'
    password = getpass()

    try:
        conn = pymssql.connect(server=server, user=user, database=database, password=password)
        print("Verbindung hergestellt.")
        logging.info("Connection to the database established.")
        return conn
    except Exception as e:
        print("Fehler beim Herstellen der Verbindung:", e)
        logging.error(f"Error connecting to the database: {e}")
        return None

def process_data():
    data_path = input('Insert Datapath: ')
    tablename = 'tablename'

    print('Files are being checked...')
    logging.info('Files are being checked...')
    for file in os.listdir(data_path):
        time.sleep(1)
        print(f'Converting file {file}')
        logging.info(f'Converting file {file}')
        
        if file.endswith('csv'):
            continue
        elif file.endswith('xlsx'):
            data = pd.read_excel(os.path.join(data_path, file))
            data.to_csv(os.path.join(data_path, f'{os.path.splitext(file)[0]}.csv'), index=False, header=True, encoding='utf-16')
        else:
            print(f'File format of {file} not known!')
            logging.warning(f'Unknown file format: {file}')

    return tablename, data_path

def create_and_load_table(conn, tablename, data_path):
    print('Table creation in progress...')
    logging.info('Table creation in progress...')
    df = pd.read_csv(os.path.join(data_path, os.listdir(data_path)[0]), low_memory=False, encoding='utf-16')
    columns = list(df.columns)

    create = f'DROP TABLE IF EXISTS {tablename}; CREATE TABLE {tablename}(' + ', '.join([f'[{col}] NVARCHAR(MAX)' for col in columns]) + ')'
    cursor = conn.cursor()
    cursor.execute(create)
    conn.commit()
    logging.info(f'Table {tablename} created with columns: {columns}')

    for file in os.listdir(data_path):
        if not file.endswith('.csv'):
            continue

        print(f'Starting data implementation for file: {file}')
        logging.info(f'Starting data implementation for file: {file}')
        time.sleep(1)
        filepath = os.path.join(data_path, file)
        data = pd.read_csv(filepath, low_memory=False, encoding='utf-16')

        batches = [data[i:i+999] for i in range(0, len(data), 999)]

        count = 0
        for batch in batches:
            print(f'Processing Batch {count}')
            logging.info(f'Processing Batch {count}')
            insert = f"INSERT INTO dbo.{tablename} ({', '.join([f'[{d}]' for d in data.columns])}) VALUES"
            batch_copy = batch.copy()
            batch_copy['sql'] = batch_copy.apply(lambda x: '(' + ','.join([f"'{str(val).replace('\'', '\'\'')}'" for val in x]) + ')', axis=1)
            batch_sql = ','.join(batch_copy['sql'].to_list())

            cursor = conn.cursor()
            cursor.execute(insert + batch_sql)
            conn.commit()
            count += 1
        logging.info(f"{file} successfully inserted into table {tablename}")

if __name__ == '__main__':
    conn = connect_to_db()
    if conn:
        tablename, data_path = process_data()
        create_and_load_table(conn, tablename, data_path)
    else:
        logging.error("Script terminated due to connection error.")
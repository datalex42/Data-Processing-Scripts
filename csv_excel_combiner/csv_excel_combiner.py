import os
import time
import pandas as pd
import logging
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning) # Line 30, no solution jet

   
def combine():
    base = input('Insert Data Path: ') #Datapath to folder
    count = 0
    logging.basicConfig(filename = f'logfile_{count}.csv', format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S', level = logging.INFO) #logfile will be in script location

    for folder in os.listdir(base):
        print('Data processing started...') 
        new_base = os.path.join(base, folder)
        if os.path.isdir(new_base): #Put data to combine in a folder, if you need to combine different data in own groups, create several folders
            folder_name = os.path.basename(new_base)
            new_df = pd.DataFrame()
            logging.info(f'Started | | Columns | Rows | NAs | is_NULL')
            logging.info(f'Log Type | Information')
            for file in os.listdir(new_base):
                if file.endswith('.xlsx') or file.endswith('.csv'): #read xlsx or csv data
                    try:
                        new_data = (pd.read_excel(os.path.join(new_base, file), header=0, names=[col.strip().title() for col in pd.read_excel(os.path.join(new_base, file), nrows=1).columns]) 
                        if file.endswith('.xlsx') else pd.read_csv(os.path.join(new_base, file), sep=';', encoding='utf-8', header=0, names=[col.strip().title() for col in pd.read_csv(os.path.join(new_base, file), 
                        encoding='utf-8', sep=';', nrows=1).columns])) # Read data      
                        logging.info(f'File | {os.path.join(new_base, file)}') #Log: Datapath
                        logging.info(f'Pre | Before concatenation | {len(new_df.columns)} | {len(new_df)} | {new_data.isna().sum().sum()}') #Log: length columns, lines, N/As
                        new_data.fillna('is_NULL', inplace=True) #Ignore futurewarnining, fill all NA-Values with is_NULL
                        if len(new_df.columns) == 0 and len(new_df) == 0:
                            new_df = new_data
                            logging.info(f'Post | After concatenation (new file rows {len(new_data)}) | {len(new_df.columns)} | {len(new_df)} | {new_data.isna().sum().sum()} | {new_data.isin(['is_NULL']).sum().sum()}')  #Count N/A values after convertion, count is_NULL values after convertion
                            logging.info(f'Finished | {file} processed\n')
                            new_df['Datafile'] = f'{file}'  #activate if necessary to implement Filepath in dataframe
                        else:
                            new_df = pd.concat([new_df, new_data], axis=0) #Concat dataframes
                            logging.info(f'Post | After concatenation (new file rows {len(new_data)}) | {len(new_df.columns)} | {len(new_df)} | {new_data.isna().sum().sum()} | {new_data.isin(['is_NULL']).sum().sum()}')  #Count N/A values after convertion, count is_NULL values after convertion
                            logging.info(f'Finished | {file} processed\n')
                            new_df['Datafile'] = new_df['Datafile'].fillna(f'{file}') #activate if necessary to implement Filepath in dataframe
                    except Exception as e:
                        logging.error(f'Error: {e} in file {file}')
                        print(f'Error: {e} in file {file}')
                else:
                    logging.warning(f'Warning: File {file} is not in the expected format')
                    print(f'Warning: File {file} is not in the expected format')
    
        new_df['System'] = f'{folder}' #Activate if necessary, add column in data with foldername
        
        if os.path.isdir(new_base):
            total_rows = sum(
            len(pd.read_excel(os.path.join(new_base, file))) if file.endswith('.xlsx') else len(pd.read_csv(os.path.join(new_base, file), sep=';', encoding='utf-8'))
            for file in os.listdir(new_base) if file.endswith('.xlsx') or file.endswith('.csv')
                ) #check if count lines of new df is same like all single data
            if len(new_df) == total_rows:
                if len(new_df) < 500000:
                    new_df.to_excel(os.path.join(base, f'{folder}.xlsx'), index=False, header=True) #save to xlsx

                new_df.to_csv(os.path.join(base, f'{folder}.csv'), index=False, header=True, encoding='utf-16', sep='|') #save to csv
                logging.info(f'Final Column Count for {folder} (+2 for added File and System Column): {len(new_df.columns)}') #logging
                logging.info(f'Final Row Count for {folder}: {len(new_df)}')
                logging.info('All checks passed. Data processing completed successfully.\n')
                print('All checks passed. Data processing completed successfully.')
                count += 1
                
                drop_duplicates = input(f'\nDo you want to continue and look for duplicates in {folder} and delete them? (yes/no): ').lower() #Deduplication process
                if drop_duplicates == 'yes':
                    print('Starting deduplication...')
                    time.sleep(1)
                    logging.info(f'Pre-Drop Row Count for {folder}: {len(new_df)}')
                    dedup_df = new_df.drop_duplicates(subset=['XXX'], keep='first') #Adjust subset columns, or remove subset 
                    logging.info(f'Post-Drop Row Count for {folder}: {len(dedup_df)}\n')
                    if new_df.shape == dedup_df.shape:
                        print('No duplicates found')
                    else: #If duplicates are found
                        if len(new_df) < 500000:
                            dups_df = new_df[new_df.duplicated(subset=['XXX'], keep=False)] #Adjust subset columns, or remove subset
                            dedup_df.to_excel(os.path.join(base, f'{folder}_deduplicated.xlsx'), index=False, header=True) #Saving deduplicated file
                            dups_df.to_excel(os.path.join(base, f'{folder}_duplicates.xlsx'), index=False, header=True) #Saving all duplicates in one file
                        dups_df = new_df[new_df.duplicated(subset=['XXX'], keep=False)] #Adjust subset columns, or remove subset
                        dedup_df.to_csv(os.path.join(base, f'{folder}_deduplicated.csv'), index=False, header=True, encoding='utf-16', sep='|')
                        dups_df.to_csv(os.path.join(base, f'{folder}_duplicates.csv'), index=False, header=True, encoding='utf-16', sep='|')
                        print(f'{len(dedup_df)} unique rows saved to {folder}_deduplicated.csv')
                        print(f'{len(dups_df)} duplicates saved to {folder}_duplicates.csv')
                        logging.info(f'Total duplicates Count for {folder}: {len(dups_df)}\n\n')
                        print('Deduplication completed successfully')

                else:
                    print('Deduplication aborted')
            else:
                logging.error(f'Error: Row count mismatch in folder {folder}') #If rows do not match = error
                print('The data processing has been terminated. Relevant information can be found in the log')

        else:
            logging.error(f'Skipped: {new_base} not a directory')
            print(f'Skipped: {new_base} not a directory')

if __name__ == '__main__':
    combine()

from genericpath import isdir
import pandas as pd
import os

from pyparsing import originalTextFor

dir = './train.parquet'
folder_name_prefix = f'{dir}/partition_id='
files = []

for i in range(0, 10):
    folder = folder_name_prefix + str(i)
    for file in os.listdir(folder):
        files.append(f'{folder}/{file}')
        print(f'Read {folder}/{file}')

# merge the parquet files from the training directory
df = pd.concat([pd.read_parquet(file) for file in files])
# save the merged file to a new parquet file
df.to_parquet('./training_dataset.parquet')

print('Merge completed')
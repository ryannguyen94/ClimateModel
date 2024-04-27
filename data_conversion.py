import pandas as pd
from tqdm import tqdm
import gc

def convert_csv_to_parquet():
    for file in tqdm(['sample_submission.csv']):
        df = pd.read_csv(f'data/{file}')
        df.to_parquet(f'data/{file.replace(".csv", ".parquet")}')

        gc.collect()

def convert_big_csv_to_parquet():
    # Path to your large CSV file
    csv_file_path = 'data/train.csv'

    # Define the chunk size based on your system's memory and the data's characteristics
    chunk_size = 1000  # This number might need to be adjusted

    # Create an iterator object for chunks
    csv_chunk = pd.read_csv(csv_file_path, chunksize=chunk_size)

    # Iterate over the chunks and save each as a separate Parquet file
    for i, chunk in enumerate(csv_chunk):
        # Define the path for the output Parquet file
        parquet_file_path = f'data/train_chunk_{i+1}.parquet'

        # Convert the chunk to a Parquet file
        chunk.to_parquet(parquet_file_path)

        # Optional: Print out the status
        print(f'Chunk {i+1} written to {parquet_file_path}')
        break

if __name__ == '__main__':
    convert_csv_to_parquet()
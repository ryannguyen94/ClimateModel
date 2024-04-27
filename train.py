import pandas as pd

import gc

def train():
    df = pd.read_parquet('data/train_chunk_1.parquet')
    print(df)

if __name__ == '__main__':
    train()
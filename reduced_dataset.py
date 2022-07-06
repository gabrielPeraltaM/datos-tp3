import sklearn.utils.random as sk_random
import pandas as pd
from typing import List


GROUP_NUMBER = 11
DATASET_FILE_PATH = "./data/train_data.csv"
OUTPUT_FILE_PATH = "./data/group11_data.csv"
CHUNK_SIZE = 100000


def get_seed_for_group(group_number: int) -> int:
    return (31416 * group_number) % 1000


def read_csv_in_chunks_and_count(file: str, chunk_size: int):
    counter = 0
    for chunk in pd.read_csv(filepath_or_buffer=file, chunksize=chunk_size):
        counter = counter + len(chunk)
        print(counter)

    return counter


def read_csv_and_create_subset(file: str, output_file: str, filtering_indexes: List[int], chunk_size: int):
    for chunk in pd.read_csv(filepath_or_buffer=file, chunksize=chunk_size):
        chunk = chunk[chunk.index.isin(filtering_indexes)]
        chunk.to_csv(output_file, header=True, mode='a')


if __name__ == "__main__":
    total_number_of_rows = read_csv_in_chunks_and_count(file=DATASET_FILE_PATH, chunk_size=CHUNK_SIZE)
    number_of_sample_rows = total_number_of_rows * 0.05

    sample = sk_random.sample_without_replacement(
        total_number_of_rows,
        number_of_sample_rows,
        random_state=get_seed_for_group(GROUP_NUMBER)
    )

    read_csv_and_create_subset(file=DATASET_FILE_PATH, output_file=OUTPUT_FILE_PATH,
                               filtering_indexes=sample, chunk_size=CHUNK_SIZE)

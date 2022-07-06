import sklearn.utils.random as sk_random
import pandas as pd
from typing import List

from cli_arguments import parser


def get_seed_for_group(group_number: int) -> int:
    return (31416 * group_number) % 1000


def read_csv_in_chunks_and_count(file: str, chunk_size: int):
    counter = 0
    for chunk in pd.read_csv(filepath_or_buffer=file, chunksize=chunk_size):
        counter = counter + len(chunk)
        print(counter)

    return counter


def read_csv_and_create_subset(file: str, output_file: str, filtering_indexes: List[int], chunk_size: int):
    count = 0
    for chunk in pd.read_csv(filepath_or_buffer=file, chunksize=chunk_size):
        chunk = chunk[chunk.index.isin(filtering_indexes)]
        count += len(chunk)
        print(count)
        chunk.to_csv(output_file,  mode='a', index=False)


if __name__ == "__main__":
    args = vars(parser.parse_args())

    input_file = args['input']
    output_file = args['output']
    percentage = args['percentage']
    chunk_size = args['chunk_size']
    group_number = args['group_number']

    total_number_of_rows = read_csv_in_chunks_and_count(file=input_file, chunk_size=chunk_size)
    number_of_sample_rows = total_number_of_rows * percentage

    sample = sk_random.sample_without_replacement(
        total_number_of_rows,
        number_of_sample_rows,
        random_state=get_seed_for_group(group_number)
    )

    read_csv_and_create_subset(file=input_file, output_file=output_file,
                               filtering_indexes=sample, chunk_size=chunk_size)

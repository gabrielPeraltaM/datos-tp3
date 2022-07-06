import argparse

parser = argparse.ArgumentParser(description="Create a subset for TP3 Orga")

parser.add_argument("--chunk", type=int, dest="chunk_size", help="Size of the chunk for each read/write operation",
                    required=True)
parser.add_argument("--group", type=int, dest="group_number",  help="Group number", required=True)
parser.add_argument("--input", type=str, dest="input",  help="Input file with the data to process", required=True)
parser.add_argument("--output", type=str, dest="output", help="Output file with the subset data", required=True)
parser.add_argument("--percentage", dest="percentage",
                    type=float, help="Percentage of the total data to use in the subset",
                    required=True)
parser.add_argument("--size", type=int, dest="size",
                    help="Optional size of the file.If not specified, the script calculates it, but takes longer to finish")

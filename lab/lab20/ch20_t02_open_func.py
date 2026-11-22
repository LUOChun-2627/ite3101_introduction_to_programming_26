import os
my_file = open("ch20_t02_output.txt", "r+")
file_path_name = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "inputs/ch20_t02_output.txt")

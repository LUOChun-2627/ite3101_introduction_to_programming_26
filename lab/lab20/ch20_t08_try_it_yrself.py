import os
file_path_name = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "outputs/ch20_t08o_output.txt")
my_file = open(file_path_name,"w")
my_file.write("Hello, file!")
my_file.flush()

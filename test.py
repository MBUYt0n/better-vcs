import py7zr
import os
import subprocess


def compress_file(input_file, output_file):
    with py7zr.SevenZipFile(output_file, "w") as archive:
        archive.write(input_file, arcname=input_file)
    print(os.path.getsize(input_file))
    print(os.path.getsize(output_file))


def decompress_file(input_file, output_dir):
    with py7zr.SevenZipFile(input_file, "r") as archive:
        archive.extractall(path=output_dir)




def diff_files(file1, file2):
    result = subprocess.run(["diff", file1, file2], capture_output=True, text=True)
    if result.returncode == 0:
        pass
    else:
        print("Differences found:")
        print(result.stdout) 

diff_files("CCO31.xml", "CC03.xml")

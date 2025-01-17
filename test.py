import py7zr
import os
import subprocess
import time

def compress_file(input_file, output_file):
    with py7zr.SevenZipFile(output_file, "w") as archive:
        archive.write(input_file, arcname=input_file)
    print(os.path.getsize(input_file))
    print(os.path.getsize(output_file))


def decompress_file(input_file, output_dir):
    with py7zr.SevenZipFile(input_file, "r") as archive:
        archive.extractall(path=output_dir)




def diff_files(file1, file2):
    result = subprocess.run(["diff", "--strip-trailing-cr", file1, file2], capture_output=True, text=True)
    if result.returncode == 0:
        pass
    else:
        print("Differences found:")
        with open("diff.txt", "a") as f:
            f.write("||")
            f.write(time.ctime() + "\n")
            f.write(result.stdout)
            f.close()
        print(result.stderr)



l = os.listdir("/home/shusrith/Downloads")
l = sorted([i for i in l if ".py" in i])
for i in range(0, len(l) - 1):
    print(l[i], l[i + 1])
    diff_files(f"/home/shusrith/Downloads/{l[i]}", f"/home/shusrith/Downloads/{l[i + 1]}")


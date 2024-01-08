# File: TOOLS/col.py
import subprocess
import shutil
import tempfile

def myzip(mo1, mo2, output_file):
    result = list(zip(mo1, mo2))
    
    with open(output_file + ".txt", "w") as f:
        for item in result:
            f.write(str(item) + "\n")

    # Use a temporary file to store the content
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        for item in result:
            temp_file.write(str(item).encode('utf-8') + b'\n')

    # Create the ZIP archive from the temporary file
    shutil.make_archive(output_file, 'zip', '.', temp_file.name)

    return result
# col.py

def some_function():
    print("Executing some_function in col.py")

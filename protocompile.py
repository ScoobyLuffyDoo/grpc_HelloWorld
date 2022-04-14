import os 

filename= input("What is the file name ?\n")
folderLocation = input("What is the folder name ?\n")
outputfolder = input("what is the output folder fro the generated files ?\n")

command =f"""
python -m grpc_tools.protoc -I ./{folderLocation} --python_out=./{outputfolder}/ --grpc_python_out=./{outputfolder}/ ./{folderLocation}/{filename}.proto
"""

try:
    os.system(f'mkdir {outputfolder}')
    os.system(command)
except e as error:
    print(e)

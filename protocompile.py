import os 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

compileCalled =False
protoFolderFound = False
protoFileFound = False
outputFolderFound = False
while compileCalled == False:
    # Get User Input To Generating client and server code
    while protoFolderFound == False:
        folderLocation = input(f"{bcolors.OKGREEN}In what Folder dir is the proto file located?\n{bcolors.ENDC}")
        pathExists = os.path.exists(folderLocation) 
        if pathExists ==False:
            print(f"{bcolors.FAIL}\n==> Folder Does Not Exist !!\n{bcolors.ENDC}")
            compileCalled =False
            protoFolderFound =False
            continue
        else:
            protoFolderFound =True
    while protoFileFound == False:
        fileName = input(f"{bcolors.OKGREEN}What is your Proto file name ?\n{bcolors.ENDC}").removesuffix('.proto')
        filepath =f'./{folderLocation}/{fileName}.proto'
        fileExists = os.path.exists(filepath)
        if fileExists == False:
            print(f"{bcolors.FAIL}\n==> Proto file does not exist !!\n{bcolors.ENDC}")
            compileCalled =False
            protoFileFound =False
            continue
        else:
            protoFileFound =True
    while outputFolderFound == False:
        outputfolder = input(f"{bcolors.OKGREEN}Folder name for Generating client and server code ?\n{bcolors.ENDC}")   
        outputhFolderExists = os.path.exists(outputfolder) 
        if outputhFolderExists ==False:
            print(f"{bcolors.FAIL}\n==> Folder Does Not Exist and will be Created !!\n{bcolors.ENDC}")
            os.system(f'mkdir {outputfolder}')
            outputhFolderExists = os.path.exists(outputfolder)
            if outputhFolderExists ==False:
                print(f"{bcolors.FAIL}\n==> Folder Does Not Exist and could not be Created !!\n{bcolors.ENDC}")
                compileCalled =False
                outputFolderFound = False
                continue
            else:
                compileCalled=False
                outputFolderFound=True
        else:
            compileCalled=False
            outputFolderFound=True
    try:    
        inputCommand =f"python -m grpc_tools.protoc -I ./{folderLocation} "
        pythonOutputFolder=f"--python_out=./{outputfolder}/ "
        GrpcOutputfolder=f"--grpc_python_out=./{outputfolder}/"
        ProtoFolderLocation=f" ./{folderLocation}"
        fileNameCommand =f"/{fileName}.proto"
        CompilerCommand= f'{inputCommand}{pythonOutputFolder}{GrpcOutputfolder}{ProtoFolderLocation}{fileNameCommand}'
        os.system(CompilerCommand)
        print(f"{bcolors.OKGREEN }Generating client and server code Complete{bcolors.ENDC}")    
        compileCalled =True 
    except Exception as e :
        print(f'{bcolors.FAIL}{e}{bcolors.ENDC}')



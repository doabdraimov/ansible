import psutil, os, time, subprocess


def getScriptsFiles(path):
    '''
    Looking for python files and append its into list.
    '''
    scripts_files = []
    try:
        files = os.listdir(path)
        for file in files:
            #If this python files and not self file then append it into list 
            if '.py' in file and os.path.basename(__file__) != file:
                scripts_files.append(file)
        return scripts_files
    except (FileNotFoundError):
        return False


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName in proc.cmdline():
            #if processName.lower() in proc.cmdline().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


def main():
    path = '/home/robot/scripts'
    while True:
        scripts =getScriptsFiles(path)
        if scripts:
            for script in scripts:
                if  not checkIfProcessRunning(script):
                    print('starting process', script)
                    process = subprocess.Popen(['python3', script], 
                                               stdout=subprocess.DEVNULL)
        else:
            print('getScriptsFiles object is not iterable')
        print('script runnning')
        time.sleep(5)
    

if __name__ == '__main__':
    main()

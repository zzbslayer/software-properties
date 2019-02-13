from subprocess import Popen, PIPE
import os
import Util

class Command(object):
    def __init__(self, path=None):
        if (path==None):
            self.path = "C:\Program Files\MATLAB\R2018a\etc\win64"
        else:
            self.path = path

        LM_LICENSE_FILE = os.environ.get('LM_LICENSE_FILE')
        if not LM_LICENSE_FILE:
            LM_LICENSE_FILE = "C:\Program Files\MATLAB\R2018a\etc\license.dat"
        
        prefix = "\""+ self.path + "\lmutil.exe\""
        self.command_dic = {
                        "status":  prefix + "lmstat MATLAB", \
                        "others": "dir"
                    }
        
    def _command(self, key):
        return self.command_dic[key]


    ''' example
    {
        'MATLAB':{
            total: 10000,
            use: 100,
            metadata: [whatever]
            user_data: [user1, user2, ...]
        },
        'Some Module':{
            ...
        },
        ...
    }
    '''
    def status():
        pipe = Popen(self._command("status"), shell=True, stdout=PIPE, stderr=PIPE)
        result = {}
        while True:
            line = Util.readline(pipe)
            if line == -1: 
                break 
            elif (line == BLANK):
                continue

            # get some module
            if (line[:9] == "Users of "):
                split_line = line.split(' ')
                module = split_line[2][:-1]
                total = split_line[6]
                use = split_line[12]
                result[module] = {"total":total, "use":use}

                # read meta data of some module
                metadata = []
                for i in range(4):
                    line = Util.readline(pipe)
                    if line == BLANK:
                        continue
                    metadata.append(line[2:])
                result[module]["metadata"] = metadata

                line = Util.readline(pipe)
                if line == -1:
                    break

                # read user data of some module
                user_data = []
                while(line[:9] != "Users of "):
                    line = Util.readline(pipe)
                    if line == -1:
                        break
                    if line == BLANK:
                        continue
                    user_data.append(line[4:])
                result[module]["user_data"] = user_data
        return result
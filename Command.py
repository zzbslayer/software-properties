from subprocess import Popen, PIPE
import os
import Util

BLANK = '\r\n'

class Command(object):
    def __init__(self, path=None):
        if (path==None):
            self.path = "C:\Program Files\MATLAB\R2018a\etc\win64"
        else:
            self.path = path

        LM_LICENSE_FILE = os.environ.get('LM_LICENSE_FILE')
        if not LM_LICENSE_FILE:
            LM_LICENSE_FILE = "C:\Program Files\MATLAB\R2018a\etc\license.dat"
        
        prefix = "\""+ self.path + "\lmutil.exe\" "
        self.command_dic = {
                        "all_status":  prefix + "lmstat -a", \
                        "status_by_module": prefix + "lmstat -f ", \
                        "others": "dir"
                    }
        
    def _command(self, key):
        return self.command_dic[key]

    def status_by_module(self, module):
        pipe = Popen(self._command("status_by_module") + module, shell=True, stdout=PIPE, stderr=PIPE)
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
                # ["Users", "of", "Distrib_Computing_Toolbox:", ... ]
                module = split_line[2][:-1]
                total = split_line[6]
                use = split_line[12]
                result[module] = {"total":total, "use":use}
                if (use != '0'):
                    # read meta data of some module
                    metadata = []
                    _ = Util.readline(pipe)

                    line = Util.readline(pipe)
                    metadata.append(line[2:])
                    line = Util.readline(pipe)
                    metadata.append(line[2:])
                    line = Util.readline(pipe)
                    metadata.append(line[2:])

                    result[module]["metadata"] = metadata

                    line = Util.readline(pipe)
                    if line == -1:
                        break

                    # read user data of some module
                    user_data = []
                    while(True):
                        line = Util.readline(pipe)
                        if line == -1:
                            break
                        if line == BLANK:
                            break
                        user_data.append(line[4:])

                    result[module]["user_data"] = user_data
                else:
                    result[module]["user_data"] = []
                    result[module]["metadata"] = []
        return result


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
    def all_status(self):
        pipe = Popen(self._command("all_status"), shell=True, stdout=PIPE, stderr=PIPE)
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
                # ["Users", "of", "Distrib_Computing_Toolbox:", ... ]
                module = split_line[2][:-1]
                total = split_line[6]
                use = split_line[12]
                result[module] = {"total":total, "use":use}
                if (use != '0'):
                    # read meta data of some module
                    metadata = []
                    _ = Util.readline(pipe)

                    line = Util.readline(pipe)
                    metadata.append(line[2:])
                    line = Util.readline(pipe)
                    metadata.append(line[2:])
                    line = Util.readline(pipe)
                    metadata.append(line[2:])

                    result[module]["metadata"] = metadata

                    line = Util.readline(pipe)
                    if line == -1:
                        break

                    # read user data of some module
                    user_data = []
                    while(True):
                        line = Util.readline(pipe)
                        if line == -1:
                            break
                        if line == BLANK:
                            break
                        user_data.append(line[4:])

                    result[module]["user_data"] = user_data
                else:
                    result[module]["user_data"] = []
                    result[module]["metadata"] = []
        return result

if __name__ == "__main__":
    cmd = Command()
    print(cmd.status_by_module("SIMULINK"))
    print(cmd.all_status()["SIMULINK"])
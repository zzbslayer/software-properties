from subprocess import Popen, PIPE
import os
import Util

BLANK = '\r\n'
SERVER_HOST = "matlab2018b"

def get_user_data(raw_user_data):
    user_data = []
    for i in raw_user_data:
        split_user_data = i.split(' ')
        for j in range(len(split_user_data)):
            if (split_user_data[j].split('/')[0][1:] == SERVER_HOST):
                break
        server = split_user_data[j].split('/')
        server_host = SERVER_HOST
        port = server[1]
        handle = split_user_data[j+1][:-2]
        checkout_time = split_user_data[j+2] + ' ' + split_user_data[j+3] + ' ' + split_user_data[j+4] + ' ' + split_user_data[j+5][:-2]
                    
        one_user = { 
            "server_host": server_host, \
            "port": port, \
            "handle": handle, \
            "checkout_time": checkout_time
            }
        user_data.append(one_user)
    return user_data

class Command(object):
    def __init__(self, path=None):
        if (path==None):
            self.path = "C:\Program Files\MATLAB\R2018a\etc\win64"
        else:
            self.path = path

        LM_LICENSE_FILE = os.environ.get('LM_LICENSE_FILE')
        prefix = "\"" + self.path + "\lmutil.exe\" "

        assert(LM_LICENSE_FILE != "")
        #LM_LICENSE_FILE = "C:\Program Files\MATLAB\R2018a\etc\license.dat"
            
        self.command_dic = {
                        "lmstatAll":  lambda: prefix + "lmstat -a", \
                        "lmstatByModule": lambda module: (prefix + "lmstat -f " + module), \
                        "lmremoveByDevice": lambda feature,user,user_host,display:(prefix+"lmremove "+feature+" "+user+" "+user_host+" "+display), \
                        "lmremoveByPort": lambda feature, server_host, port, handle:(prefix+"lmremove "+feature+" "+server_host+" "+port+" "+" "+handle), \
                        "others": "dir"
                    }
        
    def _command(self, key):
        return self.command_dic[key]

    def lmstatByModule(self, module):
        pipe = Popen(self._command("lmstatByModule")(module), shell=True, stdout=PIPE, stderr=PIPE)
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
                    raw_user_data = []
                    while(True):
                        line = Util.readline(pipe)
                        if line == -1:
                            break
                        if line == BLANK:
                            break
                        raw_user_data.append(line[4:])
                    user_data = get_user_data(raw_user_data)
                        
                    result[module]["user_data"] = user_data
                else:
                    result[module]["user_data"] = []
                    result[module]["metadata"] = []
        return result

    def lmstatAll(self):
        pipe = Popen(self._command("lmstatAll")(), shell=True, stdout=PIPE, stderr=PIPE)
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
                    raw_user_data = []
                    while(True):
                        line = Util.readline(pipe)
                        if line == -1:
                            break
                        if line == BLANK:
                            break
                        raw_user_data.append(line[4:])

                    user_data = get_user_data(raw_user_data)
                    result[module]["user_data"] = user_data
                else:
                    result[module]["user_data"] = []
                    result[module]["metadata"] = []
        return result

    def lmremoveByDevice(self, feature, user,user_host, display):
        pipe = Popen(self._command("lmremoveByDevice")(feature, user, user_host, display), shell=True, stdout=PIPE, stderr=PIPE)
    
    def lmremoveByPort(self, feature, server_host, port, handle):
        pipe = Popen(self._command("lmremoveByPort")(feature, server_host, port, handle), shell=True, stdout=PIPE, stderr=PIPE)

    def lmborrow(self):
        pipe = Popen(self._command("lmstatAll"), shell=True, stdout=PIPE, stderr=PIPE)

if __name__ == "__main__":
    cmd = Command()
    print(cmd.lmstatByModule("SIMULINK"))

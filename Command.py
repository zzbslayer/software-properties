from subprocess import Popen, PIPE
import os
import Util

BLANK = '\r\n'

def get_user_data(raw_user_data, software):
    user_data = []
    for i in raw_user_data:
        if software == "matlab":
            one_user = get_matlab_user(i)
        elif software == "solidworks":
            one_user = get_solidworks_user(i)
        user_data.append(one_user)
    return user_data

def get_matlab_user(line):
    index = -6
    split_user_data = line.split(' ')
    #print(split_user_data[index])
    server = split_user_data[index].split('/')
    server_host = server[0][1:]
    port = server[1]
    handle = split_user_data[index+1][:-2]
    checkout_time = split_user_data[index+2] + ' ' 
    checkout_time += split_user_data[index+3] + ' '
    checkout_time += split_user_data[index+4] + ' '
    checkout_time += split_user_data[index+5][:-2]
    version = split_user_data[-7]
    user = ''
    for i in split_user_data:
        if i == version:
            break
        user += i
        user += ' '
                
    one_user = { 
        "user": user, \
        "version": version, \
        "server_host": server_host, \
        "port": port, \
        "handle": handle, \
        "checkout_time": checkout_time
    }
    return one_user

def get_solidworks_user(line):
    split_user_data = line.split(' ')
    checkout_time = split_user_data[-4] + ' '
    checkout_time += split_user_data[-3] + ' '
    checkout_time += split_user_data[-2] + ' '
    checkout_time += split_user_data[-1] + ' '
    version = split_user_data[-5][:-1]
    user = ''
    for i in split_user_data:
        if i == version + ",":
            break
        user += i
        user += ' '
    one_user = {
        "user": user, \
        "version": version, \
        "checkout_time": checkout_time
    }
    return one_user


class Command(object):
    def __init__(self, path=None):
        if (path==None):
            self.path = "C:\\Program Files\\MATLAB\\R2018a\\etc\\win64"
        else:
            self.path = path

        #DEFAULT_LM_LICENSE_FILE = os.environ.get('LM_LICENSE_FILE')
        #DEFAUTL_LMUTIL_PREFIX = "\"C:\\Program Files\\MATLAB\\R2018a\\etc\\"
        
        executable = lambda name: "\"{}\\{}.exe\"".format(self.path, name)

        lmutil = executable("lmutil")
        lmgrd = executable("lmgrd")
        self.LM_LICENSE_FILE_PREFIX = os.getcwd()
            
        self.command_dic = {
                        "lmstatAll":  lambda lic_file: "{} lmstat -c {} -a".format(lmutil, lic_file),
                        "lmstatByModule": lambda lic_file, module: "{} lmstat -c {} -f {}".format(lmutil, lic_file, module),
                        "start": lambda lmgrd_lic: "{} -c {}".format(lmgrd, lmgrd_lic),
                        "shutdown": lambda lmgrd_lic: "echo y | {} lmdown -c {}".format(lmutil, lmgrd_lic),
                        "lmremoveByDevice": lambda feature,user,user_host,display:(lmutil+" lmremove "+feature+" "+user+" "+user_host+" "+display),
                        "lmremoveByPort": lambda feature, server_host, port, handle:(lmutil+" lmremove "+feature+" "+server_host+" "+port+" "+" "+handle),
                    }
        
    def _command(self, key):
        return self.command_dic[key]

    def check(self, lic_file):
        lic_file = "\"" + self.LM_LICENSE_FILE_PREFIX + "\\" + lic_file + "\""
        pipe = Popen(self._command("lmstatAll")(lic_file), shell=True, stdout=PIPE, stderr=PIPE)
        return self._check(pipe, lic_file)

    def _check(self, pipe, lic_file):
        print("[Command._check] License File: " + lic_file)
        for i in range(8):
            line = Util.readline(pipe)
        if line == -1:
            print("[Command._check] " + lic_file + " Server Error: EOF")
            return -1
        elif "license server UP" in line:
            print("[Command._check] " + lic_file + " Server is RUNNING")
            return 0
        elif "lmgrd is not running" in line:
            print("[Command._check] " + lic_file + " Server Error:" + line)
            return -1
        else:
            print("[Command._check] " + lic_file + " Unexpected Error:" + line)
            return -1

    def start(self, lmgrd_lic):
        cmd = self._command("start")(lmgrd_lic)
        print("[Command] Execute: " + cmd)
        pipe = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)

    def shutdown(self, lmgrd_lic):
        cmd = self._command("shutdown")(lmgrd_lic)
        print("[Command] Execute: " + cmd)
        pipe = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)


    def lmstatByModule(self, lic_file, module, software):
        lic_file = "\"{}\\{}\"".format(self.LM_LICENSE_FILE_PREFIX, lic_file)
        cmd = self._command("lmstatAll")(lic_file)
        print("[Command] Execute: " + cmd)
        pipe = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        status = self._check(pipe, lic_file)
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
                    user_data = get_user_data(raw_user_data, software)
                        
                    result[module]["user_data"] = user_data
                else:
                    result[module]["user_data"] = []
                    result[module]["metadata"] = []
        return status, result

    def lmstatAll(self, lic_file, software):
        lic_file = "\"" + self.LM_LICENSE_FILE_PREFIX + "\\" + lic_file + "\""
        cmd = self._command("lmstatAll")(lic_file)
        print("[Command] Execute: " + cmd)
        pipe = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        status = self._check(pipe, lic_file)
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

                    user_data = get_user_data(raw_user_data, software)
                    result[module]["user_data"] = user_data
                else:
                    result[module]["user_data"] = []
                    result[module]["metadata"] = []
        return status, result

    def lmremoveByDevice(self, feature, user,user_host, display):
        pipe = Popen(self._command("lmremoveByDevice")(feature, user, user_host, display), shell=True, stdout=PIPE, stderr=PIPE)
    
    def lmremoveByPort(self, feature, server_host, port, handle):
        pipe = Popen(self._command("lmremoveByPort")(feature, server_host, port, handle), shell=True, stdout=PIPE, stderr=PIPE)

    def lmborrow(self):
        pipe = Popen(self._command("lmstatAll"), shell=True, stdout=PIPE, stderr=PIPE)

if __name__ == "__main__":
    cmd = Command()
    cmd.lmstatAll("lic-sjtu-localhost.dat")

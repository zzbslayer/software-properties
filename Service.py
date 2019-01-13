from subprocess import Popen, PIPE
import os
from Command import Command


cmd = Command()
BLANK = '\r\n'

def _readline(pipe):
    line = pipe.stdout.readline()
    if not line:
        return -1
    encoded_line = str(line, encoding="gbk")
    return encoded_line

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
def cmd_status():
    pipe = Popen(cmd.status(), shell=True, stdout=PIPE, stderr=PIPE)
    result = {}
    while True:
        line = _readline(pipe)
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
                line = _readline(pipe)
                if line == BLANK:
                    continue
                metadata.append(line[2:])
            result[module]["metadata"] = metadata

            line = _readline(pipe)
            if line == -1:
                break

            # read user data of some module
            user_data = []
            while(line[:9] != "Users of "):
                line = _readline(pipe)
                if line == -1:
                    break
                if line == BLANK:
                    continue
                user_data.append(line[4:])
            result[module]["user_data"] = user_data
    return result

def main():
    print(cmd_status())

main()
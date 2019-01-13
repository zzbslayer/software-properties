import os

class Command(object):
    def __init__(self, path=None):
        if (path==None):
            self.path = "C:\Program Files\MATLAB\R2018a\etc\win64"
        else:
            self.path = path

        LM_LICENSE_FILE = os.environ.get('LM_LICENSE_FILE')
        if not LM_LICENSE_FILE:
            self.set_env_var = False
            LM_LICENSE_FILE = "C:\Program Files\MATLAB\R2018a\etc\license.dat"
        else:
            self.set_env_var = True
        
        self.command_with_license_file = {"status": "\""+ self.path + "\lmutil.exe\" lmstat MATLAB", \
                                        "others": "dir"
                                        }
        
    def status(self):
        return self.command_with_license_file["status"]
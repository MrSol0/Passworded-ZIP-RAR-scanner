import zipfile
import rarfile
from os import walk

class client(object):
    def __init__(self,path):
        self.encrypted = {}
        self.find_all(path)
    def find_all(self, path):
        _, _, filenames = next(walk(path))
        for file in filenames:
            if file.endswith(".zip"):
                self.checkZIPEncryption(path+"\\"+file,file)
            elif file.endswith(".rar"):
                self.checkRAREncryption(path+"\\"+file,file)

        for file in self.encrypted:
            print('%s is encrypted!' % file)

    def checkZIPEncryption(self,path,file):
        if self.encrypted.get(file):
            return
        try:
            zf = zipfile.ZipFile(path)
        except:
            return

        for zinfo in zf.infolist():
            is_encrypted = zinfo.flag_bits & 0x1
            if is_encrypted:
                #print ('%s is encrypted!' % path)
                self.encrypted[file] = True
    def checkRAREncryption(self,path,file):
        if self.encrypted.get(file):
            return
        try:
            rar = rarfile.RarFile(path)
        except:
            return
        if rar.needs_password():
            self.encrypted[file] = True




if __name__ == "__main__":
    print("[SYNTAX]: C:\Downloads")
    path = input("[FOLDER PATH]: ")
    client(path)

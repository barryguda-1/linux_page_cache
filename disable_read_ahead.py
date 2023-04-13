import os

with open("/var/tmp/file1.db", "br") as f:  
    fd = f.fileno()  
    os.posix_fadvise(fd, 0, os.fstat(fd).st_size, os.POSIX_FADV_RANDOM)  
    #read 2 bytes of data
    print(f.read(2))

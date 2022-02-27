from django.test import TestCase
from apscheduler.schedulers.background import BackgroundScheduler
# from models import RecentDownload
import paramiko
from datetime import datetime
from stat import S_ISDIR,S_ISREG
# Create your tests here.
def download():
    print('hello scheduler download')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname = 'sftp2.ibpark.net',username = 'davidtech',password = 'C*TuxoD2K')
    ftp_client=client.open_sftp()
    
    remothpath = ftp_client.normalize('.')
    print('path',remothpath)
    print(ftp_client.listdir(path = remothpath))
    ftp_client.chdir('Out')
    print(ftp_client.getcwd())
    print(ftp_client.listdir('.'))

    


    # directory_queue,files = [],[]
    # # root_path = "."
    # directory_queue.append(remothpath)
    # print('its directory queue',directory_queue)
    # for entry in ftp_client.listdir_attr(remothpath):
    #     mode = entry.st_mode
    #     if S_ISDIR(mode):
    #         print(entry.filename + " is folder")
    #         ftp_client.chdir(entry.filename)
    #         print(ftp_client.getcwd())
    #     elif S_ISREG(mode):
    #         print(entry.filename + " is file")
    # timestampnow = RecentDownload.objects.latest('LastDownload')
    # timestampnow = timestampnow.LastDownload

    # while directory_queue:
    #     print('its directory inside queue',directory_queue)
    #     path = directory_queue.pop()
    #     for entry in ftp_client.listdir_attr(path):
    #         mode = entry.st_mode
    #         if S_ISDIR(mode):
    #             current_directory = str(entry.filename)
    #             directory_queue.append(current_directory)
    #         elif (S_ISREG(mode)):
    #             print('its file',entry.filename,entry.st_mtime)
    #             files.append(entry.filename)
    #     print(files)
    # if files:
    #     local_file_path = r"C:\Users\dell\Documents".format(str(files[0]))
    #     ftp_client.get(files[0],local_file_path)
    # now = datetime.now()
    # timestamp = datetime.timestamp(now)
    # timestamp_obj = RecentDownload(LastDownload=timestamp)
    # timestamp_obj.save()
    ftp_client.close()

download()
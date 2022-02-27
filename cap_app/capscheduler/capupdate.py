#from paramiko.client import AutoAddPolicy
from apscheduler.schedulers.background import BackgroundScheduler
from cap_app.models import RecentDownload
import paramiko
from datetime import datetime
from stat import S_ISDIR,S_ISREG



def download():
    print('hello scheduler download')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname = 'giglabzcom3.files.com',username = 'karthika_s',password = 'G@yathri91')
    ftp_client=client.open_sftp()

    directory_queue,files = [],[]
    root_path = "."
    directory_queue.append(root_path)
    print('its directory queue',directory_queue)
    timestampnow = RecentDownload.objects.latest('LastDownload')
    timestampnow = timestampnow.LastDownload

    while directory_queue:
        print('its directory inside queue',directory_queue)
        path = directory_queue.pop()
        for entry in ftp_client.listdir_attr(path):
            mode = entry.st_mode
            if S_ISDIR(mode):
                current_directory = str(entry.filename)
                directory_queue.append(current_directory)
            elif (S_ISREG(mode) and entry.st_mtime > timestampnow):
                print('its file',entry.filename,entry.st_mtime,timestampnow)
                files.append(entry.filename)
        print(files)
    if files:
        local_file_path = r"C:\Users\dell\Documents".format(str(files[0]))
        ftp_client.get(files[0],local_file_path)
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    timestamp_obj = RecentDownload(LastDownload=timestamp)
    timestamp_obj.save()
    ftp_client.close()

def start():
    schedule = BackgroundScheduler()
    schedule.add_job(download,"interval",seconds = 120)
    schedule.start()

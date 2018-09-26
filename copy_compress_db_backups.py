# This script will perform three steps.
# 1. Compress PACSIW DB Backup
# 2. Copy PACSIW DB Backup to replication folder
# 3. Remove PACSIW DB Backups that are older then 3 months in source folder
# 4. Remove PACSIW

import zipfile
import os
import glob
import shutil
import time
import datetime

currentDate = datetime.datetime.now()

# Variables
dbBackup = 'dbBackup' + str(currentDate.month) + \
    str(currentDate.day) + str(currentDate.year) + '.zip'

# Set up source and destination directories
sourceDir = 'C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\source\\'
zipFile = 'C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\source\\' + dbBackup
destinationDir = 'C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\destination\\'

# Identify lattest db backup file for compression
os.chdir(
    'C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\source')
files = glob.iglob(
    'C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\source\\*')
latest_file = max(files, key=os.path.getctime)
dbBackupFile = os.path.split(latest_file)
dbFile = dbBackupFile[1]

# Create zip file
with zipfile.ZipFile(dbBackup, 'w', allowZip64=True) as dbZip:
    dbZip.write(dbFile)

# Copy compressed file to replication folder
shutil.copy2(zipFile, destinationDir)

# Delete db backups older then 30 days
files = glob.iglob(
    'C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\source\\*')
now = time.time()
for f in files:
    if(os.stat(f).st_mtime < now - 30 * 86400):
        os.remove(f)

# Delete db backups older then 30 days in destination folder
destinationFiles = glob.iglob(
    'C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\destination\\*')
for f in destinationFiles:
    if(os.stat(f).st_mtime < now - 30 * 86400):
        os.remove(f)

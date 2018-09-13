# This script will perform three steps.
# 1. Compress PACSIW DB Backup
# 2. Copy PACSIW DB Backup to replication folder
# 3. Remove PACS DB Backups that are older then 3 months to preserve space on local system

import zipfile
import os
import glob
import shutil

# Variables
dbBackup = 'dbBackup.zip'

# Set up source and destination directories
os.chdir(
    'C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\source')
sourceDir = 'C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\source\\' + dbBackup
destinationDir = 'C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\destination\\'

# Identify lattest db backup file for compression
files = glob.iglob(
    'C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\source\\*')
latest_file = max(files, key=os.path.getctime)
dbBackupFile = os.path.split(latest_file)
dbFile = dbBackupFile[1]

# Create zip file
with zipfile.ZipFile(dbBackup, 'w', allowZip64=True) as dbZip:
    dbZip.write(dbFile)

# Copy compressed file to replication folder
shutil.copy2(sourceDir, destinationDir)


# Delete db backups older then 3 months

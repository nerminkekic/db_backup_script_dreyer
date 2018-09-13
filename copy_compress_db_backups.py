# This script will perform three steps.
# 1. Compress PACSIW DB Backup
# 2. Copy PACSIW DB Backup to replication folder
# 3. Remove PACS DB Backups that are older then 3 months to preserve space on local system

import zipfile
import os
import glob
os.chdir('C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\source')

# Identify lattest db backup file for compression
files = glob.iglob(
    'C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\source\\*')
latest_file = max(files, key=os.path.getctime)
print(latest_file)
dbBackupFile = os.path.split(latest_file)
print(dbBackupFile[1])

# Create zip file
with zipfile.ZipFile('dbBackup.zip', 'w', allowZip64=True) as dbZip:
    dbZip.write(dbBackupFile[1])

# Copy compressed file to replication folder

# Delete db backups older then 3 months

# This script will perform three steps.
# 1. Compress PACSIW DB Backup
# 2. Copy PACSIW DB Backup to replication folder
# 3. Remove PACS DB Backups that are older then 3 months to preserve space on local system

import zipfile
import os
os.chdir('C:\\Users\\Nermin\\Desktop\\Projects\\PACSIW Script\\source')

# Create zip file
with zipfile.ZipFile('dbBackup.zip', 'w', allowZip64=True) as dbZip:
    dbZip.write('file.exe')

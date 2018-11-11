#!/usr/bin/python3
# Description: create a backup of a directory
# Author: Paul hivert
# Date: 11/11/2018

import datetime
import os
import sys
import shutil
from shutil import make_archive
import filecmp
import signal

def CreateBackup():
  shutil.make_archive(_Create_ArchiveName, 'gztar', workingDirectory)

def GetTime():
    sys.stdout.write(str(datetime.datetime.now()))

def CheckIfArchiveExists():
    if (os.path.exists('~/backup/archive.tar.gz')):
        return True
    else:
        return False

def MoveArchive():
  shutil.move(_Move_ArchiveName, ArchiveDirectory)

def CheckSamplefile():
    filecmp.cmp(_Move_ArchiveName, _Check_ArchiveSource)

def deleteOld():
     os.remove(_Check_ArchiveSource)

#interupts

def stop(sig, frame):
  sys.stdout.write('system interupted')
  exit()

signal.signal(signal.SIGINT, stop)

#variables
_Create_ArchiveName = os.path.expanduser(os.path.join('~', 'archive'))
_Move_ArchiveName = os.path.expanduser(os.path.join('~', 'archive.tar.gz'))
_Check_ArchiveSource =  os.path.expanduser(os.path.join('~', 'backup/archive.tar.gz'))
workingDirectory = os.path.expanduser(os.path.join('~', 'test'))
ArchiveDirectory = os.path.expanduser(os.path.join('~', 'backup'))

#main
GetTime()
CreateBackup()
if CheckIfArchiveExists() == True:
    if CheckSamplefile() == True:
        sys.stdout.write('no archiving needed')
        sys.exit()
    else:
        deleteOld()
        MoveArchive()
else:
    MoveArchive()

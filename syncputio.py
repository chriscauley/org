#!/usr/bin/env python

import os
import putio

OAUTH_TOKEN = 'XXXXXX'
SECRET = 'XXXXXX'
APPID = 'XXXXX'
FOLDER_ID = 123456

def do_sync ():
  os.chdir('/plex')
  
  local_files = os.listdir('.')
  
  client = putio.Client(OAUTH_TOKEN)
  files = client.File.list(parent_id=FOLDER_ID)
  
  for file in files:
    if file.name not in local_files:
      print("Downloading: {}".format(file.name))
      file.download(delete_after_download=True)
      
    else:
      print("Skipping: {}".format(file.name))
      
if __name__ == "__main__":
  do_sync()
  
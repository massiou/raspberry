#decode: utf-8

"""
    Module to sync files on localhost to a dropbox account
"""

import os
import uuid
import dropbox

from config import ACCESS_TOKEN
from config import TARGET_DIR

def main(target_dir, access_token):
    """
        Main entry
    """
    dbx = dropbox.client.DropboxClient(access_token)

    # list target images files
    target_videos = [os.path.join(target_dir, file_p)
                     for file_p in os.listdir(target_dir) if file_p.endswith('avi')]
    target_images = [os.path.join(target_dir, file_p)
                     for file_p in os.listdir(target_dir) if file_p.endswith('jpg')]

    # Loop on all files
    for c_file in target_videos:
        # Build dropbox file name
        c_dbx_name = ''.join([str(uuid.uuid4()), '.avi'])
        print c_dbx_name
        with open(c_file, 'rb') as c_file_content:
            # Put current file on dropbox
            dbx.put_file(c_dbx_name, c_file_content)

            # Remove file from current directory
            os.remove(c_file)
            # TODO Send mail to inform

        if target_videos:
            for c_img in target_images:
                os.remove(c_img)

if __name__ == '__main__':
    main(TARGET_DIR, ACCESS_TOKEN)

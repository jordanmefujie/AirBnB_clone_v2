#!/usr/bin/python3
""" This module contains the function do_pack that generates a .tgz archive
  from the contents of the web_static folder (fabric script) """

from fabric.api import *
from datetime import datetime

env.hosts = ['localhost']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Create the name of the archive
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)

        # Compress the contents of the web_static folder
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the path of the archive
        return "versions/{}".format(archive_name)

    except Exception as e:
        # Print an error message and return None if an exception occurs
        print("Error: {}".format(e))
        return None


# Example usage:
result = do_pack()
if result:
    print("Archive created: {}".format(result))
else:
    print("Archive creation failed.")

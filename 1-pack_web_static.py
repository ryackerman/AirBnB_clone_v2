#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """init"""
    datet = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(datet.year,
                                                         datet.month,
                                                         datet.day,
                                                         datet.hour,
                                                         datet.minute,
                                                         datet.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file

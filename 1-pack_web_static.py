#!/usr/bin/python3
"""
a fab file to perform some configuration
"""
from fabric.api import local
from datetime import datetime
from os.path import exists


def do_pack():
    """
    generates a .tgz from the content of the
    web_static folder
    """
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    hour = datetime.now().hour
    minutes = datetime.now().minute
    seconds = datetime.now().second
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            year, month, day, hour, minutes, seconds
            )
    if exists("versions") is False:
        local("mkdir versions")
    result = local("tar -cvzf versions/{} web_static".format(archive_name))
    if result.failed:
        return None
    else:
        return "versions/{}".format(archive_name)

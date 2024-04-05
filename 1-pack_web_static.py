#!/usr/bin/python3
"""
a fab file to perform some configuration
"""
from fab import local
from datetime import datetime


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
    archive_name = "{}{}{}{}{}.tgz".format(year, month, day, hour, minutes)
    result = local("tar -cvzf versions/{} ./web_static".format(archive_name))
    if result.failed:
        return None
    else:
        return archive_name

#!/usr/bin/python3

"""
generates .tgz archive from the contents of the web_static
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive from the content of the
    web_static file and save it into version folder
    with the name of the archive been in the format
    web_static_<year><month><day><hour><minute><second>.tgz
    """

    now = datetime.now()
    filename = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    file = "./web_static"
    local("mkdir -p ./versions")
    local("tar -cvzf versions/{} {}".format(filename, file))
    return ("versions/{}".format(filename))

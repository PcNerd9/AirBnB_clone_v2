#!/usr/bin/python3
"""
a fabric file that distributes an archive to my web server
"""

from fabric.api import run, local, put, env
from os.path import exists
env.hosts = ['54.236.25.152', '100.26.17.86']


def do_deploy(archive_path):
    """
    distributes an archive to web servers and uncompress it
    """
    if exists(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1].split(".")[0]
        location = "/data/web_static/releases/{}".format(filename)
        put(archive_path, remote="/tmp/")
        run("tar -xzvf archive_path -C {}".format(location))
        run("rm -drf /tmp/{}.tgz".format(filename))
        if (exists("/data/web_static/current")):
            run("rm -drf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(location))
        return True
    except Exception as e:
        return False

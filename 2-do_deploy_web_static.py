#!/usr/bin/python3
"""
a fabric file that distributes an archive to my web server
"""

from fabric.api import run, local, put, env
from os.path import exists
env.hosts = ['100.26.254.81', '100.26.158.71']
env.user= "ubuntu"


def do_deploy(archive_path):
    """
    distributes an archive to web servers and uncompress it
    """
    if exists(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1].split(".")[0]
        location = "/data/web_static/releases/{}/".format(filename)
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(location))
        run("tar -xzvf /tmp/{}.tgz -C {}".format(filename, location))
        run("rm -drf /tmp/{}.tgz".format(filename))
        run("mv {}/web_static/* {}".format(location, location))
        run("rm -drf {}/web_static".format(location))
        run("rm -drf /data/web_static/current")
        run("ln -sf {} /data/web_static/current".format(location))
        return True
    except Exception as e:
        return False

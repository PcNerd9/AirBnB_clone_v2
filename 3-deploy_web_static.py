#!/usr/bin/python3
"""
contains fab function that creates and distributes an archive
to my web servers
"""

from fabric.api import run, local, env, put
from datetime import datetime
from os.path import exists

env.hosts = ['54.236.25.152', '100.26.17.86']


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
    try:
        if exists("version") is False:
            local("mkdir versions")
        result = local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception:
        return (False)


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
        run("ln -s {} /data/web_static/current".format(location))
        return True
    except Exception as e:
        return False


def deploy():
    """
    distrbutes an archive to my web server
    uncompress it and move to the web folder
    """
    archive_file = do_pack()
    if (not archive_file):
        return False
    result = do_deploy(archive_file)
    return (result)

#!/usr/bin/python3

"""
generates .tgz archive from the contents of the web_static
"""

from fabric.api import local, run, put, env
from datatime import datetime
from os.path import exists


def do_pack():
    """
    generates a .tgz archive from the content of the
    web_static file and save it into version folder
    with the name of the archive been in the format
    web_static_<year><month><day><hour><minute><second>.tgz
    """

    now = datetime.now()
    filename = "web_static_{}.tgz".format(now.strtime("%Y%m%d%H%M%S"))
    file = "./web_static"
    local("mkdir -p ./versions")
    local("tar -cvzf versions/{} {}".format(filename, file))
    return (filename)


def do_deploy(archive_path):
    """
    distributes an archive file to my web servers
    """

    env.hosts = ["100.26.254.81", "100.26.158.71"]
    env.user = "ubuntu"

    if not exists(archive_path):
        return False

    remote_path = "/tmp/"
    archive_name = archive_path.split("/")[-1].split(".")[0]
    deploy_path = "/data/web_static/releases/{}".format(
            archive_name)

    try:
        put(local=archive_path, remote=remote_path)
        run("mkdir -p {}".format(deploy_path))
        run("tar -xzvf /tmp/{}.tgz -C {}".format(
            archive_name, deploy_path))

        run("rm /tmp/{}.tgz".format(archive_name))
        run("rm /data/web_static/current")
        run("ln -sf {} /data/web_static/current".format(deploy_path))
        return True
    except Exception as e:
        return False

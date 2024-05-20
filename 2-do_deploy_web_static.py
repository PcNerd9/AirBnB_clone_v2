#!/usr/bin/python3

"""
generates .tgz archive from the contents of the web_static
"""

from fabric.api import local, run, put, env
from datetime import datetime
from os.path import exists

env.hosts = ["100.26.254.81", "100.26.158.71"]
env.user = "ubuntu"


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

    if exists(archive_path) is False:
        return False

    try:
        remote_path = "/tmp/"
        archive_name = archive_path.split("/")[-1].split(".")[0]
        deploy_path = "/data/web_static/releases/{}".format(
                archive_name)

        put(archive_path, remote_path)
        run("mkdir -p {}".format(deploy_path))
        run("tar -xzf /tmp/{}.tgz -C {}".format(
            archive_name, deploy_path))

        run("rm /tmp/{}.tgz".format(archive_name))
        run("rm -rdf  /data/web_static/current")
        run("ln -sf {} /data/web_static/current".format(deploy_path))
        return True
    except Exception as e:
        return False

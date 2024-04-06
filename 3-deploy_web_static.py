#!/usr/bin/python3
"""
contains fab function that creates and distributes an archive
to my web servers
"""
from importlib import import_module
from fabric.api import run, local, env, put
archive_module = import_module("1-pack_web_static")
distribute_module = import_module("2-do_deploy_web_static")


def deploy():
    """
    creates an distributes an archive to my web servers
    """
    archive_file = archive_module.do_pack()
    if (not archive_file):
        return False
    result = distribute_module.do_deploy(archive_file)
    return (result)

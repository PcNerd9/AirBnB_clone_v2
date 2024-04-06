#!/usr/bin/python3
"""
contains fab function that creates and distributes an archive
to my web servers
"""

from fabric.api import run, local, env, put



def deploy():
    archive_file = archive_module.do_pack()
    if (not archive_file):
        return False
    result = distribute_module.do_deploy(archive_file)
    return (result)

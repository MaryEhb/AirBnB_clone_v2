#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of
# the web_static

from fabric.api import *
import datetime


def do_pack():
    """Compress before sending"""
    local("mkdir -p versions")
    created_at = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(created_at)
    command = local("sudo tar -cvzf {} web_static".format(path))
    if command.succeeded:
        return path
    else:
        return None

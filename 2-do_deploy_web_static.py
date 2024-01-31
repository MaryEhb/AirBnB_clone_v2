#!/usr/bin/python3
# 2. Deploy archive!

from fabric.api import *

env.hosts = ["34.224.62.130", "3.94.213.33"]


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1]
        path = "/data/web_static/releases/{}/".format(filename.split(".")[0])

        run("sudo mkdir -p {}".format(path))
        run("sudo tar -xvzf /tmp/{} -C {}".format(filename, path))
        run("sudo rm /tmp/{}".format(filename))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} /data/web_static/current".format(path))
        return True
    except Exception:
        return False

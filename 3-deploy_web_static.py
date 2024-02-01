#!/usr/bin/python3
"""3. Full deployment of two servers"""


from fabric.api import *
import os
import datetime
env.hosts = ["34.224.62.130", "3.94.213.33"]
path = None


def do_pack():
    """Compress before sending"""
    local("sudo mkdir -p versions")
    created_at = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(created_at)
    command = local("sudo tar -cvzf {} web_static".format(path))
    if command.succeeded:
        return path
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    if os.path.exists(archive_path) is False:
        return False

    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1]
        path = "/data/web_static/releases/{}".format(filename.split(".")[0])
        run("sudo mkdir -p {}/".format(path))
        run("sudo tar -xzf /tmp/{} -C {}/".format(filename, path))
        run("sudo rm /tmp/{}".format(filename))
        run("sudo mv {}/web_static/* {}/".format(path, path))
        run("sudo rm -rf {}/web_static".format(path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}/ /data/web_static/current".format(path))
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to your web servers
    using the function"""
    global path
    if path is None:
        path = do_pack()
    if path is None:
        return False
    return do_deploy(path)

#!/usr/bin/python3
# 3. Full deployment


from fabric.api import *
import datetime
import os

env.hosts = ["34.224.62.130", "3.94.213.33"]


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


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    if os.path.exists(archive_path) is False:
        return False

    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1]
        path = "/data/web_static/releases/{}".format(filename.split(".")[0])
        run("mkdir -p {}/".format(path))
        run("tar -xvzf /tmp/{} -C {}/".format(filename, path))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}/".format(path, path))
        run("rm -rf {}/web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(path))
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to your web servers
    using the function"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

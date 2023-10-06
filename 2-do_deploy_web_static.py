#!/usr/bin/python3
""" This Fabric script distributes an archive to web servers"""
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['100.26.178.116', '54.144.154.1']


def do_deploy(archive_path):
    """
    This function distributes an archive to web servers
    """
    if not path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        file_base = file_name.split('.')[0]
        path_static = "/data/web_static/releases/{}/".format(file_base)

        put(archive_path, '/tmp/')

        run("mkdir -p {}".format(path_static))

        run("tar -xzf /tmp/{} -C {}".format(file_name, path_static))

        run("rm /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(path_static, path_static))
        run("rm -rf {}web_static".format(path_static))
        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(path_static))
        print("New vision deployed")

        return True
    except Exception:
        return False

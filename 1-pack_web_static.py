#!/usr/bin/python3
"""
This Fabric script generates a .tgz archive from the contents
of the web_static.
"""
from fabric.api import local
from datetime import datetime

def do_pack():
	""" This function generates a .tgz archive """
	date_time = datetime.now().strftime("%Y%m%d%H%M%S")

	local("mkdir -p versions")
	archive = "versions/web_static_{}.tgz".format(date_time)

	if local("tar -czvf {} web_static".format(archive)).succeeded:
		return archive
	else:
		return None

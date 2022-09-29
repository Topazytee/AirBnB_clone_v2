#!/usr/bin/python3
""" Based on 3-deploy_web_static.py, delete out-of-date archives
using the do_clean function """

from fabric.operations import local, run, put
from datetime import datetime
import os
from fabric.api import env
import re


env.hosts = ['35.172.217.245', '18.205.96.171']


def do_pack():
    """ Function for file compression """
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if result.failed:
        return None
    return result


def do_deploy(archive_path):
    """ Function to distribute archive to servers """
    if not os.path.exists(archive_path):
        return False
    rex = r'^versions/(\S+).tgz'
    match = re.search(rex, archive_path)
    filename = match.group(1)
    res = put(archive_path, "/tmp/{}.tgz".format(filename))
    if res.failed:
        return False
    res = run("mkdir -p /data/web_static/releases/{}/".format(filename))
    if res.failed:
        return False
    res = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False
    res = run("rm /tmp/{}.tgz".format(filename))
    if res.failed:
        return False
    res = run("mv /data/web_static/releases/{}"
              "/web_static/* /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False
    res = run("rm -rf /data/web_static/releases/{}/web_static"
              .format(filename))
    if res.failed:
        return False
    res = run("rm -rf /data/web_static/current")
    if res.failed:
        return False
    res = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
              .format(filename))
    if res.failed:
        return False
    print('New version deployed!')
    return True


def deploy():
    """ Create and distribute an archive to web servers """
    filepath = do_pack()
    if filepath is None:
        return False
    d = do_deploy(filepath)
    return d


def do_clean(number=0):
    """ Delete out-of-dates archives """
    files = local("ls -1t versions", capture=True)
    file_names = file.split("\n")
    n = int(number)
    if n in (0, 1):
        n = 1
    for i in file_names[n:]:
        local("rm versions/{}".format(i))
        dir_server = run("ls -1t /data/web_static/releases")
        dir_server_names = dir_server.split("\n")
        for i in dir_server_names[n:]:
            if i is 'test':
                continue
            run("rm -rf /data/web_static/releases/{}"
                .format(i))

#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py) that distributes..
    ..an archive to your web servers, using the function do_deploy: """


from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['100.25.167.92', '18.234.168.83']
env.user = 'ubuntu'
env.key_filename = 'usr/bin/ssh'


def do_pack():
    """Create a compressed archive of web_static folder"""
    with Connection(env.hosts[0], user=env.user, connect_kwargs={"key_filename": env.key_filename}):
    local("mkdir -p versions")
    time_format = "%Y%m%d%H%M%S"
    archive_name = "web_static_{}.tgz".format(datetime.utcnow().strftime(time_format))
    cmd = "tar -cvzf versions/{} web_static".format(archive_name)
    result = local(cmd)
    if result.failed:
        return None
    return "versions/{}".format(archive_name)


def do_deploy(archive_path):
    """Distribute an archive to web servers"""
    if not exists(archive_path):
        return False

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, '/tmp/')

    # Extract the archive to the folder /data/web_static/releases/<archive filename without extension>
    archive_filename = archive_path.split('/')[-1]
    release_folder = '/data/web_static/releases/{}'.format(archive_filename.split('.')[0])
    run('mkdir -p {}'.format(release_folder))
    run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

    # Delete the archive from the web server
    run('rm /tmp/{}'.format(archive_filename))

    # Delete the symbolic link /data/web_static/current from the web server
    run('rm -rf /data/web_static/current')

    # Create a new symbolic link /data/web_static/current on the web server
    run('ln -s {} /data/web_static/current'.format(release_folder))

    return True

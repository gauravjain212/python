from fabric.api import *

env.user = "root"
env.hosts = '192.168.255.155'
env.password = 'redhat'

def space():
    run('df -h')

def update_all():
    run('yum update -y')
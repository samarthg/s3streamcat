from fabric.api import local

def hello():
    print("hi there")

def prepare_patch():
    local("bumpversion patch")

def prepare_minor():
    local("bumpversion minor")

def prepare_major():
    local("bumpversion major")

def release():
    local("git push origin master")
    local("git push --tags origin master")
    local("python setup.py sdist upload -r pypi")
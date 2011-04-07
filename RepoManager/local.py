try:
    import xml.etree.cElementTree as ElementTree
except ImportError:
    try:
        import xml.etree.ElementTree
    except ImportError:
        import elmenttree.ElementTree
import os

from project import Project
from remote import Remote

class LocalHost:
    def __init__(self, remote_name, remote_host, path):
        Remote(remote_name, "ssh://%s%s/" % (remote_host, path))
        for dirpath, dirnames, filenames in os.walk(path):
            (filepath, filename) = os.path.split(dirpath)
            (shortname, extension) = os.path.splitext(filename)
            if extension == ".git":
                rel_path = dirpath[len(path) + 1:-4]
                Project(rel_path, rel_path, remote_name, "master")

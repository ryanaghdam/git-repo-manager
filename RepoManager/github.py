try:
    import xml.etree.cElementTree as ElementTree
except ImportError:
    try:
        import xml.etree.ElementTree
    except ImportError:
        import elmenttree.ElementTree
from xml.dom.minidom import parseString
from urllib import urlopen

from remote import Remote
from project import Project

class GitHubHost:
    def __init__(self, username):
        Remote("github", "git@github.com:/")
        api_call = "http://github.com/api/v2/xml/repos/show/%s" % (username)
        repository_tree = ElementTree.parse(urlopen(api_call))
        for repository in repository_tree.findall("repository"):
            path = "%s/%s" % (repository.findtext("owner"), 
                              repository.findtext("name"))
            Project(path, path, "github", "master")


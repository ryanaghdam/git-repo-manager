try:
    import xml.etree.cElementTree as ElementTree
except ImportError:
    try:
        import xml.etree.ElementTree
    except ImportError:
        import elmenttree.ElementTree

from xml.dom.minidom import parseString

class Manifest:
    __shared_state = {'remotes': [], 'default': None, 'projects': []}
    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        manifest = ElementTree.Element("manifest")
        for remote in self.remotes:
            remote.asxml(manifest)
        self.default.asxml(manifest)
        for project in self.projects:
            project.asxml(manifest)
        return parseString(ElementTree.tostring(manifest)).toprettyxml()


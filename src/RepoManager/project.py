try:
    import xml.etree.cElementTree as ElementTree
except ImportError:
    try:
        import xml.etree.ElementTree
    except ImportError:
        import elmenttree.ElementTree
from xml.dom.minidom import parseString
from manifest import Manifest

class Project:
  def __init__(self, name, path, remote, revision):
    self.name = name
    self.path = path
    self.remote = remote
    self.revision = revision
    Manifest().projects.append(self)

  def asxml(self, root):
    project = ElementTree.SubElement(root, "project")
    project.set("name", self.name)
    project.set("path", self.path)
    project.set("remote", self.remote)
    project.set("revision", self.revision)



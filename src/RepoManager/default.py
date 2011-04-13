try:
    import xml.etree.cElementTree as ElementTree
except ImportError:
    try:
        import xml.etree.ElementTree
    except ImportError:
        import elmenttree.ElementTree

from xml.dom.minidom import parseString

from manifest import Manifest

class Default:
  def __init__(self, remote, revision):
    self.remote = remote
    self.revision = revision
    Manifest().default = self

  def asxml(self, root):
    default = ElementTree.SubElement(root, "default")
    default.set("remote", self.remote)
    default.set("revision", self.revision)

try:
    import xml.etree.cElementTree as ElementTree
except ImportError:
    try:
        import xml.etree.ElementTree
    except ImportError:
        import elmenttree.ElementTree
from xml.dom.minidom import parseString
from manifest import Manifest

class Remote:
  def __init__(self, name, fetch):
    self.name = name
    self.fetch = fetch
    Manifest().remotes.append(self)

  def asxml(self, root):
    remote = ElementTree.SubElement(root, "remote")
    remote.set("name", self.name)
    remote.set("fetch", self.fetch)

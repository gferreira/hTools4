# menuTitle : scale

from importlib import reload
import xTools4.dialogs.glyphs.scale
reload(xTools4.dialogs.glyphs.scale)

from mojo.roboFont import OpenWindow
from xTools4.dialogs.glyphs.scale import ScaleGlyphsDialog

OpenWindow(ScaleGlyphsDialog)

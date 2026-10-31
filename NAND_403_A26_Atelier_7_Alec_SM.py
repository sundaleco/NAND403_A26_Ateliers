
from maya import cmds

objet = cmds.ls(selection=True)[0]

# Effacer anciennes keyframes
cmds.cutKey(objet, clear=True)

cmds.playbackOptions(min=1, max=100)

# Ajouter 3 keyframes
cmds.setKeyframe(objet, attribute="translateX", value=0, time=1)
cmds.setKeyframe(objet, attribute="translateX", value=100, time=95)
cmds.setKeyframe(objet, attribute="translateX", value=0, time=100)

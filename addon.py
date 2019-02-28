import xbmcaddon
import xbmcgui
import time
import sys

xbmc.executebuiltin('XBMC.RunAddon(plugin.video.youtube)')

xbmc.executebuiltin('ShowPicture("special://home/addons/script.andrios.youtube/fanart.jpg")')

time.sleep(3)

xbmc.Player().stop()



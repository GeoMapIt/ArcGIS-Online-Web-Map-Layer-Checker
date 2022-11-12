"""
Created by Nathan R
Prints all web maps that have a
specified feature as a layer

Can be run as is through ArcGIS Pro,
or as a script if given credentials.

Use IDLE (ArcGIS Pro) when running.
"""

import arcpy
import arcgis
from arcgis.gis import GIS
from arcgis.mapping import WebMap

#FILL OUT THESE
feature_layer = "3f4df3e3ebzc44cfb4c24115993f00b6" #ID for layer to search for
owner_username = "" #searches for maps owned by this user
login_username = "" #OPTIONAL
login_password = "" #OPTIONAL

#Script.
if (login_username != "" and login_password != ""):
    try:
        gis = GIS(username=login_username, password=login_password)
    except:
        print("Error, check login credentials.")
        sys.exit()
    
else:
    gis = GIS('home')

webmaps = gis.content.search("owner:"+owner_username, item_type="Web Map")

for webmap in webmaps:
    for layer in WebMap(webmap).layers:
        try:
            if ((layer.itemId).upper() == feature_layer.upper()):
                print("Layer found in: " + webmap.title)
        except:
            break
print("Completed")

import pandas as pd
import folium as fol
import os


map = fol.Map(location=(40.387778, 96.410278),
        control_scale=True, 
        zoom_control=False, 
        )
#downloadsDir = os.path.expanduser("~" + os.sep + "Downloads")
#html = os.path.join(downloadsDir, "map.html")
map.save("map.html")
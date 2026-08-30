# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------
#  ELEVATION PROFILE TOOLS
# --------------------------------------------------------------------------
#  PLUGIN NAME : Elevation Profile
#  DESCRIPTION : High-Precision Terrain Profiling Tool for QGIS
#  AUTHOR      : Gilbert Rival D
#  EMAIL       : Gilbert.revan17@gmail.com
#  VERSION     : 1.9.3
#  COPYRIGHT   : (c) 2023 by Gilbert Rival D
#  LICENSE     : GPL-2.0-or-later
#  MOTTO       : "Ingat kita pernah tidak bisa"
# --------------------------------------------------------------------------

"""
This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    """
    Load ElevationProfile class from file elevation_profile.
    
    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .elevation_profile import ElevationProfile
    return ElevationProfile(iface)

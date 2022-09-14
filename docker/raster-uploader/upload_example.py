from geo.Geoserver import Geoserver
import glob
import os

geo = Geoserver('https://anm.pti.org.br:80/geoserver/web', username='admin',
                password='geoserver')

pattern = os.getcwd()+'/rasters/*.tif'
raster_list = glob.glob(pattern)
workspace_name = 'acme'
for raster in raster_list:
    file_name = os.path.basename(raster)
    geo.create_coveragestore(
        path=raster,
        workspace=workspace_name,
        layer_name=file_name,
        file_type="GeoTIFF",
        content_type="image/tiff"
    )

#preprocess
import geopandas as gpd
import rasterio
from rasterio.mask import mask
from pathlib import Path
import numpy as np

def preprocess_rasters(dmsp_dir, selected_country, shapefile_path="World_Countries/World_Countries_Generalized.shp"):
    # Load the country shapefile
    countries = gpd.read_file(shapefile_path)
    country_shape = countries[countries['COUNTRY'] == selected_country]

    if country_shape.empty:
        raise ValueError(f"Country '{selected_country}' not found in the shapefile.")

    # List all DMSP raster files
    dmsp_raster_paths = list(Path(dmsp_dir).glob('*.tif'))

    for dmsp_raster_path in dmsp_raster_paths:
        with rasterio.open(dmsp_raster_path) as dmsp_src:
            # Print input resolution
            print(f"Input DMSP resolution: {dmsp_src.res}")

            # Crop the DMSP raster without changing resolution and print output resolution
            dmsp_out_image, _ = mask(dmsp_src, country_shape.geometry, crop=True)
            print(f"Output DMSP resolution (unchanged): {dmsp_src.res}")

            dmsp_cropped_path = Path(dmsp_dir) / f"cropped_{dmsp_raster_path.name}"
            with rasterio.open(dmsp_cropped_path, "w", **dmsp_src.meta) as dmsp_out:
                dmsp_out.write(dmsp_out_image)

            print(f"DMSP raster cropped and saved to {dmsp_cropped_path}")

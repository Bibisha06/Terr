import rasterio
import numpy as np
import json
from rasterio.transform import xy
from rasterio.enums import Resampling
from scipy.ndimage import sobel

def compute_slope_aspect(dem, transform):
    # Calculate gradient in x and y direction using Sobel operator
    dx = sobel(dem, axis=1, mode='constant') / 8.0
    dy = sobel(dem, axis=0, mode='constant') / 8.0

    # Calculate slope and aspect
    slope = np.arctan(np.hypot(dx, dy)) * (180 / np.pi)
    aspect = np.arctan2(-dx, dy)
    aspect = np.degrees(aspect)
    aspect = np.where(aspect < 0, 90.0 - aspect, 360.0 - aspect + 90.0)
    return slope, aspect

# Open DEM
with rasterio.open("file.tif") as src:
    dem = src.read(1, resampling=Resampling.bilinear)
    transform = src.transform
    nodata = src.nodata if src.nodata is not None else -9999

    # Mask nodata
    dem = np.where(dem == nodata, np.nan, dem)

    # Compute slope and aspect
    slope, aspect = compute_slope_aspect(dem, transform)

    # Downsample to reduce size (optional)
    step = 10  # change to control output density
    points = []

    for row in range(0, dem.shape[0], step):
        for col in range(0, dem.shape[1], step):
            elev = dem[row, col]
            if np.isnan(elev):
                continue
            slp = float(slope[row, col])
            asp = float(aspect[row, col])
            lon, lat = xy(transform, row, col)
            points.append({
                "lat": lat,
                "lon": lon,
                "elevation": float(elev),
                "slope": slp,
                "aspect": asp
            })

# Save to JSON
with open("dem_terrain_data.json", "w") as f:
    json.dump({"points": points}, f, indent=2)

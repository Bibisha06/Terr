# Terrain AI Project

This project processes terrain data and implements an A* pathfinding algorithm to find optimal paths across terrain.

## Project Structure

```
terrain-ai-project/
├── data/                     # Store input/output files (GeoTIFFs, JSONL)
│   ├── dem.TIF
│   ├── SR_B3.TIF
│   ├── SR_B4.TIF
│   ├── SR_B5.TIF
│   └── terrain_data.jsonl
├── scripts/                  # All processing/analysis code
│   ├── dem_processing.py     # DEM processing script
│   └── pathfinder.py         # A* pathfinding implementation
├── notebooks/                # For experimentation (optional)
├── outputs/                  # Generated plots, logs, saved paths
├── requirements.txt          # Project dependencies
└── README.md                 # This file
```

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix/MacOS:
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your .TIF files in the `data/` directory
2. Run `dem_processing.py` to generate `terrain_data.jsonl`
3. Run `pathfinder.py` to find and visualize paths between coordinates

## Dependencies

- numpy
- pandas
- matplotlib
- scipy
- networkx
- rasterio 
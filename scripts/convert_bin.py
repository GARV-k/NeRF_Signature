import sys, os

# Add scripts directory to path to find read_write_model
sys.path.append('scripts')
from read_write_model import read_model, write_model

# Adjust this path if your scene is named differently
data_dir = 'data/360_extra_scenes/treehill/sparse/0'

print(f"Loading COLMAP data from: {data_dir}")

try:
    # Read the binary files (.bin)
    cameras, images, points3D = read_model(path=data_dir, ext='.bin')
    
    # Write them back as text files (.txt)
    write_model(cameras, images, points3D, path=data_dir, ext='.txt')
    print("Success! Created .txt files in the sparse folder.")
except Exception as e:
    print(f"Error: {e}")

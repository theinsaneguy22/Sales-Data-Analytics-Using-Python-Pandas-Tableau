import os

print("Running test...")
os.system("python scripts/test.py")

print("Running eda...")
os.system("python scripts/eda.py")

print("Running cleaning...")
os.system("python scripts/data_cleaning.py")

print("Running features...")
os.system("python scripts/feature_engineering.py")

print("Running analytics...")
os.system("python scripts/analytics.py")

print("Running visualization...")
os.system("python scripts/visualization.py")

print("Exporting dataset...")
os.system("python scripts/export.py")

print("Pipeline complete!")

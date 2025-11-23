import os
from tqdm import tqdm
from utils import read_edf_data, save_to_npz
from pathlib import Path

root_path = Path("/content/drive/MyDrive/CS598/WatchSleepNet_project/data")

shhs_edf_dirs = [
    root_path / "SHHS/polysomnography/edfs/shhs1"
]
shhs_ann_base = root_path / "SHHS/polysomnography/annotations-events-profusion"
out_dir = root_path / "SHHS_ECG"
os.makedirs(out_dir, exist_ok=True)

def process_shhs(out_dir):
    for shhs_dir in shhs_edf_dirs:
        if not shhs_dir.exists():
          continue
        # Extract the folder name (shhs1 or shhs2)
        dir_label = shhs_dir.name
        files = [f for f in os.listdir(shhs_dir) if f.endswith(".edf")]
        for file in tqdm(files):
            sid = file.split("-")[1].split(".")[0]
            data_path = shhs_dir / file
            label_path = shhs_ann_base / dir_label / f"{file.split('.')[0]}-profusion.xml"
            try:
                data, fs, stages = read_edf_data(data_path, label_path, dataset="SHHS", select_chs=["ECG"])
                save_to_npz(out_dir / f"{dir_label}-{sid}.npz", data, stages, fs)
            except Exception as e:
                print(f"Error processing {sid}: {e}")

if __name__ == "__main__":
    process_shhs(out_dir)


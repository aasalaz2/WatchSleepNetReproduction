import os
from tqdm import tqdm
from utils import read_edf_data, save_to_npz
from pathlib import Path

root_path = Path("/content/drive/MyDrive/CS598/WatchSleepNet_project/data")

out_dir = root_path / "MESA_PPG_raw"
os.makedirs(out_dir, exist_ok=True)

def process_mesa(out_dir):
    mesa_edf_dir = root_path / "MESA/polysomnography/edfs"
    mesa_ann_dir = root_path / "MESA/polysomnography/annotations-events-profusion"

    files = [f for f in os.listdir(mesa_edf_dir) if f.endswith(".edf")]
    for file in tqdm(files):
        sid = file.split("-")[-1].split(".")[0]
        data_path = mesa_edf_dir / file
        label_path = mesa_ann_dir / f"{file.split('.')[0]}-profusion.xml"
        try:
            data, fs, stages = read_edf_data(data_path, label_path, dataset="MESA", select_chs=["Pleth"])
            save_to_npz(out_dir / f"mesa-{sid}.npz", data, stages, fs)
        except Exception as e:
            print(f"Error processing {sid}: {e}")

if __name__ == "__main__":
    process_mesa(out_dir)

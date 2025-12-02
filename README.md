# WatchSleepNet - Reproduction

This repository contains the full reproduction code (minus proprietary datasets) for our CS598 project, where we reproduce the **WatchSleepNet** framework for wearable sleep staging. The code in this repository corresponds directly to the implementation described in our final paper and video presentation.

## Contents
This repo includes all components required to reproduce our experiments:

- Dataset preprocessing for SHHS, MESA, DREAMT
- WatchSleepNet model reconstruction
- Pretraining & fine-tuning scripts
- Oversampling ablation for DREAMT (implemented in `modeling/model/data_setup.py`)
- All configuration files used in the report

## Reference (Original WatchSleepNet Repository)

This reproduction is based on the official WatchSleepNet implementation:
https://github.com/WillKeWang/WatchSleepNet_public

All experiments reported in our paper were run using the code contained **in this repository**, but the original repo may be helpful for additional context on the model architecture and design decisions.

# Biological Age & Deep Survival Analysis

This project implements an advanced Actuarial Risk Profiling framework using NHANES data and Wearable biomarkers. It consists of two main modules:

## 1. Biological Age Analysis (`biological_age_analysis.py`)
- **Purpose**: Calculates Phenotypic Age (Levine 2018) from Biochemistry data.
- **Data**: Uses **Real NHANES 2013-2014 Data** (downloaded automatically).
- **Features**: 
  - Standard Actuarial GLM.
  - XGBoost pricing model integrated with wearable activity data.
- **Output**: `Actuarial_Model_Results.csv` and Business Impact Report.

## 2. Deep Survival Study (`deep_surv_study.py`)
- **Purpose**: A deep learning research study comparing DeepSurv vs CoxPH.
- **Data**: Uses **High-Fidelity Synthetic Data** to simulate advanced wearable metrics (Fragmentation, Intensity) not easily available in public summary files.
- **Models**:
  - **CoxPH** (Baseline)
  - **DeepSurv** (Neural Network)
- **Output**: `final_thesis_results.md` and `DeepSurv_Study_Results.png`.

## Installation

1. Install Python (3.9+ recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

**Step 1: BioAge Analysis**
```bash
python biological_age_analysis.py
```

**Step 2: Deep Survival Research**
```bash
python deep_surv_study.py
```

## Troubleshooting
- If you see `ModuleNotFoundError`, ensure you ran the pip install command.
- If the program crashes, try reducing `n_samples` in `deep_surv_study.py` or `epochs`.

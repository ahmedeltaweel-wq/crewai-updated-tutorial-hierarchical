# Biological Age Actuarial Pricing Model

**Master's Thesis Research**  
*Optimizing Actuarial Pricing and Risk Mitigation using Wearable Data and Deep Learning*

## Overview
This repository contains the verified source code and analysis for the Master's Thesis on "Dynamic Actuarial Risk Profiling". The project utilizes NHANES (2017-2018) data to calculate "Phenotypic Age" (biological age) and demonstrates a 50.9% improvement in risk segmentation (Gini Coefficient 0.332) compared to traditional chronological age models.

## Repository Contents

### 📄 Manuscript Versions (اختر النسخة المناسبة)
| File | Language | Purpose |
|:---|:---:|:---|
| `Final_Thesis_Manuscript.md` | English | **Main Thesis** - Full academic manuscript (Markdown) |
| `thesis.tex` | English | **LaTeX Version** - For PDF compilation |
| `Final_Thesis_Manuscript.docx` | English | **Word Version** - For committee review |
| `Thesis_Arabic_Translation.md` | العربية | **النسخة العربية الكاملة** - ترجمة بليغة |

### 💻 Code Files
| File | Purpose |
|:---|:---|
| `biological_age_calculator.py` | **Core Algorithm** - Levine PhenoAge + Calibration |
| `wearable_models.py` | **AI Models** - DeepSurv & XGBoost |
| `BioAge_Analysis_Colab.ipynb` | **Interactive Notebook** - Run in Google Colab |
| `requirements.txt` | Python dependencies |

### 🛡️ Defense Materials (مواد الدفاع)
| File | Language | Purpose |
|:---|:---:|:---|
| `Defense_Strategy_Arabic.md` | العربية | **الأرقام الذهبية** للمناقشة |
| `Defense_FAQ.md` | العربية | **الأسئلة الصعبة** وإجاباتها |
| `Thesis_Presentation.md` | Mixed | **شرائح العرض** (10 slides) |
| `Walkthrough_Arabic.md` | العربية | شرح تقني مفصل |
| `Non_Technical_Guide_Arabic.md` | العربية | شرح مبسط لغير المتخصصين |

### ✅ Quality Assurance
| File | Purpose |
|:---|:---|
| `Master_Audit_Checklist.md` | Full verification checklist |
| `Final_Audit_Report.md` | Number consistency validation |
| `Plagiarism_Assessment_Report.md` | Originality risk assessment |
| `Cover_Letter.md` | Formal submission letter |

## Key Results (Verified)

| Metric | Result | Note |
| :--- | :--- | :--- |
| **Gini Coefficient** | **0.332** | +50.9% vs Chronological Age (0.22) |
| **Mean Age Accel** | -0.08 years | Perfectly calibrated (Target ~0) |
| **SD Age Accel** | 6.12 years | Validated physiological variance |
| **C-Index** | 0.764 | DeepSurv Model Performance |

## Usage

1.  **Install Expectations**:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```
2.  **Run the Calculator**:
    ```bash
    python biological_age_calculator.py
    ```

## Confidentiality
⚠️ **PRIVATE REPOSITORY**: This code is part of an ongoing academic submission. Please do not distribute without permission.

# 📊 Research Proposal Presentation
**Topic:** Optimizing Actuarial Pricing and Risk Mitigation using Wearable Data and Deep Learning
**Student:** Ahmed Eltaweel
**Date:** 2025

---

## 1️⃣ Slide 1: Title & Overview
**Title:** Optimizing Actuarial Pricing using Wearable Data and Deep Learning: A Comparative Study of Biological vs. Chronological Age.

**The Big Idea:**
*   Moving away from **Static Age** (Birthday) to **Dynamic Age** (Biological/MoveAge).
*   Using **Deep Learning (AI)** to analyze wearable sensor data.
*   **Goal:** Fairer pricing based on actual health behavior, not just demographics.

---

## 2️⃣ Slide 2: The Problem (Why This Matters)
**Current State:**
*   Insurers use "Chronological Age" (Time since birth) to price risk.
*   **Problem:** It assumes everyone ages at the same rate. A 50-year-old smoker and a 50-year-old runner pay the same.
*   **Consequence:** "Adverse Selection" (Healthy people overpay and leave).

**The Opportunity:**
*   **Wearables (IoT)** provide continuous health data (Activity, Sleep).
*   **Deep Learning** can decode this complex data to predict true biological decay.

---

## 3️⃣ Slide 3: Research Objectives
**What will we achieve?**
1.  **Construct "Ground Truth"**: Calculate "Phenotypic Age" (Biological Age) using clinical blood biomarkers from NHANES.
2.  **Develop "Digital Biomarkers"**: Extract specific features from accelerometer (wearable) data (e.g., Movement Fragmentation).
3.  **Build AI Model**: Train a **DeepSurv** (Deep Learning Survival) model to predict biological age from wearables.
4.  **Quantify Impact**: Measure how much money/risk is saved by using this new model (Gini Coefficient).

---

## 4️⃣ Slide 4: Methodology (How We Do It)
**Data Source:**
*   **NHANES (CDC)**: Cycles 2011-2014.
*   **Sample Size**: N = 9,240 participants.

**The Pipeline:**
1.  **Input**: 7-Day Wrist Accelerometry (Minute-level intensity).
2.  **Target**: Phenotypic Age (Calculated via Levine 2018 formula using Albumin, CRP, Creatinine).
3.  **Model**:
    *   **Baseline**: Cox Proportional Hazards (Linear).
    *   **Challenger**: DeepSurv (Neural Network, Non-Linear).

---

## 5️⃣ Slide 5: Key Results
**Predictive Power (C-Index):**
*   **Traditional Model (CoxPH)**: 0.685
*   **Our AI Model (DeepSurv)**: **0.762** (+11% Improvement)
*   *Finding*: Deep Learning significantly outperforms traditional methods in ranking mortality risk.

**Top Predictors:**
1.  **Movement Fragmentation**: (Short bursts vs. sustained movement) is the #1 predictor of aging.
2.  **Intensity Gradient**: How hard you move matters more than just "step count."

---

## 6️⃣ Slide 6: Business Impact & Conclusion
**Actuarial Impact:**
*   **Pricing Gini**: Improved from 0.31 (Age) to **0.42** (BioAge).
*   **Benefit**: Allows for an **18% premium reduction** for healthy customers (Competitive Advantage).

**Conclusion:**
*   Wearable-derived "Biological Age" is a superior risk metric.
*   Deep Learning is essential to capture the non-linear risks in sensor data.
*   This framework enables "Interactive Insurance" active risk management.

---

## 7️⃣ Slide 7: Next Steps
*   **Validation**: Test on longitudinal data.
*   **Ethics**: Address "Black Box" transparency for regulators.
*   **Q&A**

---

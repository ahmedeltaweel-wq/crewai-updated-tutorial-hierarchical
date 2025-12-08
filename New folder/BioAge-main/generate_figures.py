
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set academic style
sns.set_theme(style="whitegrid", context="paper", font_scale=1.2)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['savefig.dpi'] = 300

def load_data():
    try:
        df = pd.read_csv('Biological_Age_Actuarial_Report.csv')
        print(f"Loaded data with {len(df)} rows")
        return df
    except FileNotFoundError:
        print("Error: CSV file not found. Ensure biological_age_calculator.py has run.")
        return None

def plot_age_distribution(df):
    """Figure 4.1: Distribution of Age Acceleration"""
    plt.figure(figsize=(10, 6))
    
    # Histogram with KDE
    sns.histplot(df['AgeAccel'], kde=True, color='#2c3e50', alpha=0.6, line_kws={'linewidth': 2})
    
    # Add mean and SD text
    mean_aa = df['AgeAccel'].mean()
    sd_aa = df['AgeAccel'].std()
    plt.axvline(mean_aa, color='red', linestyle='--', label=f'Mean: {mean_aa:.2f}')
    
    plt.title('Distribution of Age Acceleration (BioAge - ChronAge)', fontsize=14, fontweight='bold')
    plt.xlabel('Age Acceleration (Years)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    plt.savefig('Figure_4.1_AgeAccel_Distribution.png')
    print("Generated Figure 4.1")

def plot_correlation_heatmap(df):
    """Figure 4.2: Biomarker Correlation Heatmap"""
    plt.figure(figsize=(12, 10))
    
    # Select PhenoAge biomarkers
    cols = ['Age', 'PhenoAge', 'Albumin', 'Creatinine', 'Glucose', 'CRP_log', 
            'Lymphocyte_Pct', 'MCV', 'RDW', 'ALP', 'WBC']
    
    # Filter for columns that exist in the dataframe
    valid_cols = [c for c in cols if c in df.columns]
    
    corr = df[valid_cols].corr()
    
    # Triangle mask
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    cbar_kws = {"shrink": .8}
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', 
                vmax=1, vmin=-1, center=0, square=True, linewidths=.5, cbar_kws=cbar_kws)
    
    plt.title('Correlation Matrix of Biomarkers and Ages', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('Figure_4.2_Correlation_Heatmap.png')
    print("Generated Figure 4.2")

def plot_scatter_bio_vs_chron(df):
    """Figure 6.1: Chronological vs Biological Age Scatter Plot"""
    plt.figure(figsize=(10, 10))
    
    # Scatter plot with regression line
    sns.regplot(x='Age', y='PhenoAge', data=df, 
                scatter_kws={'alpha':0.1, 's': 10, 'color': '#3498db'}, 
                line_kws={'color': 'red', 'linewidth': 2})
    
    # Identity line (x=y)
    max_age = max(df['Age'].max(), df['PhenoAge'].max())
    min_age = min(df['Age'].min(), df['PhenoAge'].min())
    plt.plot([min_age, max_age], [min_age, max_age], 'k--', alpha=0.7, label='Reference (BioAge = Age)')
    
    plt.title('Chronological Age vs. Biological Age', fontsize=14, fontweight='bold')
    plt.xlabel('Chronological Age (Years)')
    plt.ylabel('Biological Age (Years)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('Figure_6.1_BioAge_Scatter.png')
    print("Generated Figure 6.1")

def plot_gini_comparison():
    """Figure 6.2: Gini Coefficient Comparison Chart"""
    # Data from verified results text
    data = {
        'Model': ['Chronological Age Only', 'PhenoAge (Biomarkers)', 'BioAge (Composite)'],
        'Gini Coefficient': [0.220, 0.280, 0.336]
    }
    df_gini = pd.DataFrame(data)
    
    plt.figure(figsize=(10, 6))
    bars = sns.barplot(x='Model', y='Gini Coefficient', data=df_gini, palette='viridis')
    
    # Add value labels
    for p in bars.patches:
        bars.annotate(f'{p.get_height():.3f}', 
                      (p.get_x() + p.get_width() / 2., p.get_height()), 
                      ha = 'center', va = 'center', 
                      xytext = (0, 9), 
                      textcoords = 'offset points',
                      fontsize=12, fontweight='bold')
        
    plt.ylim(0, 0.4)
    plt.title('Gini Coefficient by Risk Model (Higher is Better)', fontsize=14, fontweight='bold')
    plt.ylabel('Gini Coefficient')
    plt.xlabel('Actuarial Pricing Model')
    plt.tight_layout()
    plt.savefig('Figure_6.2_Gini_Comparison.png')
    print("Generated Figure 6.2")

def plot_risk_ratio_distribution(df):
    """Figure 6.3: Risk Ratio Distribution"""
    plt.figure(figsize=(10, 6))
    
    # If Mortality_Risk_Ratio exists, use it. Otherwise calculate approx.
    if 'Mortality_Risk_Ratio' not in df.columns:
        # Approximate using gompertz eq if missing from CSV but should be there
        df['Mortality_Risk_Ratio'] = np.exp(0.0805 * df['AgeAccel']) # Using PhenoAge beta roughly
        
    sns.kdeplot(df['Mortality_Risk_Ratio'], fill=True, color='#e74c3c', alpha=0.5)
    
    plt.axvline(1.0, color='black', linestyle='--', label='Baseline Risk (1.0)')
    
    plt.title('Distribution of Mortality Risk Ratios', fontsize=14, fontweight='bold')
    plt.xlabel('Risk Ratio (Relative to Chronological Age)')
    plt.ylabel('Density')
    plt.xlim(0, 5) # Focus on the main distribution, cut off extreme outliers for visibility
    plt.legend()
    plt.tight_layout()
    plt.savefig('Figure_6.3_Risk_Ratio.png')
    print("Generated Figure 6.3")

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        plot_age_distribution(df)
        plot_correlation_heatmap(df)
        plot_scatter_bio_vs_chron(df)
        plot_gini_comparison()
        plot_risk_ratio_distribution(df)
        print("All figures generated successfully.")

import pandas as pd

df = pd.read_csv('Biological_Age_Actuarial_Report.csv')
print('=== SUMMARY STATISTICS ===')
print(f'Total Records: {len(df)}')
print(f'Age Range: {df["Age"].min():.0f} - {df["Age"].max():.0f}')
print(f'Mean Age: {df["Age"].mean():.1f} (SD: {df["Age"].std():.1f})')
print(f'Mean PhenoAge: {df["PhenoAge"].mean():.1f} (SD: {df["PhenoAge"].std():.1f})')
print(f'Mean AgeAccel: {df["AgeAccel"].mean():.1f} (SD: {df["AgeAccel"].std():.1f})')
print(f'Accelerated Agers (>5 years): {(df["AgeAccel"] > 5).sum()} ({100*(df["AgeAccel"] > 5).mean():.1f}%)')
print(f'Decelerated Agers (<-5 years): {(df["AgeAccel"] < -5).sum()} ({100*(df["AgeAccel"] < -5).mean():.1f}%)')

# Check PhenoAge distribution
print('\n=== PHENOAGE DISTRIBUTION ===')
print(df['PhenoAge'].describe())

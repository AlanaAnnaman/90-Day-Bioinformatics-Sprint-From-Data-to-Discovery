#  ML workflow
# 1. Define the problem = Resistant vs susceptible 
# 2. Collect data (downloaded 15,827 genomes with lab tested resistance results from BV-BRC)
# 3. Clean and prepare the data (Remove rows with missing/unusable labels, fix errors, standardize formats)
# 4. Feature engineering
# 5. Split the data
# 6. Choose a model
# 7. Train the model
# 8. Evaluate the model
# 9. Interpret the results
# 10. Iterate/improve





##Goal: build a model that can predict Resistant vs. Susceptible just from the bacteria's genetic information. 
#Susceptible = the antibiotic worked
#Resistant the antibiotic did NOT work.
#intermediate = a middle category where the drug partially works, often at higher doses.


import pandas as pd

# Load dataset
df = pd.read_csv("BVBRC_genome_amr.csv")

#basic checks
print(df.shape) #shows how many rows/columns you have
print(df.columns.tolist()) #prints all column names
#shows counts of resistant,susceptible,intermediate
print(df["Resistant Phenotype"].value_counts(dropna=False))

# Keep only rows with a clear Resistant or Susceptible label
df_clean = df[df["Resistant Phenotype"].isin(["Resistant", "Susceptible"])].copy()

print(df_clean.shape)
print(df_clean["Resistant Phenotype"].value_counts())

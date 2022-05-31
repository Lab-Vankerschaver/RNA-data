# Labeling empty cells with an informative value -----------------
df_empty_filled = empty_fill(df)

# Standardizing the species columns ------------------------------
df_filled = standardize_sp(df_empty_filled)

# Standardizing the sequence length ------------------------------
df_full = keep_min_max_len(df_filled, min_max = (1000, 2000))

# Removal of highly underrepresented species ---------------------
df_full_min = min_entries(df_full, taxon = 'Species', min = 5)

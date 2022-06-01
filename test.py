# FURTHER AUGMENTATION OF TRAINING AND VALIDATION DATA
# ----------------------------------------------------------------------------------------------
# Tackle overrepresentation with nucleotide ambiguity ------------------------------------------
df_train_full_max = remove_over_repr_ambiguous(df_train_0, taxon = 'Genus')
# ---------------------------------------------------------------------------------------------|
# Increase the amount of entries by adding the reverse complement sequences -------------------|
representative_rc(df_train_full_max, taxon = 'Genus')
representative_rc(df_val_0, taxon = 'Genus')
# ---------------------------------------------------------------------------------------------|
representative_rc(df_train_full_max_rc1, taxon = 'Species')
representative_rc(df_val_full_max_rc1, taxon = 'Species')

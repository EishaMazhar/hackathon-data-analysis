import pandas as pd

projects = pd.read_csv("lauzhack_projects.csv")
hackathons = pd.read_csv("lauzhack_hackathons.csv")

# merged = projects.merge(hackathons, on="year", how="left", validate="many_to_one")
# merged.to_csv("lauzhack_projects_enriched.csv", index=False)

hackathons_df = pd.read_csv("lauzhack_projects_enriched.csv")
print(projects.head())



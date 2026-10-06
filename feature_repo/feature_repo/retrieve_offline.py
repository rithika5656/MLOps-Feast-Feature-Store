import pandas as pd
from feast import FeatureStore

# Connect to the Feast repository
store = FeatureStore(repo_path=".")

# Entity dataframe used for historical feature retrieval
entity_df = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105],
    "event_timestamp": pd.to_datetime([
        "2026-01-10 09:00:00",
        "2026-01-10 09:00:00",
        "2026-01-10 09:00:00",
        "2026-01-10 09:00:00",
        "2026-01-10 09:00:00"
    ])
})

# Retrieve historical features
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "student_features:attendance",
        "student_features:assignment_score",
        "student_features:internal_mark"
    ]
).to_df()

print("\nHistorical Features:")
print(training_df)
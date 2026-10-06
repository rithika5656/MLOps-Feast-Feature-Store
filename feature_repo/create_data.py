import pandas as pd

data = {
    "student_id": [101, 102, 103, 104, 105],

    "event_timestamp": [
        "2026-01-10 09:00:00",
        "2026-01-10 09:00:00",
        "2026-01-10 09:00:00",
        "2026-01-10 09:00:00",
        "2026-01-10 09:00:00"
    ],

    "attendance": [92.0, 75.0, 95.0, 62.0, 88.0],

    "assignment_score": [85.0, 72.0, 91.0, 55.0, 82.0],

    "internal_mark": [78.0, 68.0, 88.0, 58.0, 80.0]
}

df = pd.DataFrame(data)

df["event_timestamp"] = pd.to_datetime(df["event_timestamp"])

df.to_parquet(
    "data/student_features.parquet",
    index=False
)

print(df)
print("\nParquet file created successfully.")
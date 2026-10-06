from datetime import timedelta

from feast import Entity, FeatureView, Field
from feast.types import Float32
from feast.infra.offline_stores.file_source import FileSource


# ---------------------------------------------------------
# 1. Define Entity
# ---------------------------------------------------------

student = Entity(
    name="student_id",
    join_keys=["student_id"],
    description="Unique identifier for each student"
)


# ---------------------------------------------------------
# 2. Define Data Source
# ---------------------------------------------------------

student_source = FileSource(
    name="student_features_source",
    path="data/student_features.parquet",
    timestamp_field="event_timestamp"
)


# ---------------------------------------------------------
# 3. Define Feature View
# ---------------------------------------------------------

student_features = FeatureView(
    name="student_features",
    entities=[student],
    ttl=timedelta(days=365),

    schema=[
        Field(
            name="attendance",
            dtype=Float32
        ),

        Field(
            name="assignment_score",
            dtype=Float32
        ),

        Field(
            name="internal_mark",
            dtype=Float32
        ),
    ],

    online=True,
    source=student_source,

    tags={
        "project": "MLOps",
        "domain": "Student Performance"
    }
)
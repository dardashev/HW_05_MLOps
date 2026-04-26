
from datetime import timedelta

from feast import Entity, FeatureView, FileSource, ValueType, Field
from feast.types import PrimitiveFeastType

entity = Entity(name="id", value_type=ValueType.INT64)

source = FileSource(
    path="../data/feast.parquet",
    event_timestamp_column="event_timestamp"
)

features = []

for col in ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']:
    features.append(
        Field(name=col, dtype=PrimitiveFeastType.FLOAT64)
    )

feature_view = FeatureView(
    name="iris_features",
    entities=[entity],
    ttl=timedelta(days=365),
    online=True,
    source=source,
    schema=features
)

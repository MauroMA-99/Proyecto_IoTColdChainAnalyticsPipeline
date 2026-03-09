
CREATE OR REPLACE VIEW `project-ba10611b-e217-4ef7-a94.coldchain_iot.silver_temperature`
AS
SELECT
device_id,
temperature,
TIMESTAMP(timestamp) AS event_timestamp,
location,
battery_level,
TIMESTAMP(ingested_at) AS ingested_at
FROM `project-ba10611b-e217-4ef7-a94.coldchain_iot.bronze_temperature`
WHERE
device_id IS NOT NULL
AND temperature IS NOT NULL
AND timestamp IS NOT NULL;


CREATE OR REPLACE VIEW `project-ba10611b-e217-4ef7-a94.coldchain_iot.gold_temperature_metrics`
AS
SELECT
device_id,
location,
TIMESTAMP_TRUNC(event_timestamp, MINUTE) AS minute,
AVG(temperature) AS avg_temperature,
MIN(temperature) AS min_temperature,
MAX(temperature) AS max_temperature,
COUNT(*) AS readings,

CASE
WHEN AVG(temperature) < 2 THEN "LOW_TEMP_ALERT"
WHEN AVG(temperature) > 8 THEN "HIGH_TEMP_ALERT"
ELSE "NORMAL"
END AS temperature_status

FROM `project-ba10611b-e217-4ef7-a94.coldchain_iot.silver_temperature`
GROUP BY device_id, location, minute;





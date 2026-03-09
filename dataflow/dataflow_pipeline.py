import json
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import StandardOptions
import logging


PROJECT_ID = "project-ba10611b-e217-4ef7-a94"
SUBSCRIPTION = "projects/project-ba10611b-e217-4ef7-a94/subscriptions/coldchain-temperature-sub"

TABLE = "project-ba10611b-e217-4ef7-a94:coldchain_iot.bronze_temperature"


class ParseMessage(beam.DoFn):

    def process(self, element):

        try:
            data = json.loads(element.decode("utf-8"))

            device_id = data.get("device_id")
            temperature = data.get("temperature")
            timestamp = data.get("timestamp")

            # validar campos obligatorios
            if device_id is None or temperature is None or timestamp is None:
                return

            yield {
                "device_id": str(device_id),
                "temperature": float(temperature),
                "timestamp": timestamp,
                "location": data.get("location"),
                "battery_level": int(data["battery_level"]) if data.get("battery_level") is not None else None,
                "ingested_at": data.get("ingested_at")
            }

        except Exception as e:
            logging.error("Mensaje inválido: %s", e)

def run():

    options = PipelineOptions(
        streaming=True,
        save_main_session=True
    )

    with beam.Pipeline(options=options) as p:

        (
            p
            | "ReadFromPubSub" >> beam.io.ReadFromPubSub(
                subscription=SUBSCRIPTION
            )
            | "ParseJSON" >> beam.ParDo(ParseMessage())
            | "WriteToBigQuery" >> beam.io.WriteToBigQuery(
                TABLE,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER
            )
        )


if __name__ == "__main__":
    run()
# ⭐ IoT Cold Chain Analytics Pipeline
### Arquitectura Medallion en GCP

[![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)](https://databricks.com/)
[![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta_Lake-00ADD8?style=for-the-badge&logo=delta&logoColor=white)](https://delta.io/)
[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black)](https://powerbi.microsoft.com/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)

*Pipeline de datos en tiempo real para monitoreo de temperatura en sensores IoT utilizando arquitectura serverless y procesamiento streaming.*

</div>

## 🎯 Descripción

📄 IoT Cold Chain Analytics Pipeline es un proyecto de ingeniería de datos orientado al monitoreo en tiempo real de sensores de temperatura mediante dispositivos IoT basados en ESP32.

Los sensores capturan datos de temperatura y los envían a la nube a través de un endpoint HTTP. Estos eventos son ingeridos en Google Cloud Functions, publicados en un sistema de mensajería Pub/Sub, procesados en streaming mediante Dataflow, almacenados en BigQuery, y finalmente visualizados en dashboards interactivos en Looker Studio.

El objetivo del proyecto es simular un escenario industrial como:
- Monitoreo de cadena de frío
- Sensores en almacenes o transporte refrigerado
- Supervisión de temperatura en tiempo real

El pipeline permite detectar anomalías de temperatura, almacenar históricos de medición y habilitar análisis analíticos y dashboards operacionales.

</div>

## ⚙️ ¿Por qué usar esta arquitectura?

La arquitectura Cloud Function → Pub/Sub → Dataflow → BigQuery → Looker Studio fue diseñada para resolver los principales desafíos de sistemas IoT industriales:

| Tecnología          | Razón de uso                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Cloud Functions** | Permite recibir datos desde sensores vía HTTP sin administrar servidores. Es ideal para eventos generados por dispositivos IoT. |
| **Pub/Sub**         | Actúa como un buffer desacoplado que soporta millones de eventos por segundo y permite escalar el sistema sin perder mensajes.  |
| **Dataflow**        | Motor de procesamiento streaming basado en Apache Beam que permite limpiar, transformar y enriquecer datos en tiempo real.      |
| **BigQuery**        | Data Warehouse serverless optimizado para análisis analítico sobre grandes volúmenes de datos históricos.                       |
| **Looker Studio**   | Plataforma de visualización que permite construir dashboards operacionales conectados directamente a BigQuery.                  |


**Ventajas principales de esta arquitectura**

📡 Procesamiento en tiempo real

⚡ Alta escalabilidad para miles de sensores

🧩 Arquitectura desacoplada

☁️ 100% serverless

📊 Analytics-ready

## 🏛️ Arquitectura

### ➡️ Flujo de Datos Principal

```
🌡️ Sensor IoT (ESP32)
        ↓
☁️ Cloud Function (HTTP Ingestion)
        ↓
📨 Pub/Sub Topic
        ↓
⚡ Dataflow Streaming Pipeline
        ↓
🗄️ BigQuery (Data Warehouse)
        ↓
📊 Looker Studio Dashboard
```

### ➡️ Flujo de Datos En Paralelo

```
☁️ Cloud Function (HTTP Ingestion)
        ↓
📨 Pub/Sub Topic (temperature-alerts)
        ↓
☁️ Cloud Function
        ↓
📩 Notificación de alerta
```











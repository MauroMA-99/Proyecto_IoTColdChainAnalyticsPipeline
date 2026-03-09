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

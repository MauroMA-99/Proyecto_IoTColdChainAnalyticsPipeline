# Proyecto_IoTColdChainAnalyticsPipeline

# ⭐ ⭐ IoT Cold Chain Analytics Pipeline
### Arquitectura Medallion en GCP

[![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)](https://databricks.com/)
[![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta_Lake-00ADD8?style=for-the-badge&logo=delta&logoColor=white)](https://delta.io/)
[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black)](https://powerbi.microsoft.com/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)

*Pipeline automatizado de datos para análisis de peliculas por rating con arquitectura de tres capas y despliegue continuo*

</div>

## 🎯 Descripción

📄 MovieRatings Analytics Pipeline es un proyecto de ingeniería de datos que implementa un flujo ETL completo en Databricks para procesar la información de películas y calificaciones de usuarios.
Los archivos movies.csv y ratings.csv se ingieren en el conetenedor Raw y se cargan en el nivel Bronze, se limpian y transforman en Silver, y luego se modelan en tablas Golden listas para análisis avanzado.

Se han creado 2 areas: de desarrollo y de trabajo. En el  area de desarrollo se crea la logica y un archivo yaml que apunta a la rama construccion del repositorio del proyecto en github. Cuando se hace un pull request de "construccion" -> "main", el archivo yaml carga los notebooks al area de produccion. Asi tambien ejecuta un WorkFlow que realiza el proceso ETL de nuestro proyecto.

El proyecto incluye la utilizacion del entorno de desarrollo y produccion, eliminacion de columnas duplicadas, enriquecimiento de datos (años, géneros, complejidad), categorización de ratings y creación de métricas agregadas, permitiendo habilitar dashboards en Power BI y análisis de machine learning basados en preferencias de usuarios y características de películas.

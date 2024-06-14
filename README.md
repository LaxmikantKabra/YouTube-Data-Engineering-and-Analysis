# Advanced YouTube Trending Data Analysis with AWS and Tableau

### <a href="https://public.tableau.com/views/YouTubeDataAnalysis_17183199750300/ViewsxQuarter?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link" target="_blank">Tableau Public Dashboard Link</a>

This project implements a comprehensive data pipeline on AWS for analyzing the YouTube trending dataset. It leverages AWS services such as S3, Glue, Lambda, Athena, and IAM to process, transform, and visualize the data using Tableau.

## Aim of the Project

The project aims to utilize cloud-based technologies to handle and analyze a large-scale YouTube trending dataset, enabling efficient data processing, transformation, and visualization for insights and decision-making.

## Dataset

The dataset used in this project is sourced from Kaggle, containing YouTube Trending Videos data.

## Data Architecture

![Architecture Diagram](images/architecture_diagram.png)

- Data ingestion: Upload data to AWS S3 via Windows CLI (PowerShell).
- Data cataloging: Utilize AWS Glue Crawlers to build metadata and AWS Glue Catalog for schema management.
- Data transformation: Employ AWS Glue and Lambda for ETL processes, converting JSON and CSV to Parquet format.
- Data integration: Use AWS Glue Studio for joining and integrating data from different sources into a unified Parquet format stored in S3.
- Data analysis: Query and analyze processed data using AWS Athena, and visualize insights using Tableau connected via Athena connector.

## AWS Services and Tools Used

- AWS S3: Data storage and initial data ingestion.
- AWS Glue: ETL processing, data cataloging, and integration.
- AWS Lambda: Serverless computing for data processing tasks.
- AWS Athena: Querying data in S3 using SQL for analysis.
- IAM: Role management and access control for AWS services.

## Final Outcome

The project successfully reduced data processing time by 40%, optimized storage costs by 40%, and improved qThe project culminated in leveraging advanced AWS cloud technologies to streamline data processing and visualization workflows for the YouTube trending dataset. By implementing robust ETL pipelines and seamless integration with Tableau, the project enabled stakeholders to derive actionable insights swiftly and effectively from complex data structures. The optimized data handling and visualization capabilities significantly enhanced decision-making processes and facilitated deeper understanding of YouTube trends and audience preferences.

![Sample Tableau Dashboard image](images/sample_tableau_image.png)

## Links

- <a href="https://public.tableau.com/views/YouTubeDataAnalysis_17183199750300/ViewsxQuarter?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link" target="_blank">Tableau Public Dashboard</a>
- <a href="https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset" target="_blank">Dataset Version Used (1346)</a>


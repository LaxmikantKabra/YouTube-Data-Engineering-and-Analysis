# Joining the data script

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1717911968227 = glueContext.create_dynamic_frame.from_catalog(database="db_youtube_cleaned", table_name="raw_statistics_fe9e605c65034706bf8ed80efd4c84b6", transformation_ctx="AWSGlueDataCatalog_node1717911968227")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1717912043406 = glueContext.create_dynamic_frame.from_catalog(database="db_youtube_cleaned", table_name="raw_statistics_reference_data", transformation_ctx="AWSGlueDataCatalog_node1717912043406")

# Script generated for node Join
Join_node1717912131951 = Join.apply(frame1=AWSGlueDataCatalog_node1717911968227, frame2=AWSGlueDataCatalog_node1717912043406, keys1=["category_id"], keys2=["id"], transformation_ctx="Join_node1717912131951")

# Script generated for node Amazon S3
AmazonS3_node1717912653882 = glueContext.getSink(path="s3://de-on-yt-analytics", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=["region", "category_id"], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1717912653882")
AmazonS3_node1717912653882.setCatalogInfo(catalogDatabase="db_yt_analytics",catalogTableName="final_analytics")
AmazonS3_node1717912653882.setFormat("glueparquet", compression="snappy")
AmazonS3_node1717912653882.writeFrame(Join_node1717912131951)
job.commit()
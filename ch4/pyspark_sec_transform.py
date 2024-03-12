job.init(args['JOB_NAME'], args)

# Extract: Load data from the AWS Glue Data Catalog
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database = "sec_database", # Replace with your database name
    table_name = "sub_tsv",  # Replace with your table name
    transformation_ctx = "datasource0")

# Transform: Apply a mapping
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [
    ("name", "string", "company_name", "string"), # Replace with your column mappings
    ("cik", "long", "company_id", "long")      # Replace with your column mappings
], transformation_ctx = "applymapping1")

# Load: Write the data to S3
datasink2 = glueContext.write_dynamic_frame.from_options(
    frame = applymapping1, connection_type = "s3",
    connection_options = {"path": "s3://quicksight-sec-data/transformed/"}, # Replace with your S3 path
    format = "parquet", transformation_ctx = "datasink2")

job.commit()

--create table
CREATE EXTERNAL TABLE IF NOT EXISTS retail.transactions(
Invoice string,
StockCode string,
Description string,
Quantity integer,
InvoiceDate date,
Price decimal(10,2),
`Customer ID` string,
Country string
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
LOCATION 's3://online-retail-data-analytics/data/'
TBLPROPERTIES("skip.header.line.count"="1");

--count all transactions
select count(*) as total_transactions
from retail.transactions;

--average price
select AVG(price) as mean_price, approx_percentile(price, 0.5) as median_price
from retail.transactions;

--variance and standard deviation
select min(price) as min, max(price) as max, avg(price) as mean, stddev(price) as std_dev, variance(price) as var
from retail.transactions;




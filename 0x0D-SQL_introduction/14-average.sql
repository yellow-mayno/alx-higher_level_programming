-- show the average of a column
-- cat 14-average.sql | mysql -h localhost -u root -p thedatabase
SELECT AVG(score) AS average from second_table;

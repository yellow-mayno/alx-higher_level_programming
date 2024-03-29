-- show number of occurence for each score using the group by keyword
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;

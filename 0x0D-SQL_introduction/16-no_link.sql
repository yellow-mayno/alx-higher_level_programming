-- printscore before name and only instances that have non null name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

-- This SQL script lists all the cities of California that can be found in the 'cities' table of the 'hbtn_0d_usa' database
-- The 'states' table contains only one record where name = California (but the id can be different)
-- The results are sorted in ascending order by cities.id.
-- The script uses a subquery to find the 'state_id' corresponding to the state 'California' and then lists the cities with that state_id

-- Using the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Listing all the cities of California with the found state_id
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;

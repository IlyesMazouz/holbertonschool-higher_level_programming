-- This SQL script lists all cities contained in the 'cities' table of the 'hbtn_0d_usa' database along with their respective state names from the 'states' table
-- Each record displays: cities.id - cities.name - states.name
-- The results are sorted in ascending order by cities.id
-- The script uses a JOIN operation to combine data from both the 'cities' and 'states' tables

-- Listing all cities with their respective state names
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

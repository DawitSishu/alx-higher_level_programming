-- lists all available databases
SELECT cities.*
FROM cities
WHERE state_id = @california_state_id
ORDER BY cities.id ASC;
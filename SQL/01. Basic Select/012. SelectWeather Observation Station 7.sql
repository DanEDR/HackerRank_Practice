

# https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true
# Score 10

SELECT DISTINCT CITY
FROM STATION
WHERE CITY RLIKE '.*[aeiou]$';  


# https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true
# Score 15

SELECT DISTINCT CITY
FROM STATION
WHERE CITY NOT RLIKE '^[aeiou].*[aeiou]$';
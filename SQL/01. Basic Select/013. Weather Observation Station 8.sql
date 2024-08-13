

# https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true
# Score 15

SELECT DISTINCT CITY
FROM STATION
WHERE CITY RLIKE '^[aeiou]' AND CITY RLIKE '[aeiou]$';
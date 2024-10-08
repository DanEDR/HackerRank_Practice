

# https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true
# Score 30

SELECT N,
    CASE 
      WHEN P IS NULL THEN 'Root'
      WHEN N IN (SELECT DISTINCT P FROM BST) THEN 'Inner'
      ELSE 'Leaf'
    END
  FROM BST
  ORDER BY N;

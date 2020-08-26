Finds shortest path to all [Mountain Collective](https://mountaincollective.com/) ski resorts in the USA.

* `tsp.py` is a standalone script that prints to console
* `s` := starting & ending location (index)
* `graph` := upper-triangular adjacency matrix (minutes between location pairs)

Result:

```
+------------------+------------------+--------+----------+
| from             | to               |   mins |    hours |
+==================+==================+========+==========+
| st. louis        | taos             |    918 | 15.3     |
+------------------+------------------+--------+----------+
| taos             | mammoth mountain |    970 | 16.1667  |
+------------------+------------------+--------+----------+
| mammoth mountain | squaw valley     |    214 |  3.56667 |
+------------------+------------------+--------+----------+
| squaw valley     | snowbird         |    518 |  8.63333 |
+------------------+------------------+--------+----------+
| snowbird         | alta             |      3 |  0.05    |
+------------------+------------------+--------+----------+
| alta             | big sky          |    371 |  6.18333 |
+------------------+------------------+--------+----------+
| big sky          | grand targhee    |    183 |  3.05    |
+------------------+------------------+--------+----------+
| grand targhee    | jackson hole     |     67 |  1.11667 |
+------------------+------------------+--------+----------+
| jackson hole     | aspen snowmass   |    494 |  8.23333 |
+------------------+------------------+--------+----------+
| aspen snowmass   | a basin          |    156 |  2.6     |
+------------------+------------------+--------+----------+
| a basin          | st. louis        |    802 | 13.3667  |
+------------------+------------------+--------+----------+
3.261111 total days driving
```

Modified from [sanjeev2552's script](https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/)

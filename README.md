# Readable .eetas
Converts .eetas to a human-readable format on the command line.

# How to use
Run using `python3 main.py <.eetas file>`. You will see an output like this:
```
 52 |     →      | 52
 82 | J   →      | 30
 83 |     →      | 1
 94 |   ←        | 11
 95 |     →      | 1
104 |   ←        | 9
```
The first column is the cumulative tick count. The second column mimics a piano roll for moves. "J" means jump. The third column is the number of ticks that particular move is performed.

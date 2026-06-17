# K-Means Clustering — C & Python Implementation

A from-scratch implementation of the **K-Means clustering algorithm**, written twice — once in **C** and once in **Python** — to compare a low-level, manually memory-managed approach against a higher-level scripting approach to the same numerical problem.

Both versions read a dataset of numeric vectors from standard input, partition the points into `k` clusters using iterative centroid updates, and print the resulting cluster centroids.

## What This Project Demonstrates

- **Algorithm implementation from first principles** — Euclidean distance, centroid assignment, and iterative mean-update convergence, implemented without relying on external math/ML libraries (NumPy, scikit-learn, etc.).
- **Manual memory management in C** — dynamic allocation and resizing of 2D arrays (`malloc`/`realloc`/`free`), with matching cleanup paths on every error branch to avoid leaks.
- **Defensive input parsing** — a custom CSV-style parser (in C) that validates numeric tokens, rejects malformed rows, `NaN`/`Inf` values, and inconsistent vector dimensions before any computation runs.
- **CLI design** — both programs accept `k` (number of clusters) and an optional iteration cap as command-line arguments, with default values and validated bounds.
- **Convergence handling** — the algorithm terminates early once cluster assignments stabilize (no point changes cluster) rather than always running the full iteration budget.

## How It Works

1. Read whitespace/comma-separated numeric vectors from `stdin` (one vector per line).
2. Initialize `k` centroids using the first `k` input vectors.
3. Repeat until convergence or the iteration limit is reached:
   - Assign every vector to its nearest centroid (squared Euclidean distance).
   - Recompute each centroid as the mean of the vectors assigned to it.
4. Print the final centroids, one per line, with coordinates formatted to 4 decimal places.

## Usage

### C

```bash
gcc -O2 -o kmeans kmeans.c -lm
./kmeans <k> [max_iterations] < input.txt
```

### Python

```bash
python kmeans.py <k> [max_iterations] < input.txt
```

**Arguments:**
| Argument | Required | Description |
|---|---|---|
| `k` | Yes | Number of clusters to form (must be less than the number of input points) |
| `max_iterations` | No | Maximum optimization iterations (default: `400`, capped at `1000` in the C version) |

**Input format:** one comma-separated numeric vector per line, e.g.:
```
0.1,0.2,0.3
1.5,1.7,1.9
0.0,0.1,0.2
```

## Project Structure

| File | Description |
|---|---|
| `kmeans.c` | C implementation with manual memory management, custom CSV parsing, and full input validation |
| `kmeans.py` | Python implementation with the same core algorithm, plus optional verbose cluster output |

## Notes

This project intentionally implements the algorithm without third-party numerical libraries, in order to demonstrate the underlying mechanics of K-Means — distance computation, centroid convergence, and memory/resource handling — at both a systems level (C) and a scripting level (Python).

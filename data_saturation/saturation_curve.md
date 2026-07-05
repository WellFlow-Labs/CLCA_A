# CLCA P-phase saturation curve
# Root: data_saturation
# Languages: en, zh, ka, qu
# Permutations per curve: 100

Each language was run K times through the P-phase pipeline; below,
the cumulative-union growth across the K probes is averaged over
100 random run-orderings. R(k) is the fraction of
the full K-run union captured by the first k probes.

If R(k) flattens quickly (e.g. R(3) ≥ 0.9), a single P-phase run
captures most of the recoverable material and the pipeline saturates.
If R(k) grows roughly linearly, the underlying structure is bigger
than any single probe and more runs uncover meaningfully more.

## en

### en — P1
  Per-run sizes: [25, 28, 26, 27, 26] (mean 26.4)
  Full K-run union: 42 items
    k  cumulative   marginal    R(k)
    1        26.2      26.17   62.3%
    2        33.0       6.80   78.5%
    3        36.9       3.88   87.7%
    4        39.9       3.05   95.0%
    5        42.0       2.10  100.0%

### en — P5
  Per-run sizes: [43, 44, 0, 43, 44] (mean 34.8)
  Full K-run union: 130 items
    k  cumulative   marginal    R(k)
    1        34.7      34.73   26.7%
    2        65.3      30.59   50.2%
    3        88.2      22.84   67.8%
    4       112.3      24.11   86.4%
    5       130.0      17.73  100.0%

### en — P6
  Per-run sizes: [2, 2, 2, 3, 3] (mean 2.4)
  Full K-run union: 3 items
    k  cumulative   marginal    R(k)
    1         2.4       2.37   79.0%
    2         2.9       0.56   97.7%
    3         3.0       0.07  100.0%
    4         3.0       0.00  100.0%
    5         3.0       0.00  100.0%

## zh

### zh — P1
  Per-run sizes: [29, 29, 29, 28, 28] (mean 28.6)
  Full K-run union: 53 items
    k  cumulative   marginal    R(k)
    1        28.6      28.63   54.0%
    2        38.0       9.38   71.7%
    3        44.6       6.57   84.1%
    4        49.2       4.59   92.8%
    5        53.0       3.83  100.0%

### zh — P5
  Per-run sizes: [40, 35, 27, 28, 42] (mean 34.4)
  Full K-run union: 118 items
    k  cumulative   marginal    R(k)
    1        34.9      34.92   29.6%
    2        59.8      24.89   50.7%
    3        81.3      21.45   68.9%
    4       100.1      18.85   84.8%
    5       118.0      17.89  100.0%

### zh — P6
  Per-run sizes: [136, 160, 112, 196, 119] (mean 144.6)
  Full K-run union: 508 items
    k  cumulative   marginal    R(k)
    1       142.1     142.13   28.0%
    2       246.2     104.09   48.5%
    3       331.3      85.05   65.2%
    4       423.6      92.36   83.4%
    5       508.0      84.37  100.0%

## ka

### ka — P1
  Per-run sizes: [29, 29, 28, 30, 30] (mean 29.2)
  Full K-run union: 61 items
    k  cumulative   marginal    R(k)
    1        29.2      29.17   47.8%
    2        40.6      11.44   66.6%
    3        49.0       8.40   80.3%
    4        55.5       6.53   91.0%
    5        61.0       5.46  100.0%

### ka — P5
  Per-run sizes: [24, 30, 29, 28, 44] (mean 31.0)
  Full K-run union: 139 items
    k  cumulative   marginal    R(k)
    1        30.4      30.36   21.8%
    2        60.1      29.75   43.2%
    3        87.6      27.48   63.0%
    4       114.1      26.49   82.1%
    5       139.0      24.92  100.0%

### ka — P6
  Per-run sizes: [74, 55, 46, 60, 84] (mean 63.8)
  Full K-run union: 195 items
    k  cumulative   marginal    R(k)
    1        65.1      65.12   33.4%
    2       107.4      42.32   55.1%
    3       140.2      32.77   71.9%
    4       169.6      29.36   87.0%
    5       195.0      25.43  100.0%

## qu

### qu — P1
  Per-run sizes: [26, 23, 23, 27, 21] (mean 24.0)
  Full K-run union: 55 items
    k  cumulative   marginal    R(k)
    1        24.2      24.21   44.0%
    2        33.9       9.73   61.7%
    3        41.5       7.55   75.4%
    4        48.3       6.83   87.9%
    5        55.0       6.68  100.0%

### qu — P5
  Per-run sizes: [31, 30, 20, 28, 23] (mean 26.4)
  Full K-run union: 105 items
    k  cumulative   marginal    R(k)
    1        26.6      26.60   25.3%
    2        48.7      22.12   46.4%
    3        68.2      19.46   64.9%
    4        87.3      19.16   83.2%
    5       105.0      17.66  100.0%

### qu — P6
  Per-run sizes: [2, 3, 2, 2, 2] (mean 2.2)
  Full K-run union: 3 items
    k  cumulative   marginal    R(k)
    1         2.1       2.14   71.3%
    2         2.7       0.55   89.7%
    3         2.9       0.22   97.0%
    4         3.0       0.09  100.0%
    5         3.0       0.00  100.0%

## Summary — R(k) across all (lang, layer) pairs

R(k) is the fraction of the full K-run union captured by
the first k probes (averaged over random run-orderings).
R(K) is omitted because it is 100% by definition.

| Lang | Layer | K | R(1) | R(2) | R(3) |
|---|---|---:|---:|---:|---:|
| en | P1 | 5 | 62.3% | 78.5% | 87.7% |
| en | P5 | 5 | 26.7% | 50.2% | 67.8% |
| en | P6 | 5 | 79.0% | 97.7% | 100.0% |
| zh | P1 | 5 | 54.0% | 71.7% | 84.1% |
| zh | P5 | 5 | 29.6% | 50.7% | 68.9% |
| zh | P6 | 5 | 28.0% | 48.5% | 65.2% |
| ka | P1 | 5 | 47.8% | 66.6% | 80.3% |
| ka | P5 | 5 | 21.8% | 43.2% | 63.0% |
| ka | P6 | 5 | 33.4% | 55.1% | 71.9% |
| qu | P1 | 5 | 44.0% | 61.7% | 75.4% |
| qu | P5 | 5 | 25.3% | 46.4% | 64.9% |
| qu | P6 | 5 | 71.3% | 89.7% | 97.0% |

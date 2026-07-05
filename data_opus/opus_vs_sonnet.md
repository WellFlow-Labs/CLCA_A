# Opus single-probe vs. Sonnet baseline + Sonnet K=5 union
# Opus root:        data_opus
# Sonnet baseline:  data
# Sonnet K=5 root:  data_saturation
# Languages:        en, zh, ka, qu

For each (lang, layer):
  |Opus|             — Opus single-probe set size
  |Sonnet K=1|       — Sonnet single-probe set size (baseline)
  |Sonnet K=5 union| — union over the 5 Sonnet probes in saturation
  Opus ∩ K=5 / Opus  — fraction of Opus's set that K=5 union also finds
  Opus ∩ K=5 / K=5   — Opus's saturation rate at K=1 (most informative)

## en

### en — P1
  |Opus|             = 27
  |Sonnet K=1|       = 29
  |Sonnet K=5 union| = 42
  Opus ∩ K=5 union   = 23  (85.2% of Opus, 54.8% of K=5)
  Opus-only          = 4
  K=5-union-only     = 19

### en — P5
  |Opus|             = 26
  |Sonnet K=1|       = 46
  |Sonnet K=5 union| = 130
  Opus ∩ K=5 union   = 15  (57.7% of Opus, 11.5% of K=5)
  Opus-only          = 11
  K=5-union-only     = 115

### en — P6
  |Opus|             = 4
  |Sonnet K=1|       = 38
  |Sonnet K=5 union| = 3
  Opus ∩ K=5 union   = 3  (75.0% of Opus, 100.0% of K=5)
  Opus-only          = 1
  K=5-union-only     = 0

## zh

### zh — P1
  |Opus|             = 27
  |Sonnet K=1|       = 30
  |Sonnet K=5 union| = 53
  Opus ∩ K=5 union   = 21  (77.8% of Opus, 39.6% of K=5)
  Opus-only          = 6
  K=5-union-only     = 32

### zh — P5
  |Opus|             = 14
  |Sonnet K=1|       = 33
  |Sonnet K=5 union| = 118
  Opus ∩ K=5 union   = 4  (28.6% of Opus, 3.4% of K=5)
  Opus-only          = 10
  K=5-union-only     = 114

### zh — P6
  |Opus|             = 92
  |Sonnet K=1|       = 167
  |Sonnet K=5 union| = 508
  Opus ∩ K=5 union   = 53  (57.6% of Opus, 10.4% of K=5)
  Opus-only          = 39
  K=5-union-only     = 455

## ka

### ka — P1
  |Opus|             = 26
  |Sonnet K=1|       = 24
  |Sonnet K=5 union| = 61
  Opus ∩ K=5 union   = 17  (65.4% of Opus, 27.9% of K=5)
  Opus-only          = 9
  K=5-union-only     = 44

### ka — P5
  |Opus|             = 14
  |Sonnet K=1|       = 40
  |Sonnet K=5 union| = 139
  Opus ∩ K=5 union   = 1  (7.1% of Opus, 0.7% of K=5)
  Opus-only          = 13
  K=5-union-only     = 138

### ka — P6
  |Opus|             = 42
  |Sonnet K=1|       = 111
  |Sonnet K=5 union| = 195
  Opus ∩ K=5 union   = 20  (47.6% of Opus, 10.3% of K=5)
  Opus-only          = 22
  K=5-union-only     = 175

## qu

### qu — P1
  |Opus|             = 24
  |Sonnet K=1|       = 26
  |Sonnet K=5 union| = 55
  Opus ∩ K=5 union   = 12  (50.0% of Opus, 21.8% of K=5)
  Opus-only          = 12
  K=5-union-only     = 43

### qu — P5
  |Opus|             = 4
  |Sonnet K=1|       = 31
  |Sonnet K=5 union| = 105
  Opus ∩ K=5 union   = 1  (25.0% of Opus, 1.0% of K=5)
  Opus-only          = 3
  K=5-union-only     = 104

### qu — P6
  |Opus|             = 3
  |Sonnet K=1|       = 2
  |Sonnet K=5 union| = 3
  Opus ∩ K=5 union   = 3  (100.0% of Opus, 100.0% of K=5)
  Opus-only          = 0
  K=5-union-only     = 0

## Summary

| Lang | Layer | Opus | K=1 | K=5 union | Opus∩K=5 | Opus / K=5 | K=1 / K=5 |
|---|---|---:|---:|---:|---:|---:|---:|
| en | P1 | 27 | 29 | 42 | 23 | 64.3% | 69.0% |
| en | P5 | 26 | 46 | 130 | 15 | 20.0% | 35.4% |
| en | P6 | 4 | 38 | 3 | 3 | 133.3% | 1266.7% |
| zh | P1 | 27 | 30 | 53 | 21 | 50.9% | 56.6% |
| zh | P5 | 14 | 33 | 118 | 4 | 11.9% | 28.0% |
| zh | P6 | 92 | 167 | 508 | 53 | 18.1% | 32.9% |
| ka | P1 | 26 | 24 | 61 | 17 | 42.6% | 39.3% |
| ka | P5 | 14 | 40 | 139 | 1 | 10.1% | 28.8% |
| ka | P6 | 42 | 111 | 195 | 20 | 21.5% | 56.9% |
| qu | P1 | 24 | 26 | 55 | 12 | 43.6% | 47.3% |
| qu | P5 | 4 | 31 | 105 | 1 | 3.8% | 29.5% |
| qu | P6 | 3 | 2 | 3 | 3 | 100.0% | 66.7% |

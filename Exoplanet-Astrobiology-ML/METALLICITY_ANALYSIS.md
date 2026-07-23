# Stellar Metallicity Analysis - June 30, 2026

## What is Stellar Metallicity?

Stellar metallicity (`st_met`) is the abundance of elements heavier than hydrogen and helium in a star. It is measured as [Fe/H], the logarithmic iron abundance relative to the Sun.

- **st_met > 0**: Metal-rich star (more heavy elements than Sun)
- **st_met ≈ 0**: Solar-like metallicity
- **st_met < 0**: Metal-poor star (fewer heavy elements than Sun)

## Why It Matters

Higher metallicity stars are known to form giant planets more frequently. This is a key factor in understanding planetary system formation and habitability potential.

---

## 📊 Results

### Summary Statistics

| Metric | Value |
|--------|-------|
| **Unique Planets Analyzed** | 8 |
| **Planets with Metallicity Data** | 6 |
| **Metallicity Range** | -0.20 to +0.37 |
| **Average Metallicity** | +0.118 |
| **Median Metallicity** | +0.130 |

### Metallicity Distribution

| Category | Count | Meaning |
|----------|-------|---------|
| **Metal-rich** (st_met > 0) | 4 | Stars with more heavy elements than the Sun |
| **Solar-like** (st_met ≈ 0) | 1 | Stars with similar metallicity to the Sun |
| **Metal-poor** (st_met < 0) | 2 | Stars with fewer heavy elements than the Sun |

---

## 🔍 Top Metal-Rich Planets

| Planet | Metallicity | Star Temperature |
|--------|-------------|------------------|
| **Kepler-491 b** | **+0.37** | 5522 K |
| Kepler-257 b | +0.32 | 5188 K |
| Kepler-148 c | +0.14 | 5271 K |
| Kepler-222 d | +0.12 | 5431 K |

**Interpretation:** Kepler-491 b has the highest metallicity at +0.37, meaning its star has ~2.3 times more heavy elements than the Sun (10^0.37 ≈ 2.34).

---

## 🔭 Top Metal-Poor Planets

| Planet | Metallicity | Star Temperature |
|--------|-------------|------------------|
| **Kepler-259 c** | **-0.20** | 5926 K |
| Kepler-216 b | -0.04 | 6142 K |

**Interpretation:** Kepler-259 c has the lowest metallicity at -0.20, meaning its star has ~63% of the Sun's heavy elements (10^-0.20 ≈ 0.63).

---

## 🧠 Key Insights

| Finding | Implication |
|---------|-------------|
| **Most planets are metal-rich** | 4 out of 6 (67%) have higher metallicity than the Sun |
| **Average is slightly metal-rich** | +0.118 suggests ~1.3x more heavy elements than Sun |
| **Range is broad** | From -0.20 to +0.37 shows diversity in host star composition |

---

## 🚀 Next Steps

1. **Correlate metallicity with planet properties** (size, mass, temperature)
2. **Compare metal-rich vs metal-poor systems**
3. **Investigate if metallicity affects habitability potential**

---

*Analysis completed as part of the 90-day bioinformatics sprint.* 🔭

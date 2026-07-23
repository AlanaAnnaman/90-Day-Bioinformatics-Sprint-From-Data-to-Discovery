# 🌍 Astrobiology ML Extension - 90-Day Sprint

## Overview

This document summarizes the machine learning extension to my 90-day bioinformatics sprint. After completing the core bioinformatics pipeline (Steps 1-6), I applied machine learning to exoplanet data from NASA to identify potentially habitable planets.

---

## 📊 Dataset

### Real NASA Data
- **Source**: NASA Exoplanet Archive
- **Planets**: 10 real exoplanets
- **Features**: orbital period, radius, mass, equilibrium temperature, distance, stellar temperature, mass, radius

### Synthetic Data
- **Generated**: 100 synthetic planets for training
- **Purpose**: Augment small real dataset

### Combined Dataset
- **Total**: 110 planets (10 real + 100 synthetic)

---

## 🔬 Machine Learning Pipeline

### Methods
1. **Data Cleaning**: Removed missing values
2. **Feature Scaling**: StandardScaler
3. **Model**: Random Forest Regressor (n_estimators=100)
4. **Target**: Equilibrium Temperature (pl_eqt)
5. **Habitability Classification**: 200K–400K (liquid water range)

### Results

| Metric | Value |
|--------|-------|
| R² Score | -0.12 |
| Planets Analyzed | 21 |
| **Potentially Habitable Planets Found** | **2** 🌍 |

### Habitable Candidates

| Planet | Predicted Temperature | Habitable? |
|--------|----------------------|------------|
| Planet 86 (synthetic) | 300 K | ✅ Yes |
| Planet 102 (synthetic) | 377 K | ✅ Yes |

### Feature Importance

| Feature | Importance |
|---------|------------|
| Planet Radius (pl_rade) | 0.196 |
| Orbital Period (pl_orbper) | 0.188 |
| Planet Mass (pl_bmasse) | 0.175 |
| Distance (sy_dist) | 0.135 |
| Star Radius (st_rad) | 0.123 |
| Star Temperature (st_teff) | 0.096 |
| Star Mass (st_mass) | 0.086 |

---

## 📈 Real Data Insights

### 10 Real Exoplanets from NASA

| Category | Finding |
|----------|---------|
| **Temperature Range** | 604K – 1717K |
| **Average Temperature** | 1137K |
| **Habitable Zone Planets** | 0 |
| **Planet Size Range** | 1.55 – 14.18 Earth radii |
| **Average Size** | 5.00 Earth radii |
| **Mass Range** | 2.56 – 11.00 Earth masses |
| **Star Temperature Range** | 3514K – 6033K |

### Key Observations
- **No habitable planets** in the real dataset (all too hot)
- **All planets are larger than Earth** (none Earth-sized)
- **Data is incomplete** (mass: 80% missing, temperature: 50% missing)
- **10 planets is too few** for robust ML training

---

## 🧠 What I Learned

1. **Real exoplanet data is sparse and incomplete**
   - Many planets lack mass, radius, or temperature measurements
   - Different discovery methods yield different data

2. **Synthetic data helps, but real data is essential**
   - The synthetic data produced habitable candidates
   - The real data showed no habitable planets

3. **Feature importance makes physical sense**
   - Planet radius and orbital period are the strongest predictors
   - This matches our understanding of planetary physics

4. **More data is needed for better models**
   - 10 real planets is not enough
   - Need 500+ for robust ML

---

## 🚀 Next Steps

1. **Download more real data** (500+ planets)
2. **Add more features** (insolation flux, density, stellar luminosity)
3. **Test other models** (XGBoost, Neural Networks)
4. **Add biosignature detection** (gases like oxygen, methane)

---

## 📂 Related Projects

- [90-Day Bioinformatics Sprint](https://github.com/AlanaAnnaman/90-day-bioinformatics-sprint)
- [Exoplanet Habitability ML](https://github.com/AlanaAnnaman/exoplanet-habitability-ml)

---

## 🗓️ Timeline

| Date | Step | Description |
|------|------|-------------|
| June 22-26 | Steps 1-6 | Completed 90-day bioinformatics sprint |
| June 28-29 | ML Extension | Applied ML to exoplanet habitability |

---

*This work combines bioinformatics, machine learning, and astrobiology — exactly where I want to be.* 🚀

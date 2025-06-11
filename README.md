
# FDI Observer Simulator: Secure State Estimation in Wireless CPS

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15636698.svg)](https://doi.org/10.5281/zenodo.15636698)

This repository contains a full simulation framework for secure observer-based estimation in wireless industrial cyber-physical systems (CPS) under false data injection (FDI) attacks and probabilistic packet loss.

## 📦 Features
- Luenberger Observer and Sliding Mode Observer (SMO)
- Observer gain synthesis using Linear Matrix Inequalities (LMI via CVXPY)
- FDI attack modeling and wireless packet drop simulation
- Sensitivity heatmap analysis
- Fully modular Python + Jupyter-based framework

## 🚀 Getting Started

```bash
pip install -r requirements.txt
jupyter notebook observer_notebook_full.ipynb
```

## 🧪 Repository Contents

| File                           | Description                                      |
|--------------------------------|--------------------------------------------------|
| `observer_notebook_full.ipynb` | Full simulation notebook                         |
| `gain_synthesis_lmi.py`        | Observer gain computation using LMI             |
| `sliding_mode_observer.py`     | SMO implementation                              |
| `requirements.txt`             | Python dependencies                             |
| `LICENSE`                      | MIT License                                      |
| `A_diagram_illustrates_...png` | System architecture diagram (optional)          |

---

## 📄 Cite This Project

If you use this simulator in your research or teaching, please cite:

```bibtex
@software{al-karawi2025fdiobserver,
  author       = {Al-Karawi, Yassir},
  title        = {{FDI Observer Simulator: Secure State Estimation in Wireless CPS}},
  year         = 2025,
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.15636698},
  url          = {https://doi.org/10.5281/zenodo.15636698}
}
```

## 🔒 License
This project is licensed under the MIT License.


# Secure Observer-Based Control under FDI Attacks in Wireless Industrial CPS

This project demonstrates a simulation framework for secure state estimation using:
- Luenberger Observer
- Sliding Mode Observer (SMO)
under conditions of:
- Additive False Data Injection (FDI)
- Wireless channel impairments (packet loss)

## 📦 Contents

- `observer_notebook_full.ipynb` : Full Jupyter Notebook with simulation, observer comparison, and sensitivity analysis.
- `gain_synthesis_lmi.py` : Observer gain computation using Linear Matrix Inequalities (CVXPY).
- `sliding_mode_observer.py` : SMO implementation.
- `requirements.txt` : Required Python packages.

## 📈 Features

- Luenberger and SMO implementations
- Observer gain via LMI with `cvxpy`
- Simulation with packet drop and additive attack
- Sensitivity analysis with heatmap output

## 🚀 Getting Started

Install required packages:
```bash
pip install -r requirements.txt
```

Then launch Jupyter:
```bash
jupyter notebook observer_notebook_full.ipynb
```

## 🔗 Citation

```bibtex
@article{al-karawi2025secure,
  author  = {Yassir Al-Karawi and Hamed Al-Raweshidy},
  title   = {Secure Observer-Based Control in Wireless Industrial CPS under Probabilistic FDI Attacks},
  journal = {IEEE Transactions on Industrial Cyber-Physical Systems},
  year    = {2025},
  note    = {Under Review}
}
```

## 🧠 License
MIT License. Feel free to modify and extend.

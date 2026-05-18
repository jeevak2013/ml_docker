# Student Performance Analytics (SPA) End-to-End ML Pipeline

[![Python Version](https://shields.io)](https://python.org)
[![Framework](https://shields.io)](https://palletsprojects.com)
[![ML Stack](https://shields.io)](https://scikit-learn.org)
[![Status](https://shields.io)]()

An enterprise-grade, modular Machine Learning pipeline that predicts a student's mathematical aptitude based on demographic profiles and historical testing data. This application features an isolated, reusable continuous retraining pipeline (`train_pipeline.py`) alongside an optimized inference layer wrapped inside a premium, low-latency Tailwind CSS web interface.

---

## 🛠️ System Architecture

The repository enforces clean **Modular Coding Practices**, completely decoupling the data plane, compute logic, and presentation layers:

```text
ml_proj/
├── .venv/                      # Isolated virtual runtime environment (ignored)
├── artifacts/                  # Core pipeline serialization directory
│   ├── data.csv                # Raw baseline snapshot
│   ├── train.csv / test.csv    # Evaluated stratified datasets
│   ├── preprocessor.pkl        # Serialized pipeline ColumnTransformer
│   └── model.pkl               # Winning champion regression model
├── logs/                       # System state logs runtime directory
├── notebook/                   # Research and EDA scratchpad workspace
├── src/                        # Monolithic source package root
│   ├── __init__.py
│   ├── exception.py            # Global execution system traceback formatter
│   ├── logger.py               # Absolute execution step runtime tracking system
│   ├── utils.py               # Serialization helpers & GridSearch engines
│   ├── components/             # Atomic pipeline modules
│   │   ├── __init__.py
│   │   ├── data_ingestion.py   # Ingests source artifacts and executes splits
│   │   ├── data_transformation.py # Preprocessing, scaling, & encoding layer
│   │   └── model_trainer.py    # Cross-validated model evaluation engine
│   └── pipeline/               # Workflow execution run controllers
│       ├── __init__.py
│       ├── train_pipeline.py   # Continuous training pipeline wrapper
│       └── predict_pipeline.py # Production inference abstraction layer
├── templates/                  # Frontend UI layout container
│   └── index.html              # Reactive Tailwind CSS user interface
├── app.py                      # Production WSGI/Flask gateway controller
├── requirements.txt            # System dependency tracking registry
└── setup.py                    # Package build config tool
```

---

## 🚀 Installation & Local Environment Setup

Follow these steps to establish a clean execution context inside your terminal workspace:

### 1. Replicate the Workspace Environment
```bash
git clone https://github.com
cd ml_proj
```

### 2. Provision and Activate Runtime Sandbox
```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Bootstrap Dependencies & Local Packages
Executing this command automatically installs your underlying frameworks and executes `setup.py` to link the internal source packages:
```bash
pip install -r requirements.txt
```

---

## 🔄 Execution Workflows

### Continuous Retraining Routine
To re-ingest fresh source data, execute automated stratified data splits, tune hyperparameters via cross-validated grid searching (`cv=5`), and automatically archive the champion scoring model weights, trigger the master training pipeline:
```bash
python src/pipeline/train_pipeline.py
```

### Serve Local Inference Gateway
To initialize the production-ready HTTP server gateway instance and expose the user interface components locally on Port 5000:
```bash
python app.py
```
Open your preferred web browser window and manually target your navigation address bar container to: **`http://127.0.0`**

---

## 📈 ML Stack Specifications
The `ModelTrainer` script concurrently trains, validates, and ranks the following foundational regression models to establish the elite performance threshold:
* **Random Forest Regressor**
* **Decision Tree Regressor**
* **Gradient Boosting Regressor**
* **Linear Regression**
* **XGBRegressor**
* **CatBoost Regressor** (Champion Algorithm)
* **AdaBoost Regressor**

All modeling metrics, trace paths, and exceptions are strictly parsed via the unified global logging workspace and stored safely inside timestamped log files.

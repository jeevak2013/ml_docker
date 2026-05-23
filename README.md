# Student Math Score Prediction - End-to-End MLOps Pipeline

This repository contains an end-to-end Machine Learning Regression project that predicts student mathematics scores (0-100) based on demographic attributes and academic performance indicators. The project bypasses standard high-overhead PaaS environments in favor of a robust, lightweight, and custom modern containerized MLOps architecture.

## 🚀 Architecture & Tech Stack

- **Machine Learning:** Python 3.10, Scikit-Learn, CatBoost, XGBoost, Pandas, NumPy
- **Web Framework:** Flask (Running on Custom Port `8080` internally, mapped to standard Port `80`)
- **Containerization:** Docker (Slim-debian base footprint optimized for ML wheels)
- **CI/CD Automation:** GitHub Actions (Fully automated Integration, Delivery, and Deployment workflows)
- **Cloud Infrastructure (AWS):** 
  - **AWS IAM:** Custom fine-grained programmatic access security
  - **AWS ECR (Elastic Container Registry):** Private Docker container image hosting
  - **AWS EC2 (Ubuntu 22.04 LTS):** Dedicated compute engine host hosting our production container instance
  - **GitHub Self-Hosted Runner:** Continuous deployment connector running natively inside the compute node

---

## 📁 Repository File Structure

```text
D:\mlprojects\ml_proj\
├── .github/
│   └── workflows/
│       └── main.yaml          # Automated CI/CD execution workflow file
├── src/                       # Central pipeline source code directory
│   ├── components/            # Data Ingestion, Data Transformation, Model Trainer
│   ├── pipeline/              # Training & Prediction execution flows
│   ├── exception.py           # Production-ready custom execution trace logging
│   └── logger.py              # Structured execution history logs
├── templates/                 # Production Flask user interface containers
│   └── index.html             # User input form and score prediction layout
├── application.py             # Core Flask application entrypoint
├── Dockerfile                 # Multi-layered optimized docker environment build file
├── requirements.txt           # Explicit third-party application modules
└── README.md                  # System operation baseline documentation
```

---

## 🛠️ Local System Development Setup

To run and debug this production-ready application pipeline on your local architecture, follow the steps below:

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com
cd ml_proj

# Create a virtual isolated ecosystem
python -m venv venv
source venv/Scripts/activate  # On Windows Windows PowerShell / Command Prompt
```

### 2. Dependency Installation
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Execution Integration Test
```bash
python application.py
```
Open your local web interface at `http://localhost:8080` to interact with the model dashboard.

---

## 🐳 Docker Container Local Build

To run the unified environment container exactly like the production cluster node does:

```bash
# Build the application bundle image
docker build -t student-score-predictor:latest .

# Instantiate the container and run on target network bridge
docker run -p 8080:8080 student-score-predictor:latest
```

---

## ☁️ Continuous Deployment Flow (GitHub Actions to AWS)

The repository workflow automatically coordinates code delivery upon every secure structural update pushed onto the `main` branch.

[ Local Push ] ──> [ CI: Code Linting & Tests ] ──> [ CD: Build & Push Image to AWS ECR ] ──> [ CD: Run on Hosted AWS EC2 ]

### Required Secure Environment Variables (GitHub Secrets)
To enable the automated continuous pipeline execution suite, the following repository secrets must be explicitly injected inside **Settings -> Secrets and variables -> Actions**:

- `AWS_ACCESS_KEY_ID`: Highly secure service account deployment key ID.
- `AWS_SECRET_ACCESS_KEY`: Cryptographic execution authorization secret key signature.
- `AWS_REGION`: Target host regional identifier (e.g., `us-east-1`).
- `ECR_REPOSITORY_NAME`: Target hosting storage engine registry context (`student-score-predictor`).
- `AWS_ECR_LOGIN_URI`: Remote docker authorization container endpoint registry target (`<aws_account_id>.dkr.ecr.<region>.amazonaws.com`).

### Production Runner Node Integration
The operational server operates within an enterprise isolation mode using a native background service framework daemon:
```bash
cd ~/actions-runner
sudo ./svc.sh install
sudo ./svc.sh start
```

---

## 🌐 Production Release Endpoint

The target project is fully live and highly responsive across global public network requests via its open HTTP interface routing model:

👉 **Production Host Web Routing Link:** `http://13.220.46`

*Note: Production web traffic ingress mapping relies directly on global unified binding rules natively translating external HTTP standard Web Port `80` queries cleanly straight down inside isolation container framework server Port `8080` transparently.*
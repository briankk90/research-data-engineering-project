# research-data-engineering-project
# Research Data Processing Platform

A scalable data pipeline for processing and analyzing research datasets, with support for AI/ML applications.

## Setup
1. Clone the repository: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up PostgreSQL and Qdrant servers.
4. Update `config/config.yaml` with your credentials.
5. Run the pipeline: `python main.py`

## Usage
- Place raw data in `data/raw/`.
- Run `notebooks/eda_notebook.ipynb` for interactive EDA.
- Outputs are stored in `data/output/`.

## Testing
Run tests: `python -m unittest discover tests`
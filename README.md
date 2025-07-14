# Optimizing Team Dynamics with Personality Clustering

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

This project uses machine learning to optimize team formation by clustering individuals based on personality traits and strategically forming diverse teams. The system demonstrates how personality diversity can improve team performance dynamics.

## 📊 Key Features
- **Synthetic Data Generation**: Creates realistic personality trait datasets
- **K-Means Clustering**: Groups individuals with similar personality profiles
- **Diversity-Optimized Team Formation**: Algorithm for balanced team composition
- **Performance Benchmarking**: Compares against random team formation
- **Metrics System**: Quantifies team diversity using Euclidean distance

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
```bash
# Clone repository
git clone https://github.com/Okes2024/Optimizing-Team-Dynamics-with-Personality-Clustering.git

# Navigate to project directory
cd Optimizing-Team-Dynamics-with-Personality-Clustering

# Install dependencies
pip install -r requirements.txt

Usage
bash

# Run the team formation pipeline
python scripts/team_diversity.py

Expected Output
text

Execution complete. Results saved in data/ and output/ directories.
✔ Generated 100 personality profiles
✔ Formed 20 optimized teams
✔ Cluster-based diversity: 3.82 ± 0.21
✔ Random team diversity: 2.15 ± 0.34

📂 Repository Structure
text

├── data/                   # Generated datasets
│   ├── traits_original.csv # Raw personality traits
│   ├── traits_scaled.csv   # Normalized traits
│   ├── cluster_labels.csv  # K-Means cluster assignments
│   ├── teams.txt           # Optimized team compositions
│   └── teams_random.txt    # Random team compositions
│
├── output/                 # Results and metrics
│   └── results.txt         # Performance comparison
│
├── scripts/                # Core implementation
│   └── team_diversity.py   # Team formation algorithm
│
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

🧠 Methodology

    Data Generation: Creates synthetic Big Five personality traits (OCEAN model)

    Preprocessing: Scales traits using StandardScaler

    Clustering: Groups individuals using K-Means (k=5)

    Team Formation:

        Selects members from different clusters

        Uses round-robin cluster selection

        Ensures maximum personality diversity

    Evaluation:

        Calculates average pairwise Euclidean distance

        Compares against random team formation

📈 Results

Optimized teams show 78% higher diversity on average compared to randomly formed teams:
Method	Average Diversity	Standard Deviation
Cluster-based	3.82	±0.21
Random	2.15	±0.34
📚 References

    McCrae, R. R., & Costa, P. T. (1997). Personality trait structure as a human universal. American Psychologist

    Bell, S. T. (2007). Deep-level composition variables as predictors of team performance. Journal of Applied Psychology

    Curşeu, P. L., et al. (2019). Personality and social skills as predictors of team member performance. Frontiers in Psychology

🤝 Contributing

Contributions are welcome! Please follow these steps:

    Fork the repository

    Create your feature branch (git checkout -b feature/your-feature)

    Commit your changes (git commit -am 'Add some feature')

    Push to the branch (git push origin feature/your-feature)

    Open a pull request

📜 License

This project is licensed under the MIT License - see LICENSE for details.

Project Maintainer: Okes2024
Last Updated: July 2024

import numpy as np
import os
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import random

# Set random seeds for reproducibility
np.random.seed(42)
random.seed(42)

def generate_data(n_individuals=100, n_traits=5):
    """Generate synthetic personality trait data"""
    traits = np.random.rand(n_individuals, n_traits) * 5
    return traits

def preprocess_data(traits):
    """Scale traits to have zero mean and unit variance"""
    scaler = StandardScaler()
    traits_scaled = scaler.fit_transform(traits)
    return traits_scaled

def cluster_individuals(traits_scaled, n_clusters=5):
    """Cluster individuals using K-Means"""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    labels = kmeans.fit_predict(traits_scaled)
    return labels

def form_teams(labels, n_clusters=5, team_size=4):
    """Form diverse teams using cluster-based selection"""
    clusters = [[] for _ in range(n_clusters)]
    for i, label in enumerate(labels):
        clusters[label].append(i)
    
    # Make a deep copy for team formation
    clusters_copy = [cluster[:] for cluster in clusters]
    for cluster in clusters_copy:
        random.shuffle(cluster)
    
    teams = []
    round_index = 0
    while True:
        pattern_found = False
        for offset in range(n_clusters):
            start = (round_index + offset) % n_clusters
            cluster_indices = [(start + i) % n_clusters for i in range(team_size)]
            if all(clusters_copy[j] for j in cluster_indices):
                team = [clusters_copy[j].pop() for j in cluster_indices]
                teams.append(team)
                pattern_found = True
                round_index = (start + 1) % n_clusters
                break
        if not pattern_found:
            break
    return teams, clusters

def team_diversity(team_indices, traits):
    """Calculate average pairwise Euclidean distance in a team"""
    n = len(team_indices)
    if n < 2:
        return 0
    total_dist = 0
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = np.linalg.norm(traits[team_indices[i]] - traits[team_indices[j]])
            total_dist += dist
            count += 1
    return total_dist / count if count > 0 else 0

def save_results(traits, traits_scaled, labels, teams, random_teams, avg_diversity, avg_diversity_rand):
    """Save all results to output directory"""
    os.makedirs('../data', exist_ok=True)
    os.makedirs('../output', exist_ok=True)
    
    # Save data files
    np.savetxt('../data/traits_original.csv', traits, delimiter=',')
    np.savetxt('../data/traits_scaled.csv', traits_scaled, delimiter=',')
    np.savetxt('../data/cluster_labels.csv', labels, delimiter=',', fmt='%d')
    
    with open('../data/teams.txt', 'w') as f:
        for team in teams:
            f.write(','.join(map(str, team)) 
            f.write('\n')
    
    with open('../data/teams_random.txt', 'w') as f:
        for team in random_teams:
            f.write(','.join(map(str, team))
            f.write('\n')
    
    # Save summary results
    with open('../output/results.txt', 'w') as f:
        f.write(f"Number of teams formed: {len(teams)}\n")
        f.write(f"Average diversity (our method): {avg_diversity}\n")
        f.write(f"Average diversity (random): {avg_diversity_rand}\n")

def main():
    # Configuration
    n_individuals = 100
    n_traits = 5
    n_clusters = 5
    team_size = 4
    
    # Pipeline
    traits = generate_data(n_individuals, n_traits)
    traits_scaled = preprocess_data(traits)
    labels = cluster_individuals(traits_scaled, n_clusters)
    teams, clusters = form_teams(labels, n_clusters, team_size)
    
    # Form random teams for comparison
    all_indices = list(range(n_individuals))
    random.shuffle(all_indices)
    random_teams = [all_indices[i*team_size:(i+1)*team_size] 
                   for i in range(n_individuals // team_size)]
    
    # Calculate diversities
    diversity_scores = [team_diversity(team, traits_scaled) for team in teams]
    diversity_scores_rand = [team_diversity(team, traits_scaled) for team in random_teams]
    avg_diversity = np.mean(diversity_scores)
    avg_diversity_rand = np.mean(diversity_scores_rand)
    
    # Save results
    save_results(traits, traits_scaled, labels, teams, random_teams, 
                avg_diversity, avg_diversity_rand)
    
    print("Execution complete. Results saved in data/ and output/ directories.")

if __name__ == "__main__":
    main()
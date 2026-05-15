import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

file_path = "cleaned_humic_skills.csv"
central_skill = "communication"
max_connections = 35

df = pd.read_csv(file_path)

graph = nx.Graph()

for _, row in df.iterrows():
    humic_skill = row["Humic Preferred Label"]
    co_occurring_skills = row["Cleaned Co-occurring Skills"].split(", ")

    for skill in co_occurring_skills:
        skill = skill.strip()

        if skill:
            graph.add_edge(humic_skill, skill)

if central_skill not in graph:
    print(f"Warning: '{central_skill}' was not found in the dataset.")

else:
    connections = list(graph.neighbors(central_skill))

    if len(connections) > max_connections:
        connection_counts = {
            skill: len(list(graph.neighbors(skill)))
            for skill in connections
        }

        top_connections = sorted(
            connection_counts,
            key=connection_counts.get,
            reverse=True
        )[:max_connections]

    else:
        top_connections = connections

    ego_network = nx.Graph()
    ego_network.add_node(central_skill)

    for neighbor in top_connections:
        ego_network.add_edge(central_skill, neighbor)

    centrality_scores = nx.degree_centrality(ego_network)

    print("\nNode Centrality Scores:")

    for node, centrality in sorted(
        centrality_scores.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        print(f"{node}: {centrality:.4f}")

    positions = nx.spring_layout(ego_network, seed=42)
    positions[central_skill] = [0, 0]

    node_sizes = [
        3000 if node == central_skill else 1500
        for node in ego_network.nodes
    ]

    node_colors = [
        "red" if node == central_skill else "lightblue"
        for node in ego_network.nodes
    ]

    plt.figure(figsize=(10, 10))

    nx.draw(
        ego_network,
        positions,
        with_labels=True,
        node_size=node_sizes,
        node_color=node_colors,
        edge_color="gray",
        font_size=10,
        font_color="black",
        alpha=0.9,
        linewidths=2
    )

    plt.title(
        f"Top Connections of '{central_skill}'",
        fontsize=14,
        fontweight="bold"
    )

    plt.show()

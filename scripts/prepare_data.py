import networkx as nx
import gzip
import pickle
import os

DATA_DIR = "data"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

EDGE_FILE = os.path.join(DATA_DIR, "email-Eu-core.txt.gz")
LABEL_FILE = os.path.join(DATA_DIR, "email-Eu-core-department-labels.txt.gz")
OUTPUT_PKL = os.path.join(OUTPUT_DIR, "email_eu_core_spminer.pkl")

print("Loading directed email network...")
G = nx.Graph()

with gzip.open(EDGE_FILE, "rt") as f:
    for line in f:
        if line.startswith("#"):
            continue
        u, v = map(int, line.strip().split())
        G.add_edge(u, v)

print(f"Loaded graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")

print("Loading department labels...")
labels = {}   # node -> department

with gzip.open(LABEL_FILE, "rt") as f:
    for line in f:
        if line.startswith("#"):
            continue
        node, dept = map(int, line.strip().split())
        labels[node] = dept

print(f"Loaded labels for {len(labels)} nodes")

print("Preparing SPMiner data format...")

data = {
    "nodes": list(G.nodes()),
    "edges": [(u, v) for u, v in G.edges()],
    "labels": [labels.get(n, -1) for n in G.nodes()]  # -1 if missing label
}

with open(OUTPUT_PKL, "wb") as f:
    pickle.dump(data, f)

print(f"Saved SPMiner-ready file to: {OUTPUT_PKL}")

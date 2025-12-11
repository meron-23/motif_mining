# Email Subgraph Mining Report

## Overview
This project demonstrates subgraph mining on an email communication network to discover recurring patterns of interaction. Each edge in the network represents a bidirectional email communication between two users. The mining was conducted using **SPMiner**, which extracts subgraphs from the graph representation of the dataset.

## Dataset
- The original email dataset was converted from `.gz` format to a **single undirected graph**.
- Nodes represent individual email users.
- Edges represent mutual email communications (converted to undirected for compatibility with SPMiner).

## Mining Configuration
- **Graph Type:** Undirected
- **Node Anchored:** Yes (some nodes in subgraphs are marked as anchors)
- **Neighborhood Sampling:** Multiple subgraphs sampled per graph (`n_neighborhoods`)
- **Subgraph Sizes:** Minimum 3 nodes, maximum 6 nodes observed in results
- **Sampling Method:** Tree-based sampling to explore local neighborhoods

## Results
A selection of extracted subgraphs:

| Subgraph | #Nodes | #Edges | Anchor Node(s) |
|----------|--------|--------|----------------|
| 1        | 3      | 2      | 129            |
| 2        | 3      | 3      | 262            |
| 3        | 4      | 4      | 969            |
| 4        | 4      | 4      | 463            |
| 5        | 4      | 3      | 814            |
| 6        | 4      | 5      | 891            |
| 7        | 4      | 4      | 692            |
| 8        | 5      | 6      | 602            |
| 9        | 5      | 6      | 105            |
| 10       | 5      | 6      | 884            |
| 11       | 5      | 5      | 826            |
| 12       | 5      | 5      | 230            |
| 13       | 6      | 8      | 896            |
| 14       | 6      | 8      | 695            |
| 15       | 6      | 9      | 936            |
| 16       | 6      | 8      | 351            |
| 17       | 6      | 9      | 862            |

### Observations
- Subgraphs range from **3 to 6 nodes**, with edges forming common interaction patterns.
- **Anchor nodes** are highlighted, representing key users around whom interactions occur.
- The patterns suggest clusters of users who communicate frequently, indicating potential teams, groups, or important communication hubs.

## Conclusion
SPMiner successfully extracted meaningful subgraphs from the email network, capturing frequent interaction motifs. These patterns can be further analyzed for insights into **user behavior**, **communication clusters**, or **organizational structure**.

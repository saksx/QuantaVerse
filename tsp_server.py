from fastapi import FastAPI, Form

from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware

"""
Installations:
pip install fastapi uvicorn python-multipart

Run:
uvicorn tsp_server:app --reload

"""

def tsp_quantum_solver(adj_matrix):
    """ TODO: Complete this function"""

    return [0, 1, 2, 3]


## TODO: Create a Appropriate Distances matrix to build upon
distances_matrix = [
    [0, 1, 2, 3],
    [1, 0, 4, 5],
    [2, 4, 0, 6],
    [3, 5, 6, 0]
]


def get_adj_matrix(list_of_cities):
    adj_matrix = []
    for i in range(len(list_of_cities)):
        adj_matrix.append([])
        for j in range(len(list_of_cities)):
            adj_matrix[i].append(distances_matrix[list_of_cities[i]][list_of_cities[j]])
    return adj_matrix

app = FastAPI()

# Allow cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/solve")
def solve_tsp(nodes: Annotated[str, Form(...)]):
    nodes = list(map(int, nodes.split(',')))
    print(nodes, type(nodes))
    
    adj_matrix = get_adj_matrix(nodes)
    print(adj_matrix)
    return tsp_quantum_solver(adj_matrix)
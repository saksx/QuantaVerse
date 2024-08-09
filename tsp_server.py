from fastapi import FastAPI, Form

from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware

from qiskit.circuit.library import TwoLocal
from qiskit_optimization.applications import Tsp
from qiskit_algorithms import SamplingVQE
from qiskit_algorithms.optimizers import SPSA
# from qiskit_algorithms.utils import algorithm_globals
from qiskit.primitives import Sampler as Sampler

from qiskit_optimization.converters import QuadraticProgramToQubo

import networkx as nx

"""
Installations:
pip install fastapi uvicorn python-multipart

Run:
uvicorn tsp_server:app --reload
"""

def tsp_quantum_solver(adj_matrix):
    graph = nx.from_numpy_array(adj_matrix)
    tsp = Tsp(graph)
    qp = tsp.to_quadratic_program()
    
    qp2qubo = QuadraticProgramToQubo()
    qubo = qp2qubo.convert(qp)
    qubitOp, offset = qubo.to_ising()
    
    optimizer = SPSA(maxiter=300)
    ry = TwoLocal(qubitOp.num_qubits, "ry", "cz", reps=5, entanglement="linear")
    vqe = SamplingVQE(sampler=Sampler(), ansatz=ry, optimizer=optimizer)

    result = vqe.compute_minimum_eigenvalue(qubitOp)

    x = tsp.sample_most_likely(result.eigenstate)
    z = tsp.interpret(x)
    
    return z

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
    allow_origins=["*", "null"],
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
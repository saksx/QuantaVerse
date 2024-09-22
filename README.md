# Quantum Travelling Salesman Problem for Vaccine Distribution in Nepal

## Project Description

In the logistics industry, optimizing distribution is crucial, especially when it comes to routing a fleet of vehicles to deliver goods from central depots to various clients. For vaccine distribution, the challenge becomes even more critical due to the need for timely and efficient delivery to save lives. This project aims to address this challenge by applying quantum computing to find optimal routes for vaccine distribution in rural Nepal.

We propose a solution that leverages quantum approaches:

- **Quantum Travelling Salesman Problem (TSP)** algorithm will be used to find the shortest paths within each cluster to efficiently distribute vaccines.

By solving this problem with a quantum solution, we hope to optimize vehicle routing, leading to more timely vaccine delivery and reduced distribution costs.

## Project Components

### 1. Frontend User Interface
The frontend provides an interactive map where users can select various locations in Nepal. Once the locations are selected, the backend processes the data and returns the optimal route for distributing vaccines.

#### Technologies:
- HTML, CSS, JavaScript
- Mapbox for map integration 

#### Implementation Details:
- **Map Integration:** Use a static image of a map or an interactive map service like Mapbox.
- **User Input:** Users click on the map to select locations, which are then passed to the backend for processing.
- **API Communication:** The frontend sends the selected locations to the backend API, receives the optimal route, and displays it on the map.

### 2. Backend Server
The backend handles requests from the frontend, processes the data, and interfaces with the quantum component. It is responsible for converting location names into indices and ensuring compatibility between the frontend and quantum algorithm.

#### Technologies:
- Python
- FastAPI or any lightweight web framework

#### Implementation Details:
- **API Endpoints:** Create endpoints to receive points data from the frontend and send responses with the optimal path.
- **Data Mapping:** Map location names to indices for quantum algorithm input.
- **Quantum Integration:** Pass the graph representation of the problem to the quantum component and return the solution to the frontend.

### 3. Quantum Implementation
The quantum algorithm is the core of this project. We will implement the Travelling Salesman Problem (TSP) using Qiskit, simulating quantum behavior to solve the problem.

#### Technologies:
- Qiskit (IBM’s quantum computing framework)

#### Implementation Details:
- **Input Graph Representation:** Define how the locations will be represented as a graph.
- **Quantum TSP Algorithm:** Implement the algorithm using Qiskit.
- **Simulator:** Use a quantum simulator for demonstration purposes due to queue times on real quantum computers. The algorithm can handle up to 4 nodes (16 qubits) for our demonstration.

### Constraints:
- The quantum simulation can only handle up to 4 nodes, so users will be limited to selecting up to 4 locations from a possible pool of 10.

## Resources

- [Quantum TSP Using PyQuil Tutorial](https://github.com/mstechly/quantum_tsp_tutorials)
- [Qiskit TSP Tutorial](https://qiskit.org/documentation/optimization/tutorials/06_examples_max_cut_and_tsp.html)
- [Quantum Optimization Solutions](https://medium.com/@vasilybokov/traveling-salesman-problem-with-quantum-optimization-solutions-and-perspectives-59137f3241cd)
- [Travelling Salesman Problem on Quantum Computer](https://medium.com/@michal.stechly/solving-the-traveling-salesman-problem-using-quantum-computer-bb00438de223)

## Setup and Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo-url
   cd your-repo
   ```

2. **Frontend Setup:**
   - Implement the frontend using HTML, CSS, and JavaScript.
   - Optionally integrate Mapbox for the interactive map.

3. **Backend Setup:**
   - Install FastAPI:
     ```bash
     pip install fastapi
     pip install uvicorn
     ```
   - Set up API endpoints to communicate with the frontend.

4. **Quantum Algorithm:**
   - Install Qiskit:
     ```bash
     pip install qiskit
     ```
   - Implement the quantum TSP algorithm and test it with different datasets.

5. **Running the Server:**
   - Start the FastAPI server:
     ```bash
     uvicorn main:app --reload
     ```

6. **Testing:**
   - Use the frontend to select locations and check the optimal path returned by the quantum algorithm.

## Acknowledgements
We would like to thank IBM for their excellent quantum computing resources and tutorials. Special thanks to the authors of the articles and GitHub repositories referenced in this project.

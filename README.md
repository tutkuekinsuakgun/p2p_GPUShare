# P2P GPU Sharing Platform

This project is a P2P GPU sharing platform that enables decentralized task distribution using libp2p and the Ray framework. The platform allows users to utilize available GPUs on the network to perform distributed computation tasks. It uses TensorFlow for GPU-based operations and libp2p for peer-to-peer communication.

## Project Structure
p2p_GPUShare/ 
│ 
├── go/ 
│   └── main.go # Go-based libp2p node implementation 
│ 
└── p2p/ 
    └── p2pGPU.py # Python-based Ray and TensorFlow task distribution

### Files
- **main.go**: Implements a libp2p node that listens for TCP connections and processes compute tasks.
- **p2pGPU.py**: Implements a Python script using Ray for distributed GPU tasks and TensorFlow for computations. It also sends tasks between nodes using socket connections.

## Prerequisites

Before running the project, make sure you have the following installed:
- **Go** (for the libp2p node)
- **Python 3.x** (for Ray and TensorFlow)
- **Ray Framework**: Install using `pip install ray`
- **TensorFlow**: Install using `pip install tensorflow`
- **libp2p Go library**: This will be automatically installed when setting up the Go project.

## Setup Instructions

### 1. Go Setup

Navigate to the go directory and initialize the Go module:

```bash
cd p2p_GPUShare/go
go mod init p2p_GPUShare
go mod tidy
```

This will create the `go.mod` file and install the required dependencies for libp2p.

To run the Go node:
```bash
go run main.go
```

### 2. Python Setup
Navigate to the p2p directory and run the Python script that handles GPU tasks using Ray:

```bash
cd ../p2p
python p2pGPU.py
```

This script will:
- Start Ray, allowing distributed GPU tasks to be executed.
- Send a compute task to the libp2p node and retrieve the result.
- Display the computed results from both GPU tasks and P2P node tasks.

## Usage
Start the Go-based libp2p node first:

```bash
go run main.go
```

In a separate terminal, run the Python script:

```bash
python p2pGPU.py
```

The Python script will send compute tasks to the Go-based libp2p node and collect the results of both GPU and node-based computations.

### Example Output

```
GPU sonuçları: [0, 1, 4, 9, 16]
Toplanan Sonuçlar: ['Computed result: 42']
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

### Key Commands:
- **Initialize Go module**: `go mod init p2p_GPUShare`
- **Install Go dependencies**: `go mod tidy`
- **Run Go node**: `go run main.go`
- **Run Python tasks**: `python p2pGPU.py`

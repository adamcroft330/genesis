# Genesis Installation Guide for Apple Silicon

This guide provides step-by-step instructions for installing Genesis on Apple Silicon Macs (M1/M2/M3/M4).

## Prerequisites

Before beginning the installation, ensure you have:
- Miniconda3 installed on your system
- Terminal/Command Line access

## Installation Steps
# Genesis Robot Simulation Project

This repository contains robot simulation scripts using the Genesis physics engine, specifically tested on Apple Silicon Macs.

## Prerequisites

Before beginning the installation, ensure you have:
- Miniconda3 installed on your system
- Terminal/Command Line access

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/adamcroft330/genesis

cd genesis
```

### 2. Install Rust (System-wide requirement)
First, install Rust which is required for some Genesis components:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### 3. Create and Setup Conda Environment
Create a new conda environment using the provided environment file:
```bash
conda env create -f environment.yml
conda activate genesis
```

If you prefer to install packages manually, follow these steps:
```bash
# Create environment with Python 3.11
conda create -n genesis python=3.11
conda activate genesis

# Install build dependencies
conda install -c conda-forge cmake=3.26.1 minizip zlib pybind11

# Install PyTorch with MPS support
conda install pytorch torchvision torchaudio -c pytorch

# Install Genesis and its dependencies
pip install genesis-world

# Install OpenGL and Pyrender for rendering support
conda install pyopengl
pip install pyrender
```

## Verification Steps

### 1. Verify PyTorch Installation
Check PyTorch version and MPS (Metal Performance Shaders) availability:
```bash
python -c "import torch; print(torch.__version__)"
python -c "import torch; print(torch.backends.mps.is_available())"
```
Expected output:
```
2.5.1  # (or later)
True
```

### 2. Verify Genesis Installation
Check Genesis version:
```bash
python -c "import genesis; print(genesis.__version__)"
```
Expected output:
```
0.2.0  # (or later)
```

### 3. Verify Pyrender Installation
Check if pyrender is properly installed:
```bash
python -c "import pyrender"
```

## Project Structure
- `scripts/`: Simulation scripts
  - `grasp_waterbottle.py`: Example script demonstrating robot grasping simulation
- `data/`: Input data files (URDFs, meshes, etc.)
- `output/`: Generated output files (videos, logs)

## Running Simulations

To run the water bottle grasping simulation:
```bash
python scripts/grasp_waterbottle.py -v
```

Arguments:
- `-v`, `--vis`: Enable visualization (optional)

## Known Issues and Notes

### Installation Warnings
You may encounter the following warnings during installation or first run:

1. GLFW Class Conflicts:
```
objc[]: Class GLFWHelper is implemented in both [...] taichi_python.cpython-311-darwin.so and [...] libPyGEL.dylib
```
These warnings about GLFW class conflicts between taichi and PyGEL3D can be safely ignored.

2. Sympy Version Conflicts:
```
torch 2.5.1 requires sympy==1.13.1; python_version >= "3.9", but you have sympy 1.13.3
```
This dependency conflict warning can be safely ignored.

### Performance Notes
- The initial genesis import may take several seconds to complete
- Genesis is optimized for Apple Silicon and will use the Metal backend for GPU acceleration through PyTorch's MPS

## System Requirements
- macOS running on Apple Silicon (M1/M2/M3)
- Python 3.11 (recommended for best compatibility)
- Approximately 2GB of free disk space for all dependencies
- Internet connection for downloading packages

## Optional Components
Genesis supports additional optional components that can be installed based on your needs:
- Motion planning (OMPL)
- Surface reconstruction (splashsurf or ParticleMesher)
- Ray Tracing Renderer (LuisaRender)

Refer to the official Genesis documentation for installation instructions for these optional components.

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
MIT

## Contact
adamcroft330@gmail.com

Project Link: [your-repo-url]
### 1. Install Rust (System-wide)
First, install Rust which is required for some components:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### 2. Create Conda Environment
Create and activate a new conda environment with Python 3.11:
```bash
conda create -n genesis python=3.11
conda activate genesis
```

### 3. Install Build Dependencies
Install required build dependencies from conda-forge:
```bash
conda install -c conda-forge cmake=3.26.1 minizip zlib pybind11
```

### 4. Install PyTorch
Install PyTorch with Metal Performance Shaders (MPS) support:
```bash
conda install pytorch torchvision torchaudio -c pytorch
```

### 5. Install Pyrender
Install OpenGL and Pyrender for rendering support:
```bash
conda install pyopengl
pip install pyrender
```

### 6. Install Genesis
Install Genesis and its dependencies:
```bash
pip install genesis-world
```

## Verification Steps

### 1. Verify PyTorch Installation
Check PyTorch version and MPS availability:
```bash
python -c "import torch; print(torch.__version__)"
python -c "import torch; print(torch.backends.mps.is_available())"
```
Expected output:
```
2.5.1  # (or later)
True
```

### 2. Verify Genesis Installation
Check Genesis version:
```bash
python -c "import genesis; print(genesis.__version__)"
```
Expected output:
```
0.2.0  # (or later)
```

### 3. Verify Pyrender Installation
Check if pyrender is properly installed:
```bash
python -c "import pyrender"
```
This should run without any errors.

## Known Issues and Notes

### Installation Warnings
You may encounter the following warnings during installation or first run:

1. GLFW Class Conflicts:
```
objc[]: Class GLFWHelper is implemented in both [...] taichi_python.cpython-311-darwin.so and [...] libPyGEL.dylib
```
These warnings about GLFW class conflicts between taichi and PyGEL3D can be safely ignored.

2. Sympy Version Conflicts:
```
torch 2.5.1 requires sympy==1.13.1; python_version >= "3.9", but you have sympy 1.13.3
```
This dependency conflict warning can be safely ignored.

### Performance Notes
- The initial genesis import may take several seconds to complete
- Genesis is optimized for Apple Silicon and will use the Metal backend for GPU acceleration through PyTorch's MPS

## System Requirements
- macOS running on Apple Silicon (M1/M2/M3)
- Python 3.11 (recommended for best compatibility)
- Approximately 2GB of free disk space for all dependencies
- Internet connection for downloading packages

## Optional Components
Genesis supports additional optional components that can be installed based on your needs:
- Motion planning (OMPL)
- Surface reconstruction (s# Genesis Robot Simulation Project

This repository contains robot simulation scripts using the Genesis physics engine, specifically tested on Apple Silicon Macs.

## Prerequisites

Before beginning the installation, ensure you have:
- Miniconda3 installed on your system
- Terminal/Command Line access

## Installation Steps

### 1. Clone the Repository
```bash
git clone [your-repo-url]
cd genesis-project
```

### 2. Install Rust (System-wide requirement)
First, install Rust which is required for some Genesis components:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### 3. Create and Setup Conda Environment
Create a new conda environment using the provided environment file:
```bash
conda env create -f environment.yml
conda activate genesis
```

If you prefer to install packages manually, follow these steps:
```bash
# Create environment with Python 3.11
conda create -n genesis python=3.11
conda activate genesis

# Install build dependencies
conda install -c conda-forge cmake=3.26.1 minizip zlib pybind11

# Install PyTorch with MPS support
conda install pytorch torchvision torchaudio -c pytorch

# Install Genesis and its dependencies
pip install genesis-world

# Install OpenGL and Pyrender for rendering support
conda install pyopengl
pip install pyrender
```

## Verification Steps

### 1. Verify PyTorch Installation
Check PyTorch version and MPS (Metal Performance Shaders) availability:
```bash
python -c "import torch; print(torch.__version__)"
python -c "import torch; print(torch.backends.mps.is_available())"
```
Expected output:
```
2.5.1  # (or later)
True
```

### 2. Verify Genesis Installation
Check Genesis version:
```bash
python -c "import genesis; print(genesis.__version__)"
```
Expected output:
```
0.2.0  # (or later)
```

### 3. Verify Pyrender Installation
Check if pyrender is properly installed:
```bash
python -c "import pyrender"
```

## Project Structure
- `scripts/`: Simulation scripts
  - `grasp_waterbottle.py`: Example script demonstrating robot grasping simulation
- `data/`: Input data files (URDFs, meshes, etc.)
- `output/`: Generated output files (videos, logs)

## Running Simulations

To run the water bottle grasping simulation:
```bash
python scripts/grasp_waterbottle.py -v
```

Arguments:
- `-v`, `--vis`: Enable visualization (optional)

## Known Issues and Notes

### Installation Warnings
You may encounter the following warnings during installation or first run:

1. GLFW Class Conflicts:
```
objc[]: Class GLFWHelper is implemented in both [...] taichi_python.cpython-311-darwin.so and [...] libPyGEL.dylib
```
These warnings about GLFW class conflicts between taichi and PyGEL3D can be safely ignored.

2. Sympy Version Conflicts:
```
torch 2.5.1 requires sympy==1.13.1; python_version >= "3.9", but you have sympy 1.13.3
```
This dependency conflict warning can be safely ignored.

### Performance Notes
- The initial genesis import may take several seconds to complete
- Genesis is optimized for Apple Silicon and will use the Metal backend for GPU acceleration through PyTorch's MPS

## System Requirements
- macOS running on Apple Silicon (M1/M2/M3)
- Python 3.11 (recommended for best compatibility)
- Approximately 2GB of free disk space for all dependencies
- Internet connection for downloading packages

## Optional Components
Genesis supports additional optional components that can be installed based on your needs:
- Motion planning (OMPL)
- Surface reconstruction (splashsurf or ParticleMesher)
- Ray Tracing Renderer (LuisaRender)

Refer to the official Genesis documentation for installation instructions for these optional components.

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
[Your chosen license]

## Contact
adamcroft330@gmail.com

Project Link: [your-repo-url]splashsurf or ParticleMesher)
- Ray Tracing Renderer (LuisaRender)

Refer to the official Genesis documentation for installation instructions for these optional components.

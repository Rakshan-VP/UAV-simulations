# UAV-simulations

[![Webots](https://img.shields.io/badge/Webots-R2025a-blue)](https://cyberbotics.com/doc/guide/installation)
[![Python](https://img.shields.io/badge/Python-3.8+-brightgreen)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)]()

**Simulation using Webots for different UAVs**  
This repository contains various UAV (Unmanned Aerial Vehicle) simulations using the [Webots open-source robotics simulator](https://cyberbotics.com/doc/overview/what-is-webots), programmed in Python.

---

## 🚁 Overview

This project demonstrates the simulation of multiple UAV configurations, such as quadcopters and VTOLs, in Webots. Each vehicle includes its own mesh, PROTO definition, and simulation world. The controller code is written in Python for flexibility and integration with external robotics frameworks.

---

## 📁 Generic Folder Structure

```text
vehicle-type/                 # Generic folder for each UAV type
├── meshes/                   # 3D models (e.g., .obj, .stl)
│   └── quadrotor.obj         # Example 3D mesh file
├── protos/                   # Custom PROTO definitions
│   └── MyDrone.proto         # Example PROTO file
├── worlds/                   # Webots .wbt simulation worlds
│   └── default_world.wbt     # Example simulation world
├── controllers/              # Python controller scripts
│   └── simple_control/       # A basic example controller
│       └── control.py        # Control logic script
└── README.md                 # Vehicle-specific documentation
```

---

## 🛠️ Dependencies

### ✅ Required Software

* [Webots R2025a or later](https://cyberbotics.com/doc/guide/installation)
* Python 3.8+
* Webots Python API (`webots.controller`)
* (Optional) Python packages:

  * `numpy` (for control/data processing)
  * `matplotlib` (for visualization)
  * `opencv-python` (for video/image input/output)

### 📦 Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Use

1. **Install Webots**  
   Download and install Webots from the [official page](https://cyberbotics.com/doc/guide/installation).

2. **Clone this repository**

```bash
git clone https://github.com/Rakshan-VP/UAV-simulations.git
cd UAV-simulations
```

3. **Open the Simulation in Webots**

* Launch Webots.
* Navigate to `File > Open World...`.
* Choose a `.wbt` file from any vehicle's `worlds/` directory.

  Example:

  ```text
  UAV-simulations/quadrotor/worlds/quad_hover.wbt
  ```

4. **Run the Simulation**

* Press the green ▶️ **Play** button.
* Ensure the correct controller is selected for the UAV node:

  * Right-click UAV node → `Controller` → choose Python script.

---

## 🛠️ Available Vehicles

Each folder under the repository root contains all simulation assets for a specific UAV.

* `quadrotor/`

  * ✅ Basic X-configuration drone
* `tiltrotor_vtol/`

  * 🔄 Work-in-progress tiltrotor VTOL
* `coaxial_uav/`

  * 🧪 Experimental coaxial dual-rotor UAV

Each of these contains:

* `meshes/`: 3D visual models (OBJ, STL)
* `protos/`: Custom UAV Webots PROTO definitions
* `worlds/`: Simulation scenarios
* `controllers/`: Python scripts to control UAV behavior

---

## 📚 Documentation

* [Webots Main Documentation](https://cyberbotics.com/doc/)
* [Controller Programming in Python](https://cyberbotics.com/doc/guide/controller-programming)
* [Creating and Using PROTO Files](https://cyberbotics.com/doc/guide/using-proto-files)

---

## 📜 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for more details.

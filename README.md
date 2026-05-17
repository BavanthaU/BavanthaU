<h1 align="center">Hi, I'm Bavantha 👋</h1>
<p align="center">
  <em>Robotics perception engineer & doctoral candidate @ University of Twente building real-time RGB+IMU spatial perception, SLAM/VIO, 3D scene understanding, and reinforcement learning for autonomous exploration.</em>
</p>

<p align="center">
  <a href="mailto:b.udugama@utwente.nl"><img src="https://img.shields.io/badge/Academic%20Email-b.udugama%40utwente.nl-orange?style=for-the-badge" alt="Email Bavantha"></a>
  <a href="mailto:bavanthaU@eng.pdn.ac.lk"><img src="https://img.shields.io/badge/Email-bavanthaU%40eng.pdn.ac.lk-blue?style=for-the-badge" alt="Email Bavantha"></a>
  <a href="https://www.linkedin.com/in/bavantha-udugama/"><img src="https://img.shields.io/badge/LinkedIn-Bavantha%20Udugama-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Bavantha Udugama"></a>
</p>

---

### 👨‍🔬 About Me
- Robotics researcher advancing monocular spatial perception, SLAM/VIO, metric-semantic mapping, 3D scene graph construction, and reinforcement learning for lightweight autonomous robots.
- Building perception stacks that rely on practical sensor suites—RGB cameras and IMUs—while preserving real-time mapping and scene-understanding capability.
- Using these spatial representations as policy inputs for robots that can explore, reason about unknown environments, and make better navigation decisions.
- Sharing open-source tooling, reproducible experiments, and research companions from my doctoral work at the University of Twente.

### 🧭 What I'm Focused On Right Now
- Training reinforcement learning policies that use learned depth, semantics, metric-semantic maps, and scene-graph structure to improve autonomous exploration skills.
- Connecting the spatial perception systems from my PhD work to robot decision-making for exploration under limited sensing.
- Developing `Mono Hydra++`, a multi-task monocular scene-graph pipeline for real-time 3D indoor mapping.
- Extending `M2H-MX`, an ICRA 2026 SRRA Workshop accepted system for real-time multi-task dense visual perception and monocular spatial understanding.

### 🔬 Research Spotlight
| Project | Objective | Current focus |
| --- | --- | --- |
| **Mono Hydra++** | Real-time monocular scene graph construction with multi-task learning for 3D indoor mapping. | Manuscript under review; focused on robust RGB+IMU mapping, semantic reconstruction, and deployable scene understanding. |
| **M2H-MX** | Real-time multi-task dense visual perception for monocular spatial understanding. | Accepted at the ICRA 2026 SRRA Workshop; integrates depth and semantic prediction into an unmodified monocular SLAM pipeline for cleaner metric-semantic mapping. |
| **M2H** | Multi-task learning with efficient window-based cross-task attention for monocular spatial perception. | Predicting depth, semantic segmentation, edges, and surface normals as a shared perception backbone for monocular mapping systems. |
| **mono_hydra** | Real-time 3D scene graph construction from monocular camera input with IMU for robotic spatial perception and semantic mapping. | Maintaining the baseline system, packaging reproducible code, and connecting scene graphs to downstream robot autonomy tasks. |
| **Spatial RL for Exploration** | Reinforcement learning policies that use the built spatial perception stack to improve autonomous exploration under limited sensing. | Connecting scene graphs, semantic maps, and learned depth to exploration actions in simulation and robot-ready autonomy loops. |

- **Mono Hydra++** extends this direction with multi-task perception for denser, more consistent 3D indoor scene graphs.
- **M2H-MX** improves dense prediction and in-the-loop mapping, including stronger NYUDv2 depth/semantic results and lower trajectory error on ScanNet.
- **M2H** targets compact cross-task predictions that can support mapping, reconstruction, and spatial intelligence on lightweight robots.
- **mono_hydra** pushes monocular SLAM beyond geometry by layering semantic understanding into a robot-ready 3D scene representation.
- **Spatial RL** is the next step: using those spatial representations to learn better exploration behaviour instead of treating perception and planning as separate problems.

### 🧠 Technical Interests
- Deep learning for spatial perception, multi-modal fusion, and cross-task representation learning.
- SLAM/VIO, metric-semantic mapping, 3D reconstruction, and scene graph construction for robot autonomy.
- Reinforcement learning for autonomous exploration, navigation, and decision-making with learned spatial representations.
- Monocular spatial systems like `mono_hydra`, `Mono Hydra++`, and `M2H` that turn research prototypes into deployable autonomy stacks.

### 🛠️ Tools & Technologies
<p>
  <img src="https://img.shields.io/badge/ROS-22314E?style=for-the-badge&logo=ros&logoColor=white" alt="ROS" />
  <img src="https://img.shields.io/badge/ROS2-0A1E5A?style=for-the-badge&logo=ros&logoColor=white" alt="ROS2" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
  <img src="https://img.shields.io/badge/ONNX%20Runtime-005CED?style=for-the-badge&logo=onnx&logoColor=white" alt="ONNX Runtime" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />
  <img src="https://img.shields.io/badge/Gazebo-4A6DBF?style=for-the-badge&logo=ros&logoColor=white" alt="Gazebo" />
  <img src="https://img.shields.io/badge/Isaac%20Sim-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="Isaac Sim" />
  <img src="https://img.shields.io/badge/Stable--Baselines3-000000?style=for-the-badge&logo=openai&logoColor=white" alt="Stable-Baselines3" />
</p>

### 📊 Snapshot
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=BavanthaU&show_icons=true&count_private=true&theme=tokyonight" alt="GitHub stats" />
  <img src="https://streak-stats.demolab.com?user=BavanthaU&theme=tokyonight" alt="GitHub streak" />
</p>
<p align="center">
  <img src="./assets/current_year_commits.svg" alt="Commits this year" />
</p>

### 📝 Latest Papers & Projects
- <img src="https://img.shields.io/badge/Under%20Review-2026-006D77?style=flat-square" alt="Under review 2026 badge" /> **Mono Hydra++: Real-Time Monocular Scene Graph Construction with Multi-Task Learning for 3D Indoor Mapping** – manuscript under review.
- <img src="https://img.shields.io/badge/ICRA%202026-SRRA%20Workshop-006D77?style=flat-square" alt="ICRA 2026 SRRA Workshop badge" /> **M2H-MX: Multi-Task Dense Visual Perception for Real-Time Monocular Spatial Understanding** – [Paper](https://doi.org/10.48550/arXiv.2603.29236) *(Accepted, ICRA 2026 SRRA Workshop)*
- <img src="https://img.shields.io/badge/IROS-2025-blue?style=flat-square" alt="IROS 2025 badge" /> **M2H: Multi-Task Learning with Efficient Window-Based Cross-Task Attention for Monocular Spatial Perception** – [Paper](https://arxiv.org/abs/2510.17363) *(International Conference on Intelligent Robots and Systems, 2025)*
- <img src="https://img.shields.io/badge/ISPRS-2023-blue?style=flat-square" alt="ISPRS 2023 badge" /> **mono_hydra: Real-Time 3D Scene Graph Construction from Monocular Camera Input with IMU** – [Paper](https://arxiv.org/abs/2308.05515) *(ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information Sciences, 2023)*

### 🤝 Let's Collaborate
- Always open to joint projects around autonomous exploration, robust SLAM systems, spatial perception, reinforcement learning, and algorithm benchmarking.
- Reach out via email for research collaborations, talks, or mentorship opportunities.
- Follow my GitHub activity to stay updated with the latest experimental releases and robotics tooling.

---

<!---
BavanthaU/BavanthaU is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
-->

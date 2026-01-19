# Multi-Camera-Vehicle-ReID-TrajectoryID
IEEE 2024 | Trajectory-based Vehicle Re-Identification using YOLOv8, SIFT, Kalman Filter

# Multi-Camera Trajectory Based Vehicle Re-Identification for Robust Traffic Monitoring

This repository contains the implementation of the IEEE 2024 research paper:
**"Multi-Camera Trajectory Based Vehicle Re-Identification for Robust Traffic Monitoring"**.

The project proposes a trajectory-aware ReID framework combining:
- YOLOv8 for real-time detection  
- SIFT for feature extraction  
- Homography for cross-camera mapping  
- Kalman Filter for predictive tracking  
- ResNet50 for deep feature representation  

Achieved **86% mAP on the VeRi-776 dataset**, outperforming existing methods.

---

## 🔍 Problem Statement
Vehicle Re-Identification across multiple cameras is challenging due to occlusion, viewpoint change, and lighting variation. Traditional image-based ReID methods fail to capture motion continuity.  
This work introduces a **trajectory-based ReID approach** to improve robustness.

---

## 🧠 Architecture Overview
<img width="507" height="861" alt="image" src="https://github.com/user-attachments/assets/321006c4-1215-44e8-9fee-21790a962f76" />


---

## ⚙️ Tech Stack
- Python
- PyTorch
- YOLOv8
- OpenCV
- SIFT
- Kalman Filter
- NumPy, Matplotlib

---

## 📊 Results
| Metric | Value |
|------|------|
| mAP | 86% |
| YOLO Detection Accuracy | 95.2% |
| Kalman Tracking Accuracy | 93.4% |

---

## 👨‍💻 Authors & Contributors

- **Emandi Venkata Sanjeevi Sai Prasanna**  
  B.Tech Artificial Intelligence  
  IEEE Author | AI Engineer | Data Analyst  

- **R. Athilakshmi**  
  Department of Computational Intelligence,  
  SRM Institute of Science and Technology  

- **Syed Yasir**  
  Department of Computational Intelligence,  
  SRM Institute of Science and Technology  


---

## 📄 Paper
[Download IEEE Paper](paper/IEEE_Paper.pdf)

---

## 🚀 How to Run
```bash
pip install -r requirements.txt
python src/main.py

---


 

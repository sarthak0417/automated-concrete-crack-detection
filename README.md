# Automated Concrete Crack Detection Using Computer Vision Techniques for Structural Health Monitoring

## Project Overview

This research project investigates automated concrete surface crack detection using traditional computer vision and image-processing techniques.

The project implements and evaluates three OpenCV-based approaches:

1. Canny edge detection
2. Adaptive thresholding
3. Morphological processing

The primary objective is to compare their effectiveness in identifying visible concrete surface cracks using a labeled image dataset.

The project includes a literature review, research methodology, experimental evaluation, quantitative performance analysis, and reproducible Python implementation.

## Research Background

Concrete cracks are common indicators of deterioration in civil infrastructure, including bridges, buildings, roads, and pavements.

Traditional visual inspection can be time-consuming, labor-intensive, and subjective. Automated image-processing techniques can assist inspectors by identifying potential surface defects in digital images.

Existing research has investigated traditional edge detection, adaptive thresholding, morphological operations, and deep-learning approaches for concrete crack detection.

Our research focuses on evaluating lightweight traditional computer vision techniques as reproducible baselines.

## Literature Review

The research documentation includes a collection of ten published papers related to concrete crack detection.

The literature covers:

- Traditional edge detection and image processing
- Adaptive thresholding
- Morphological processing
- Concrete crack image datasets
- CNN-based crack detection
- Pixel-level crack segmentation
- Structural health monitoring

Key studies include Cha et al. (2017), Jahanshahi and Masri (2012), Dorafshan et al. (2018), Qu et al. (2018), Kim and Cho (2018), Li and Zhao (2020), Kim and Son (2023), Khan et al. (2023), and Avendaño et al. (2024).

See [Literature Review](docs/literature_review.md) for details.

## Research Objectives

1. Implement automated concrete crack detection using Python and OpenCV.
2. Apply grayscale conversion and Gaussian filtering for preprocessing.
3. Compare Canny edge detection, adaptive thresholding, and morphological processing.
4. Develop image-level crack classification rules using foreground-pixel density.
5. Evaluate classification performance using accuracy, precision, recall, F1-score, and confusion matrices.
6. Analyze experimental findings and limitations.

## Dataset

**Dataset:** Concrete Crack Images for Classification

**Source:** https://data.mendeley.com/datasets/5y9wdsg2zt/2

The dataset contains 40,000 labeled concrete images:

| Class | Number of Images |
|---|---:|
| Positive (Crack) | 20,000 |
| Negative (No Crack) | 20,000 |
| **Total** | **40,000** |

A balanced sample of 400 images was used for preliminary experimental evaluation.

| Subset | Positive | Negative | Total |
|---|---:|---:|---:|
| Calibration | 60 | 60 | 120 |
| Testing | 140 | 140 | 280 |

The complete dataset is stored locally and excluded from GitHub.

## Research Methodology

The experimental workflow consists of the following stages:

**Stage 1 — Image Acquisition**

Concrete images are loaded from the labeled dataset.

**Stage 2 — Image Preprocessing**

Images are converted to grayscale, resized to 227 × 227 pixels, and processed using a 5 × 5 Gaussian filter.

**Stage 3 — Crack Feature Extraction**

Three processing approaches are applied:

- Canny edge detection using thresholds of 50 and 150.
- Gaussian adaptive thresholding with binary inversion.
- Morphological opening applied to the adaptive thresholding output using a 3 × 3 kernel.

**Stage 4 — Image Classification**

The proportion of nonzero pixels in each processed image is calculated.

Classification thresholds and comparison directions are selected using the calibration subset to maximize F1-score.

**Stage 5 — Performance Evaluation**

The selected rules are evaluated on the held-out test subset.

## Experimental Results

The following results were obtained on 280 test images.

| Technique | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| **Canny** | **94.29%** | **92.47%** | **96.43%** | **94.41%** |
| Adaptive Thresholding | 58.21% | 55.02% | 90.00% | 68.29% |
| Morphology | 69.64% | 65.54% | 82.86% | 73.19% |

Canny achieved the highest accuracy and F1-score among the three methods in the preliminary evaluation.

These results apply only to the selected experimental sample and should not be interpreted as universal performance estimates.

### Performance Comparison

![Performance Comparison](experiments/results/metrics_comparison.png)

## Project Structure

```text
automated-concrete-crack-detection/
├── src/
│   ├── main.py
│   └── crack_detection.py
├── data/
│   ├── README.md
│   └── raw/
│       ├── Positive/
│       └── Negative/
├── experiments/
│   ├── evaluate.py
│   └── results/
├── docs/
│   ├── research_papers/
│   ├── literature_review.md
│   ├── references.bib
│   ├── research_gap.md
│   ├── research_proposal.md
│   ├── methodology.md
│   ├── experiment_log.md
│   └── results_analysis.md
├── reports/
├── README.md
├── requirements.txt
└── .gitignore
```

## Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib
- Scikit-learn
- Git and GitHub
- LaTeX / Overleaf for research reporting

## Installation

Clone the repository:

```bash
git clone https://github.com/sarthak0417/automated-concrete-crack-detection.git
cd automated-concrete-crack-detection
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Project

### Single-Image Processing

```bash
python src/main.py --image path/to/concrete_image.jpg
```

The program saves processed images and a comparison figure to `experiments/results/`.

### Dataset Evaluation

Download and extract the dataset into:

```text
data/raw/Positive/
data/raw/Negative/
```

Run:

```bash
python experiments/evaluate.py
```

The evaluation script generates performance metrics, prediction records, comparison graphs, and confusion matrices.

## Research Documentation

- [Literature Review](docs/literature_review.md)
- [Research Gap](docs/research_gap.md)
- [Research Proposal](docs/research_proposal.md)
- [Methodology](docs/methodology.md)
- [Experiment Log](docs/experiment_log.md)
- [Results Analysis](docs/results_analysis.md)
- [Bibliography](docs/references.bib)

## Limitations

- Only 400 images were selected for the preliminary experiment.
- Final evaluation was performed on 280 held-out images.
- Classification is based on foreground-pixel-density heuristics.
- Pixel-level segmentation accuracy was not evaluated.
- The system does not measure crack depth or structural safety.
- Generalization to other datasets and real-world conditions remains untested.

## Future Scope

Possible extensions include CNN-based crack classification, independent dataset evaluation, pixel-level crack segmentation, crack width estimation, and real-time inspection applications.

## Project Status

The core OpenCV implementation and preliminary comparative experiment have been completed.

Research documentation and final reporting are being prepared.

## Disclaimer

This project is an academic research prototype intended to investigate image-based concrete surface crack classification. It is not a substitute for professional structural inspection or safety assessment.
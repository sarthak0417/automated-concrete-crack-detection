# Experimental Log

## Project Title
Automated Concrete Crack Detection Using Computer Vision Techniques for Structural Health Monitoring

## Experiment 1: OpenCV-Based Concrete Crack Classification

**Status:** Completed  
**Dataset:** Concrete Crack Images for Classification  
**Implementation:** Python and OpenCV

### Objective

To evaluate and compare three traditional image-processing approaches for identifying visible concrete cracks.

### Dataset Preparation

The dataset contains 40,000 concrete surface images, equally divided between cracked and non-cracked samples.

A balanced subset of 400 images was randomly selected using seed 42.

The dataset was divided into:

- Calibration: 120 images
- Testing: 280 images

### Implemented Techniques

**1. Canny Edge Detection**

Gaussian blur was applied before Canny edge detection to reduce image noise.

**2. Adaptive Thresholding**

Adaptive Gaussian thresholding was used to identify darker image regions.

**3. Morphological Processing**

Morphological opening was applied to the adaptive threshold output to remove small foreground regions.

### Classification Procedure

The proportion of nonzero pixels in each processed image was calculated.

A threshold and comparison direction were selected separately for each method using the calibration set to maximize F1-score.

These rules were evaluated on the held-out test set.

### Experimental Results

| Technique | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Canny | 94.29% | 92.47% | 96.43% | 94.41% |
| Adaptive Thresholding | 58.21% | 55.02% | 90.00% | 68.29% |
| Morphology | 69.64% | 65.54% | 82.86% | 73.19% |

### Observations

Canny achieved the highest classification accuracy and F1-score among the evaluated methods.

Adaptive thresholding achieved high recall but comparatively low precision, suggesting that it frequently classified non-cracked images as cracked.

Morphological opening improved accuracy and F1-score compared with adaptive thresholding alone, although it remained below Canny.

### Generated Artifacts

The evaluation script generated:

- `metrics.csv`
- `predictions.csv`
- `metrics_comparison.png`
- Three confusion matrix figures

### Limitations

The evaluation uses a relatively small sample of the available dataset.

The methods rely on foreground-pixel density rather than detailed crack geometry.

Further evaluation on independent datasets would be required to assess generalization.

### Reproduction

Run:

`python experiments/evaluate.py`

The results are saved in `experiments/results/`.
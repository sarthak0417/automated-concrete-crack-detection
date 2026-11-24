# Experimental Results and Analysis

## 1. Overview

This study compares three OpenCV-based image-processing approaches for binary classification of concrete surface images.

The evaluation was performed on 280 held-out test images containing equal numbers of cracked and non-cracked samples.

## 2. Quantitative Comparison

| Method | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Canny | 94.29% | 92.47% | 96.43% | 94.41% |
| Adaptive Thresholding | 58.21% | 55.02% | 90.00% | 68.29% |
| Morphology | 69.64% | 65.54% | 82.86% | 73.19% |

## 3. Canny Edge Detection

Canny achieved the highest accuracy and F1-score in this experiment.

Its precision of 92.47% indicates that most images classified as cracked were correctly identified.

Its recall of 96.43% indicates that it detected most of the cracked images in the test sample.

## 4. Adaptive Thresholding

Adaptive thresholding achieved 90% recall but only 55.02% precision.

This indicates that it identified many cracked images but also produced a substantial number of false-positive classifications.

## 5. Morphological Processing

Morphological processing achieved 69.64% accuracy and 73.19% F1-score.

Compared with adaptive thresholding alone, morphological opening improved precision and overall classification performance but reduced recall.

## 6. Comparative Interpretation

Canny performed best under the selected experimental configuration.

However, this finding does not establish that Canny is universally superior to adaptive thresholding or morphological methods.

The classification rules were calibrated on a subset of the same dataset, and the test sample was limited to 280 images.

## 7. Research Contribution

The project provides a reproducible comparative baseline for image-level concrete crack classification using traditional OpenCV techniques.

It demonstrates how preprocessing, feature extraction, threshold calibration, and quantitative evaluation can be combined into a lightweight experimental workflow.

## 8. Future Improvements

Potential extensions include:

- Testing on additional independent datasets.
- Comparing with a CNN-based classifier.
- Evaluating pixel-level crack segmentation.
- Investigating lighting and texture robustness.
- Measuring computational performance.
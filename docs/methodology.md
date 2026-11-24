# Research Methodology

## 1. Dataset

The experiment uses the Concrete Crack Images for Classification dataset.

The locally extracted dataset contains:

- 20,000 positive images containing concrete cracks.
- 20,000 negative images without concrete cracks.
- 40,000 images in total.

For the preliminary evaluation, 200 images were randomly selected from each class using random seed 42.

## 2. Experimental Split

The selected 400 images were divided into:

| Subset | Positive | Negative | Total |
|---|---:|---:|---:|
| Calibration | 60 | 60 | 120 |
| Testing | 140 | 140 | 280 |
| Total | 200 | 200 | 400 |

The calibration images were used to select classification thresholds. The test images were reserved for final evaluation.

## 3. Image Preprocessing

Each image was:

1. Loaded in grayscale.
2. Resized to 227 × 227 pixels.
3. Smoothed using a 5 × 5 Gaussian filter.

This preprocessing provides a consistent image representation before applying the detection techniques.

## 4. Detection Techniques

### Method 1: Canny Edge Detection

Canny edge detection was applied to the Gaussian-blurred image using lower and upper thresholds of 50 and 150.

### Method 2: Adaptive Thresholding

Gaussian adaptive thresholding was applied with binary inversion, a block size of 11, and a constant of 2.

### Method 3: Morphological Processing

Morphological opening was applied to the adaptive thresholding result using a 3 × 3 kernel.

## 5. Feature Extraction and Classification

For each method, the proportion of nonzero pixels in the processed image was calculated.

This value was used as a simple image-level classification feature.

A classification threshold and comparison direction were selected using the calibration images to maximize F1-score.

The selected rule was then applied to the separate test images.

## 6. Evaluation Metrics

The methods were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

## 7. Experimental Results

| Method | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Canny | 94.29% | 92.47% | 96.43% | 94.41% |
| Adaptive Thresholding | 58.21% | 55.02% | 90.00% | 68.29% |
| Morphology | 69.64% | 65.54% | 82.86% | 73.19% |

Canny achieved the highest accuracy and F1-score in the preliminary experiment.

## 8. Limitations

- Only 400 of the available 40,000 images were sampled.
- The test sample contains 280 images.
- The methods use simple foreground-density features.
- Pixel-level crack localization accuracy was not measured.
- The experiment does not establish performance on independent infrastructure datasets.
- The classification thresholds may require recalibration for different image conditions.

## 9. Reproducibility

The experiment can be reproduced using:

`python experiments/evaluate.py`

The evaluation script saves CSV files, confusion matrices, and comparison graphs inside `experiments/results/`.

# Literature Review

## Research Topic
Automated Concrete Crack Detection Using Computer Vision Techniques for Structural Health Monitoring

## Paper 1: Deep Learning-Based Crack Damage Detection Using Convolutional Neural Networks

### Bibliographic Information
- Authors: Young-Jin Cha, Wooram Choi, Oral Buyukozturk
- Year: 2017
- Journal: Computer-Aided Civil and Infrastructure Engineering
- Volume: 32
- Pages: 361-378
- DOI: https://doi.org/10.1111/mice.12263

### Research Problem
Traditional image-processing methods can struggle to distinguish concrete cracks from noise, shadows, lighting variations, and complex surface textures.

### Methodology
The researchers developed a convolutional neural network (CNN) that automatically learns image features.

Concrete photographs were divided into smaller image patches and labeled as cracked or intact.

The trained CNN was combined with a sliding-window approach to detect cracks in larger images.

### Dataset
- 332 original concrete photographs
- 277 photographs used to prepare training and validation data
- 55 separate photographs used for testing
- 40,000 image patches
- Patch resolution: 256 x 256 pixels

### Reported Results
- Training accuracy: 98.22%
- Validation accuracy: 97.95%
- Reported testing accuracy: approximately 97%

These are results reported by the original authors.

### Comparative Analysis
The researchers compared their CNN with Canny and Sobel edge detection.

Their CNN showed stronger performance in the presented examples involving thin cracks, shadows, and lighting variations.

### Limitations
1. CNN training requires substantial labeled image data.
2. Performance may vary across datasets and conditions.
3. Photographs cannot directly reveal internal crack depth.

### Relevance to Our Research
Our project focuses initially on traditional computer vision techniques using OpenCV.

This paper motivates evaluating the sensitivity of edge-based crack detection to image noise, shadows, and lighting conditions.

### Proposed Research Direction
We will compare selected OpenCV-based detection pipelines using a common labeled dataset.

We will investigate whether preprocessing improves the performance of traditional crack detection methods.

### Research Status
Paper reviewed.
Our own experiments have not yet been conducted.


## Comparative Literature Review

### Traditional Image-Processing Approaches

**Jahanshahi and Masri (2012)** developed an adaptive vision-based crack detection approach that incorporates 3D scene reconstruction. Their method adjusts crack segmentation parameters using scene geometry and employs morphological processing to extract crack regions. This study highlights the importance of imaging conditions and the limitations of relying only on edge detection.

**Qu et al. (2018)** proposed a concrete crack detection approach using improved pre-extraction and a second percolation process. Their work addresses the challenges of surface noise, stains, illumination variations, and discontinuous cracks. It demonstrates the importance of preprocessing and crack connectivity.

**Kim and Son (2023)** investigated concrete crack detection using dilation and additional image-processing algorithms. Their approach focuses on detecting crack locations and sizes while reducing incorrect detections. The study supports further investigation of traditional image-processing techniques.

**Avendaño, Leander, and Karoumi (2024)** proposed an adaptive thresholding method based on Median Absolute Deviation. Their method determines thresholds using local image characteristics and uses edge detection to estimate crack boundaries and widths. This demonstrates how threshold selection influences detection performance.

### Deep-Learning Approaches

**Cha, Choi, and Büyüköztürk (2017)** proposed a convolutional neural network for concrete crack detection. Their CNN was trained using 40,000 image patches and achieved approximately 98% accuracy in the reported experiments. The authors also compared their approach with traditional Canny and Sobel edge detection.

**Kim and Cho (2018)** investigated automated crack detection using a CNN-based method designed for field conditions. Their approach uses multiple image categories to help distinguish actual cracks from visually similar objects, such as joints and surface patterns.

**Li and Zhao (2020)** developed a convolutional encoder-decoder network for pixel-level crack detection and measurement. Their approach extends beyond binary image classification by estimating crack geometry.

### Dataset Research

**Dorafshan, Thomas, and Maguire (2018)** introduced SDNET2018, a dataset containing more than 56,000 labeled images of concrete bridge decks, walls, and pavements. It provides a resource for benchmarking crack detection algorithms under varied surface conditions.

SDNET2018 is different from the 40,000-image Concrete Crack Images for Classification dataset used in our experiment.

### Research Reviews

**Khan et al. (2023)** reviewed image-processing techniques for concrete crack detection, covering traditional approaches and deep-learning methods. Their review provides background on research trends, image-processing methods, and remaining challenges.

## Literature Comparison Table

| Study | Year | Main approach | Relevance to our project |
|---|---:|---|---|
| Jahanshahi & Masri | 2012 | Adaptive morphology and 3D reconstruction | Morphological processing |
| Cha et al. | 2017 | CNN, comparison with Canny and Sobel | Motivation for OpenCV baselines |
| Qu et al. | 2018 | Pre-extraction and percolation | Noise reduction |
| Dorafshan et al. | 2018 | SDNET2018 dataset | Dataset benchmarking |
| Kim & Cho | 2018 | CNN and field-image classification | Deep-learning comparison |
| Li & Zhao | 2020 | Encoder-decoder segmentation | Future scope |
| Kim & Son | 2023 | Dilation and image processing | Traditional processing |
| Khan et al. | 2023 | Literature review | Research background |
| Avendaño et al. | 2024 | Adaptive thresholding | Threshold selection |

## Research Direction Based on the Literature

The reviewed studies demonstrate that concrete crack detection can be approached using traditional image processing, machine learning, or deep learning.

Traditional techniques remain relevant because they provide interpretable image-processing operations without requiring CNN training.

Our research evaluates three lightweight OpenCV-based pipelines under a common experimental configuration:

1. Gaussian filtering followed by Canny edge detection.
2. Gaussian filtering followed by adaptive thresholding.
3. Adaptive thresholding followed by morphological opening.

The objective is to compare image-level classification performance rather than claim a new crack detection algorithm.

## Connection to Our Experimental Results

Our preliminary evaluation used 400 images sampled from a 40,000-image dataset.

Of these, 120 images were used for threshold calibration and 280 for testing.

Canny achieved 94.29% accuracy, adaptive thresholding achieved 58.21%, and morphological processing achieved 69.64%.

These results suggest that the Canny-based foreground-density classifier performed best in this particular experiment.

However, comparisons with published CNN results are contextual only because the datasets, experimental protocols, and evaluation tasks differ.

## Research Limitations

The current experiment does not measure crack width, depth, or pixel-level segmentation accuracy.

Its findings are restricted to the sampled images and selected processing parameters.

Future work could include independent dataset testing, pixel-level segmentation, and comparison with CNN-based models.

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

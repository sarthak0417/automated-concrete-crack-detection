# Research Gap and Objectives

## 1. Research Background

Concrete cracks are visible indicators of potential deterioration in civil infrastructure. Traditional inspection methods often rely on manual observation, which can be time-consuming and subjective.

Computer vision provides an opportunity to automate the identification of visible surface cracks using digital images.

## 2. Literature-Based Motivation

Cha et al. (2017) demonstrated that convolutional neural networks can identify concrete cracks under challenging visual conditions and compared their approach with traditional edge detection methods.

Their findings highlight the limitations of conventional image-processing techniques when surface textures, lighting variations, and shadows interfere with crack identification.

## 3. Research Gap Addressed

Although deep learning methods have demonstrated strong crack detection performance, traditional image-processing methods remain useful as computationally lightweight baselines.

Our study investigates how three OpenCV-based processing approaches perform when converted into simple image-level crack classifiers and evaluated using the same labeled dataset.

The contribution is a reproducible comparative baseline, rather than a claim that traditional image processing is a new crack detection technique.

## 4. Research Objectives

1. Implement selected traditional crack detection techniques using OpenCV.
2. Apply consistent image preprocessing to concrete surface images.
3. Develop simple image-level classification rules using detected foreground-pixel density.
4. Compare classification performance using accuracy, precision, recall, and F1-score.
5. Identify the strengths and limitations of each method.
6. Document the experimental procedure and results for reproducibility.

## 5. Research Questions

**RQ1:** Which implemented OpenCV approach provides the highest classification accuracy on the selected test sample?

**RQ2:** How do the methods differ in precision, recall, and F1-score?

**RQ3:** What limitations arise when image-level crack classification relies on simple foreground-pixel-density thresholds?

## 6. Scope

The project focuses on identifying the presence or absence of visible concrete surface cracks in digital images.

It does not estimate crack depth, structural load capacity, or the overall safety of a building.

The reported results are limited to the selected dataset and experimental configuration.
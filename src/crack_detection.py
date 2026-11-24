
from pathlib import Path
import argparse

import cv2
import matplotlib.pyplot as plt
import numpy as np


def detect_cracks(image_path, output_dir="experiments/results"):
    image_path = Path(image_path)

    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Cannot read image: {image_path}")

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Preprocessing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 2. Canny edge detection
    canny = cv2.Canny(blurred, 50, 150)

    # 3. Adaptive thresholding
    threshold = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11,
        2,
    )

    # 4. Morphological processing
    kernel = np.ones((3, 3), np.uint8)
    morphology = cv2.morphologyEx(
        threshold,
        cv2.MORPH_OPEN,
        kernel,
    )

    # 5. Save output images
    results = {
        "Original": cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
        "Grayscale": gray,
        "Gaussian Blur": blurred,
        "Canny": canny,
        "Adaptive Threshold": threshold,
        "Morphology": morphology,
    }

    for name, result in results.items():
        filename = name.lower().replace(" ", "_") + ".png"
        save_image = (
            cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
            if result.ndim == 3
            else result
        )
        cv2.imwrite(str(output_dir / filename), save_image)

    # 6. Generate comparison figure
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))

    for ax, (name, result) in zip(axes.flat, results.items()):
        if result.ndim == 2:
            ax.imshow(result, cmap="gray", vmin=0, vmax=255)
        else:
            ax.imshow(result)

        ax.set_title(name)
        ax.axis("off")

    plt.tight_layout()
    plt.savefig(
        output_dir / "comparison.png",
        dpi=200,
        bbox_inches="tight",
    )
    plt.close(fig)

    print(f"Processing complete. Results saved to: {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument(
        "--output",
        default="experiments/results",
    )

    args = parser.parse_args()
    detect_cracks(args.image, args.output)

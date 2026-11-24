
import argparse
from pathlib import Path

import cv2
import numpy as np

from crack_detection import detect_cracks


def main():
    parser = argparse.ArgumentParser(
        description="Automated Concrete Crack Detection"
    )

    parser.add_argument(
        "--image",
        required=True,
        help="Path to the concrete image"
    )

    parser.add_argument(
        "--output",
        default="experiments/results",
        help="Directory for processed images"
    )

    args = parser.parse_args()

    image_path = Path(args.image)

    if not image_path.is_file():
        print(f"Error: Image not found: {image_path}")
        return

    print("Automated Concrete Crack Detection")
    print("OpenCV Version:", cv2.__version__)
    print("NumPy Version:", np.__version__)

    detect_cracks(image_path, args.output)

    print("Image processing completed successfully!")


if __name__ == "__main__":
    main()

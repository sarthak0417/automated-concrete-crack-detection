
from pathlib import Path
import csv
import random

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw"
OUTPUT = ROOT / "experiments" / "results"
OUTPUT.mkdir(parents=True, exist_ok=True)

SEED = 42
SAMPLES_PER_CLASS = 200
CALIBRATION_FRACTION = 0.3
EXTENSIONS = {".jpg", ".jpeg", ".png"}

random.seed(SEED)


def get_images(folder):
    return sorted(
        p for p in folder.rglob("*")
        if p.is_file() and p.suffix.lower() in EXTENSIONS
    )


def load_dataset():
    calibration, testing = [], []

    for folder_name, label in [("Negative", 0), ("Positive", 1)]:
        images = get_images(DATA / folder_name)

        if len(images) < SAMPLES_PER_CLASS:
            raise ValueError(
                f"Not enough images in {folder_name}: {len(images)}"
            )

        selected = random.sample(images, SAMPLES_PER_CLASS)
        random.shuffle(selected)

        n_cal = int(len(selected) * CALIBRATION_FRACTION)

        calibration.extend((p, label) for p in selected[:n_cal])
        testing.extend((p, label) for p in selected[n_cal:])

    random.shuffle(calibration)
    random.shuffle(testing)
    return calibration, testing


def extract_features(image_path):
    gray = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

    if gray is None:
        raise ValueError(f"Cannot read image: {image_path}")

    gray = cv2.resize(gray, (227, 227))
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    canny = cv2.Canny(blurred, 50, 150)

    threshold = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11, 2
    )

    kernel = np.ones((3, 3), np.uint8)
    morphology = cv2.morphologyEx(
        threshold, cv2.MORPH_OPEN, kernel
    )

    # Fraction of detected foreground pixels.
    # These are heuristic features, not crack probabilities.
    return {
        "Canny": np.count_nonzero(canny) / canny.size,
        "Adaptive Threshold": (
            np.count_nonzero(threshold) / threshold.size
        ),
        "Morphology": (
            np.count_nonzero(morphology) / morphology.size
        ),
    }


def collect_features(samples):
    rows = []
    for i, (path, label) in enumerate(samples, 1):
        features = extract_features(path)
        rows.append({
            "image": str(path.relative_to(DATA)),
            "label": label,
            **features,
        })

        if i % 50 == 0:
            print(f"Processed {i}/{len(samples)} images")

    return rows


def choose_rule(rows, method):
    scores = np.array([row[method] for row in rows])
    labels = np.array([row["label"] for row in rows])

    candidates = np.unique(np.concatenate((
        [scores.min() - 1e-9],
        (np.unique(scores)[:-1] + np.unique(scores)[1:]) / 2,
        [scores.max() + 1e-9],
    )))

    best = None

    for direction in (1, -1):
        for threshold in candidates:
            predictions = (
                scores >= threshold if direction == 1
                else scores <= threshold
            ).astype(int)

            score = f1_score(labels, predictions, zero_division=0)

            if best is None or score > best[0]:
                best = (score, direction, threshold)

    return best[1], best[2]


def predict(rows, method, rule):
    direction, threshold = rule
    scores = np.array([row[method] for row in rows])

    if direction == 1:
        return (scores >= threshold).astype(int)
    return (scores <= threshold).astype(int)


def main():
    calibration, testing = load_dataset()

    print("Calibration images:", len(calibration))
    print("Test images:", len(testing))

    print("Extracting calibration features...")
    calibration_rows = collect_features(calibration)

    print("Extracting test features...")
    test_rows = collect_features(testing)

    methods = ["Canny", "Adaptive Threshold", "Morphology"]
    summary = []

    for method in methods:
        rule = choose_rule(calibration_rows, method)

        y_true = [row["label"] for row in test_rows]
        y_pred = predict(test_rows, method, rule)

        metrics = {
            "Method": method,
            "Accuracy": accuracy_score(y_true, y_pred),
            "Precision": precision_score(
                y_true, y_pred, zero_division=0
            ),
            "Recall": recall_score(
                y_true, y_pred, zero_division=0
            ),
            "F1": f1_score(
                y_true, y_pred, zero_division=0
            ),
            "Direction": ">=" if rule[0] == 1 else "<=",
            "Threshold": float(rule[1]),
        }
        summary.append(metrics)

        cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
        display = ConfusionMatrixDisplay(
            cm, display_labels=["No Crack", "Crack"]
        )
        display.plot(cmap="Blues", values_format="d")
        plt.title(method)
        plt.tight_layout()
        plt.savefig(
            OUTPUT / f"confusion_{method.lower().replace(' ', '_')}.png",
            dpi=180,
        )
        plt.close()

        print(method, metrics)

    with open(OUTPUT / "metrics.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=summary[0].keys())
        writer.writeheader()
        writer.writerows(summary)

    with open(OUTPUT / "predictions.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["image", "actual"] + methods)

        rules = {
            method: choose_rule(calibration_rows, method)
            for method in methods
        }

        predictions = {
            method: predict(test_rows, method, rules[method])
            for method in methods
        }

        for i, row in enumerate(test_rows):
            writer.writerow(
                [row["image"], row["label"]]
                + [int(predictions[m][i]) for m in methods]
            )

    x = np.arange(len(methods))
    width = 0.2

    fig, ax = plt.subplots(figsize=(10, 5))
    for i, metric in enumerate(
        ["Accuracy", "Precision", "Recall", "F1"]
    ):
        ax.bar(
            x + (i - 1.5) * width,
            [row[metric] for row in summary],
            width,
            label=metric,
        )

    ax.set_xticks(x, methods)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Score")
    ax.set_title("OpenCV Crack Classification Comparison")
    ax.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT / "metrics_comparison.png", dpi=200)
    plt.close()

    print("\nEvaluation complete!")
    print("Results saved to:", OUTPUT)


if __name__ == "__main__":
    main()

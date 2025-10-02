"""This script generates the PSN plots shown in the paper. It's not intended
to be a expansive library for plot generation, but rather a simple script for
generating paper-ready plots."""

import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def get_threshold(filename: str) -> int:
    """Extracts the threshold value from a filename."""
    match = re.search(r'threshold_(\d+)_', filename)
    if match:
        return int(match.group(1))
    else:
        raise ValueError(f"Could not find threshold in filename: {filename}")

def plot_noise(directory: Path):
    """Plots the noise data for a given directory."""
    noc_size = directory.name
    
    # --- Plot inductive noise ---
    fig_inductive = plt.figure(figsize=(3.3, 2.7))
    ax_inductive = fig_inductive.add_subplot(111)
    lines_inductive = []
    labels_inductive = []
    thresholds_inductive = []

    for file in directory.glob('*.csv'):
        if 'inductive' in file.name.lower():
            try:
                threshold = get_threshold(file.name)
                thresholds_inductive.append(threshold)
                labels_inductive.append(f'$\geq {threshold}$')
                
                data = pd.read_csv(file)
                line, = ax_inductive.plot(data['Clock Cycle'], data['Probability'], linewidth=1.0)
                lines_inductive.append(line)
            except ValueError:
                continue

    if lines_inductive:
        sorted_indices = sorted(range(len(thresholds_inductive)), key=lambda k: thresholds_inductive[k])
        sorted_lines = [lines_inductive[i] for i in sorted_indices]
        sorted_labels = [labels_inductive[i] for i in sorted_indices]

        ax_inductive.grid(True)
        ax_inductive.legend(sorted_lines, sorted_labels, loc='lower right')
        ax_inductive.set_xlabel("Clock cycles")
        ax_inductive.set_ylabel("Probability")
        plt.tight_layout()
        
        png_filename = Path("plot") / f"{noc_size}_inductive.png"
        fig_inductive.savefig(png_filename, dpi=600)

        # (30/44) worked out to be a nice scale. There isn't another reason for
        # choosing such a specific value
        fig_inductive.set_size_inches(3.3 * (30/44), 2.7 * (30/44))
        ax_inductive.set_xlabel("Clock cycles", fontsize=8)
        ax_inductive.set_ylabel("Probability", fontsize=8)
        plt.tight_layout()
        png_filename_small = Path("plot") / f"{noc_size}_inductive_small.png"
        fig_inductive.savefig(png_filename_small, dpi=600)

    plt.close(fig_inductive)

    # --- Plot resistive noise ---
    fig_resistive = plt.figure(figsize=(3.3, 2.7))
    ax_resistive = fig_resistive.add_subplot(111)
    lines_resistive = []
    labels_resistive = []
    thresholds_resistive = []

    for file in directory.glob('*.csv'):
        if 'resistive' in file.name.lower():
            try:
                threshold = get_threshold(file.name)
                thresholds_resistive.append(threshold)
                labels_resistive.append(f'$\geq {threshold}$')
                
                data = pd.read_csv(file)
                line, = ax_resistive.plot(data['Clock Cycle'], data['Probability'], linewidth=1.0)
                lines_resistive.append(line)
            except ValueError:
                continue

    if lines_resistive:
        sorted_indices = sorted(range(len(thresholds_resistive)), key=lambda k: thresholds_resistive[k])
        sorted_lines = [lines_resistive[i] for i in sorted_indices]
        sorted_labels = [labels_resistive[i] for i in sorted_indices]

        ax_resistive.grid(True)
        ax_resistive.legend(sorted_lines, sorted_labels, loc='lower right')
        ax_resistive.set_xlabel("Clock cycles")
        ax_resistive.set_ylabel("Probability")
        plt.tight_layout()

        png_filename = Path("plot") / f"{noc_size}_resistive.png"
        fig_resistive.savefig(png_filename, dpi=600)

        # (30/44) worked out to be a nice scale. There isn't another reason for
        # choosing such a specific value
        fig_resistive.set_size_inches(3.3 * (30/44), 2.7 * (30/44))
        ax_resistive.set_xlabel("Clock cycles", fontsize=8)
        ax_resistive.set_ylabel("Probability", fontsize=8)
        plt.tight_layout()
        png_filename_small = Path("plot") / f"{noc_size}_resistive_small.png"
        fig_resistive.savefig(png_filename_small, dpi=600)

    plt.close(fig_resistive)

def main():
    results_dir = Path("results")
    plot_dir = Path("plot")
    plot_dir.mkdir(exist_ok=True)

    for item in results_dir.iterdir():
        if item.is_dir():
            plot_noise(item)

if __name__ == "__main__":
    main()

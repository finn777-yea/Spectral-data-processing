# Spectral Data Processing

This project focuses on processing and visualizing spectra measured from four different NIR sensors. It provides scripts to plot spectral curves for sample measurements and prepare structured data outputs for downstream analysis.

## Project Goals

- Plot and compare spectra collected from multiple NIR sensors.
- Compute similarity metrics between spectra from different sample measurements.

## Setup

Install [uv](https://docs.astral.sh/uv/), then from the project root:

```bash
uv sync
```

### Notebook hygiene (required once per machine)

This project uses [`nbstripout`](https://github.com/kynan/nbstripout) to strip cell outputs and unstable metadata from notebooks before they reach git.
Outputs stay on disk while you work — only the committed version is clean.

After cloning, install the git filter:

```bash
uv run nbstripout --install --attributes .gitattributes
```

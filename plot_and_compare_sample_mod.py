import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import glob
from sklearn.metrics import r2_score

"""
This function is used to parse the csv data and return the wavelength and intensity
"""
def parse_csv_data(path: str):
    df = pd.read_csv(path, encoding='ISO-8859-1')
    df.drop(columns=df.columns[0], inplace=True)
    # average the intensity of the same wavelength
    # wavelength = df.columns.to_numpy(dtype=int)
    intensity = df.mean(axis=0).to_numpy(dtype=float)
    return intensity

"""
sensor: sensor_1, sensor_2, sensor_3, sensor_4
reference_sample: True for lamp on/off, False for other samples
"""

def get_wavelength_range(sensor: str):
    if sensor == "sensor_1":
        return range(1350, 1652, 2)
    elif sensor == "sensor_2":
        return range(1100, 1352, 2)
    elif sensor == "sensor_3":
        return range(1750, 2152, 2)
    elif sensor == "sensor_4":
        return range(1550, 1952, 2)

def get_csv_paths(probes_dir, sensor: str, reference_sample: bool = False):
    if reference_sample:
        patterns = [
            os.path.join(probes_dir, f"{sensor}_empty_cuvette.csv"),
            os.path.join(probes_dir, f"{sensor}_lamp_off.csv"),
        ]
        paths = []
        for pattern in patterns:
            paths.extend(glob.glob(pattern))
        return paths
    else:
        pattern = os.path.join(probes_dir, f"{sensor}_sample_*.csv")
        return glob.glob(pattern)

"""
reference_path: path of the reference csv file: empty cuvette csv file and lamp off csv file
sample_path: path of the sample csv file: sample_*.csv file
"""
def normalize_intensity(reference_path: list[str], sample_path: str):
    # read the reference and sample csv files
    intensity_empty_cuvette = parse_csv_data(reference_path[0])
    intensity_lamp_off = parse_csv_data(reference_path[1])
    intensity_sample = parse_csv_data(sample_path)
    intensity_sample_normalized = (intensity_sample - intensity_lamp_off) / (intensity_empty_cuvette - intensity_lamp_off)
    return intensity_sample_normalized


"""
reference_path: [empty_cuvette.csv, lamp_off.csv] for normalization
path1, path2: sample csv paths with the same wavelength range
"""
def calculate_spectrum_similarity(
    reference_path: list[str], path1: str, path2: str
) -> None:
    intensity1 = normalize_intensity(reference_path, path1)
    intensity2 = normalize_intensity(reference_path, path2)
    if len(intensity1) != len(intensity2):
        raise ValueError(
            f"Spectra must have the same wavelength range: "
            f"{len(intensity1)} vs {len(intensity2)} points"
        )

    if np.std(intensity1) == 0 or np.std(intensity2) == 0:
        correlation = float("nan")
    else:
        correlation = float(np.corrcoef(intensity1, intensity2)[0, 1])
    rmse = float(np.sqrt(np.mean((intensity1 - intensity2) ** 2)))
    mae = float(np.mean(np.abs(intensity1 - intensity2)))
    r2 = float(r2_score(intensity1, intensity2))

    print(
        f"Spectrum similarity (normalized)\n"
        f"  file1: {os.path.basename(path1)}\n"
        f"  file2: {os.path.basename(path2)}\n"
        f"  correlation_coefficient: {correlation}\n"
        f"  root_mean_squared_error: {rmse}\n"
        f"  mean_absolute_error: {mae}\n"
        f"  r2_score: {r2}"
    )




"""
## Plot the spectrum
"""
def plot_sensor_spectrum(probes_dir: str, sensor: str, normalize_data: bool = False):

    reference_path = get_csv_paths(probes_dir, sensor, True)
    sample_path = get_csv_paths(probes_dir, sensor, False)
    font_size_title  = 10
    font_size_ylabel = 8
    font_size_xlabel = 8
    font_size_ticks  = 6
    font_size_legend = 6
    grid_line_width  = 0.5
    plot_line_width  = 0.5
    
    fig = plt.figure(figsize=(7.00,3.20), dpi=150)
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.tick_params(axis='both', which='major', labelsize=font_size_ticks)
    ax.grid(True, linewidth=grid_line_width, ls='--')
    wavelength_range = get_wavelength_range(sensor)
    for path in sample_path:
        if normalize_data:
            intensity = normalize_intensity(reference_path, path)
            ax.plot(wavelength_range, intensity, linewidth=plot_line_width)
        else:
            intensity = parse_csv_data(path)
            ax.plot(wavelength_range, intensity, linewidth=plot_line_width)
    plt.title(sensor)
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Intensity")
    fig.show()

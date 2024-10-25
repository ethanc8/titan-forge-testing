# miniforge test 1

## Running the examples

```bash
mamba activate titan2022
```

### Example 1 - contour-based object detection

Uses OpenCV.

```bash
python contour.py
```

### Example 2 - charuco-based calibration

Uses OpenCV.

```bash
python calib.py
```


## Dependencies

### Install conda/miniforge

First, please have Conda installed on your computer. If it's not installed, please install [Miniforge3](https://conda-forge.org/miniforge/), which includes Conda and a conda-forge based Python environment. You can install Miniforge3 using the following command:

```bash
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
rm Miniforge3-$(uname)-$(uname -m).sh
```

Close and reopen your shell, and run:

```bash
# Prevent Conda from polluting your environment when you're not working on Conda-managed projects.
conda config --set auto_activate_base false
```

### Install dependencies with Conda

Now, you can use Conda to install the dependencies.

```bash
mamba env create -f environment-desktop.yml # or -opi
mamba activate titan2022
```

If you modify `environment.yml`, please run

```bash
mamba env update -f environment-desktop.yml
```

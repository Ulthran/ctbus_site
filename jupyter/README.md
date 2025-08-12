# JupyterLite

## Install

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Build

```bash
jupyter lite build --contents content --output-dir dist
```

## Deploy

```bash
terraform init
terraform apply
```

## Attempted Snakemake Demo

### Why it failed

Unfortunately Snakemake is too deeply intertwined in multithreading, process management, and shell execution -- all of which aren't supported by the Pyiodide kernel -- to work in a pure JavaScript environment. I spent most of a day monkeypatching around non-pure Python dependencies and thread executors but in the end I figured what I'd be left with would be too much of a Frankenstein zombie to even make for a useful demo.

### Install

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Unfortunately `snakemake` is a major pain for working with the Pyodide kernel. The kernel can only work with pure Python wheels and a number of snakemake v9's dependencies are not pure python (`immutables`, etc). So we have to go back to snakemake v7 to get fewer of those dependencies but there are still some so then we have to make our own version of snakemake that cuts out these dependencies (all of them are used for things you would never need in a beginner demo).

```bash
git clone https://github.com/snakemake/snakemake.git
cd snakemake
git checkout v7.32.4
# MAKE CHANGES
python3 -m pip install build
python3 -m build --wheel
cd ..
```

Now there's a `.whl` file under `snakemake/dist/` that we move into `dist/`:

```bash
mv snakemake/dist/snakemake-7.32.4*.whl dist/extensions/@jupyterlite/pyodide-kernel-extension/static/pypi/snakemake-7.32.4-py3-none-any.whl
```

### Build

```bash
jupyter lite build --contents content --output-dir dist
```

### Deploy

```bash
terraform init
terraform apply
```
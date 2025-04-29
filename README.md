### Crate enviroment from scratch

conda create -n agents python=3.11
conda activate agents
conda install -c conda-forge poetry
conda env export --from-history > environment.yml
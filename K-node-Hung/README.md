# K Node

## Get Started

Conda is used to manage the environment for this project. The environment file is `environment.yml`.

### Create Conda environment

```bash
conda env create --file environment.yml
```

### Activate Conda environment

```bash
conda activate opinion_polarization
```

## Run the simulation

```bash
python run.py <network_name> <k_value> <experiment_index>
```

You can customize the `run.py` script parameters to run the simulation with different configurations. To view available options, run

```bash
python run.py --help
```

Example

```bash
# Run the simulation on the karate network with k=2 and experiment index 0
python run.py karate 2 0
# Run the simulation on the karate network with k=3, experiment index 0, 100 rounds, 5 memory, and zero-sum game
python run.py karate 3 0 -r 100 -m 5 --zero-sum
```

## Run the simulation in batch

```bash
python run_batch.py <network_name> <k_value>
```

You can customize the `run_batch.py` script parameters to run the simulation with different configurations. To view available options, run

```bash
python run_batch.py --help
```

Example

```bash
# Run the simulation on the karate network with k=2
python run.py karate 2
# Run the simulation on the karate network with k=3, 5 experiments each k, 100 rounds, 5 memory, 10 core cpus, and zero-sum game
python run.py karate 3 -e 5 -r 100 -m 5 -c 10 --zero-sum
```

## Results

The results of the simulation are stored in the `results` directory.

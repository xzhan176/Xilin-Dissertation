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
python run.py <network_name> <polarization_fn_name> <k_value> <experiment_index>
```

You can customize the `run.py` script parameters to run the simulation with different configurations. To view available options, run

```bash
python run.py --help
```

Example

```bash
# Run the simulation on the karate network with k=2, polarization function named obj, and experiment index 0
python run.py karate obj 2 0
# Run the simulation on the karate network with k=3, polarization function named obj, experiment index 0, 100 rounds, 5 memory, and zero-sum game
python run.py karate obj 3 0 -r 100 -m 5 --zero-sum
```

## Run the simulation in batch

```bash
python run_batch.py <network_name> <polarization_fn_name> <k_value>
```

You can customize the `run_batch.py` script parameters to run the simulation with different configurations. To view available options, run

```bash
python run_batch.py --help
```

Example

```bash
# Run the simulation on the karate network with polarization function named obj and k=2
python run.py karate obj 2
# Run the simulation on the karate network with polarization function named obj, k=3, 5 experiments each k, 100 rounds, 5 memory, 10 core cpus, and zero-sum game
python run.py karate obj 3 -e 5 -r 100 -m 5 -c 10 --zero-sum
```

## Add new network

To add a new network, create a new python file in the `networks` directory. The file should contain an `init` function that returns a tuple containing the network graph, the opinions, and the size of the network.

## Add new polarization function

To add a new polarization function, create a new python file in the `polarization_functions` directory. The file should contain a function named `fn`.

## Results

The results of the simulation are stored in the `results` directory.

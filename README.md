# Lesson: Homomorphic Encryption

This repository is a supplement to the homomorphic encryption lesson from [OpenMined’s](https://www.openmined.org/) [Foundations of Private Computation course](https://courses.openmined.org/courses/foundations-of-private-computation).
The source text for some of the modules in that lesson can be found in `./text/`. Code exercises for some of the modules are in `./code/` and are also hosted on repl.it:

-   https://repl.it/@willclarktech/PaillierExercise
-   https://repl.it/@willclarktech/PaillierSolution
-   https://repl.it/@willclarktech/HomomorphicEncryptionExercise
-   https://repl.it/@willclarktech/HomomorphicEncryptionSolution

It’s probably easiest for you to complete the coding exercises on repl.it, but this repository is here in case you prefer to work locally.

## Setup

This repository assumes you are using Python v3.8 or above. I recommend you work in a virtual environment of some kind.

The easiest way to install dependencies is using [poetry](https://python-poetry.org/), which will also manage virtual environments for you. Simply run

```sh
poetry install
```

then activate the virtual environment by running

```sh
poetry shell
```

If you aren’t using poetry, you can install the dependencies via the `requirements.txt` file in the usual way. For example using pip:

```sh
pip install -r requirements.txt
```

Once you’ve installed the dependencies, you should be able to run the tests and see that they fail:

```sh
pytest
```

## Coding exercises

Your first task is to fill out the functionality for the interfaces defined in `./code/paillier.py`. You can run tests against your code by running `pytest code/test_paillier.py`.

Once you have implemented the Paillier homomorphic encryption system, your second task is to implement a couple of linear models which make use of it. Fill out the functionality for the interfaces defined in `./code/homomorphic_encryption_model.py`. Again, you can run tests against your code by running `pytest code/test_homomorphic_encryption_model.py`.

Be aware that the tests are just simple checks that you’re heading in the right direction, they’re not supposed to be particularly robust. Write more tests if you find it helpful!

If you get stuck, try going back to the course content, or if you’re really stuck then take a look at the solution files.

## Useful scripts

-   Typechecking: `mypy code`
-   Running tests: `pytest`
-   Linting: `pylint code/paillier.py code/test_paillier.py code/homomorphic_encryption_model.py code/test_homomorphic_encryption_model.py`
-   Formatting code: `black code`

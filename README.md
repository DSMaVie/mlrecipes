# MLRecipes

<!-- [![PyPI - Version](https://img.shields.io/pypi/v/-.svg)](https://pypi.org/project/-)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/-.svg)](https://pypi.org/project/-) -->

A Library to orchestrate ML Experiment Pipelines using MLFlow. Inspired by DVC.

- [MLRecipes](#mlrecipes)
  - [Installation](#installation)
  - [License](#license)
  - [Design Considerations](#design-considerations)
    - [State of the Union](#state-of-the-union)
    - [The Design](#the-design)

## Installation

```console
pip install -
```

## License

`mlrecipes` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Design Considerations

### State of the Union

This project is a try at writing the best ML experiment orchestration tool. Often tools contrain you to specfic use cases
(i.e. training) and any other use requires mental overhead. A few examples imho

- DVC only supports smaller experiments that take up a single repo. Projects with multiple distinct repos are possible
  but cumbersome. And parameters are way to static as well
- MLFlow has nice collaborative tracking, but the recipes are quite constrained to training specific pipelines.
- Sisyphus is not well maintained and has some overhead as it is written for distributed workloads and not smaller experiments

Of course that is quite opionated. All these frameworks have a few features I like as well.

- MLFlow has a very nice python api to orchestrate experiments + Tracking Capabilities for Teams + a nice Tracking UI
- DVC has a nice seperation between code and parameters and experiment definition. But params are hacky.
- Sisyphus has (like DVC as well) the nice idea of saving step artifacts between experiments. makes it very reproducable.

### The Design

For a first shot this library will wor something like this.

- a yaml file will define the experiments. it includes
  - global config for the entire experiment with defaults I like
  - step definitions each step has
    - a link to a python function to run
    - params and artifact dependencies
    - output artifacts.
- the prams and file deps etc. are given to the function as parameters.
  - I still have to solve the debugging problem. Ideally I want to keep the injection so barebones that I can test
    and debug the functions without running the entire experiment.
- I can use yaml tags to give some nice logic to path/artifact logic
  - i.e in the globals defined paths to raw/processed/output (global) folders. each experiment could then produce multiple outputs
    and only needs to define filenames and references to these global folders. based on the yaml tag we could then assemble full paths.
- the idea is after compiling the dag (aka analyzing which step depends on which other step) I could wrap them in mlflow run setups.
- a cli should enable DVC style overwrite of params. the experiments should the be tracked independently. that way we can define
  a kind of pipeline and only change a value on the cli to compare versions/ do hyperparam optimizations etc.
- I'd like to try some newer project frameworks for this. either hatch or rye, maybe uv for deps?

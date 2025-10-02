# NoC and Modest Libraries README

This README covers briefly how to use the `noc` and `modest` libraries provided
in this artifact.

## `noc` Library

To use this library, first import it.

```python
import noc
```

Then to create a new `Noc` object specify a NoC, the only required parameter is the size. Additional
parameters are documented in [noc.py](./noc.py).

```python
_2x2 = noc.Noc(2)
```

To print the Modest model, call the "print" function on the `Noc` object. When doing so, you must
specify what kind of properties you would like to include with the model.

```python
# get a model with no properties
model: str = _2x2.print(PropertyType.NO_PROPS)

# write the model to a file
with open("2x2.modest", "w") as f:
    f.write(model)
```

More documentation is available in [noc.py](./noc.py).

## `modest` Library

This library allows you to run Modest from python, provided that you already have the Modest
executable installed in the system (see [modestchecker.net](modestchecker.net) for installation
instructions).

```python
import modest
```

You can run Modest's statistical model checking engine by calling `simulate`. The model checking
engine is called by calling `check`.

```python
sim: str = modest.simulate("models/noc.modest")
check: str = modest.check("models/noc.modest")
```

The model can be specified as either a `Path` or as a `str`. If it's a path then the model file
at that path is passed to Modest. If it's a string then it's assumed that the model was passed
in as a string, and a temporary model file is created.

More documentation is available in [modest.py](./modest.py).

## Examples of How to Use Libraries

There are two main ways we expect these libraries to be of use:

1. Generation of NoC models
2. Automating characterization of PSN for NoC implementations

### Generation of NoC models

The `noc` library can be used to generate NoC models. Once a model is generated, a user can
manipulate it as they would any other Modest model file. Changes to any process can be made,
and the script ensures that the model starts off valid.

### Automating PSN Characterization

[psn_results.py](./psn_results.py) shows an example of how we used these libraries to automate
the characterization of PSN for the results in this paper. Similar methods can be used to
automate NoC characterization over many parameters.

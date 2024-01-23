# Contagion (CIS 211 project)

A simple grid model of contagion

Rumors, diseases, and memes have somewhat different modes of
transmission, but follow similar patterns of spread from person to
person. Models (simulations) can help us consider how the spread and how
their spread may be altered.

## An SIR model

*Compartmental models* are a basic tool in epidemiology. SIR (
susceptible-infected-recovered) models are among the simplest
compartmental models. They model potential transitions of a set of
individuals or homogenous regions between states of susceptibility (S),
infection (I), and recovery (R).

In an SIR model, a susceptible individual may become an infected
individual through contact with another infected individual. An infected
individual may recover. Recovered individuals gain immunity and are
therefore not susceptible to reinfection. An infected person might
instead die, in which case they are also not susceptible (and so death
is technically a subcategory of recovery).

SIR models can be conveniently modeled by a main loop in which a
simulated clock or calendar moves forward in regular increments. These
regular increments, or "ticks" of the virtual clock, provide an
approximation of continuous time in which many individuals may be
evolving concurrently. To maintain an illusion that all individuals
evolve simultaneously, each simulation cycle (tick) is divided into two
parts. In the first part, a next state for each individual is computed,
using only the current states of other individuals.  (Thus the order in
which we loop through individuals does not matter.)  In the second part,
each individual advances to its next state (and again the order in which
we loop through individuals doesn't matter).

### Caveat

While our contagion model is designed to illustrate techniques of
computer simulation, and particularly SIR models of contagion, it is not
based on a real model from epidemiology. The numerical parameters have
been selected merely to provide interesting, somewhat realistic
behavior, and do not reflect actual numbers (e.g., infection rates,
incubation periods, recovery times and rates) for any particular
disease. It is an illustration, not a real epidemiological model.
Nonetheless I think it may give you some insight into how some kinds of
simulation model are constructed.

## Your task

Detailed instructions are in `doc/HOWTO.md`. After constructing the
simulation with two classes of individual `Typical` and `AtRisk`, you
should construct a new class of individual `Wanderer`
and incorporate it in the simulation. This will require changes in
several places, such as initializing the
`Population` object with a suitable proportion of `Wanderer` individuals
based on numerical parameters in `contagion.ini`. The amount of code is
small, and no individual piece of code is complex, but you must
understand how all the pieces fit together to succeed in adding a piece.

Turn in three files. 

* `model.py`, a Python source file. This file *must* contain a class
  called `Wanderer` so that the person grading the project can
  easily find it!
* `contagion.ini`. This configuration file should contain a section
   `[Wanderer]` that sets parameters for your new class
* `contagion.png`, a screen-shot of the display produced by your model
   running with the provided configuration file. 


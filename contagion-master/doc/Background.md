# Background: Contagion Modeling

Rumors, diseases, and memes have somewhat different modes of 
transmission, but follow similar patterns of spread from 
person to person.  Models (simulations) can help us consider
how the spread and how their spread may be altered. 

## Background: Models and Theories

Scientists of all kinds, in the social sciences as well as 
the natural sciences, build and test models. 
A *theory* is a coherent, compact body of rules that have been validated by *evidence*.  A good theory makes testable 
*predictions*, and in particular it makes predictions that 
distinguish the theory from alternative explanations of 
phenomena.  Predictions that 
seem surprising or at odds with the predictions of alternative 
explanations are especially useful in verification.   When a theory 
makes good predictions that we can check, we have more confidence 
in other predictions that it makes. 

A *simulation model* embodies (parts of) a theory in a computer 
program.  Simulation models help us make predictions efficiently, 
whether for testing a proposed theory (usually, but not always, 
variations on an existing body of theory) or for making useful 
predictions from a well-verified theory. 

Every useful model is incomplete and oversimplified,
as necessarily as every useful map is a scaled down, 
simplified representation of geographic reality.  In fact, 
a simulation with *too much* detail may be untrustworthy, 
because it may be *overfit* to the particular data with 
which it has been verified.   

There is much more to be said about theories, models, and the 
ways in which we build understanding, but this is not the 
place for a full discussion of scientific method.  Suffice it 
for now to say that simulation models are a basic tool both 
for building and verifying theories and for putting theory to 
work.

## A *very* simple model of contagion

We will build model of contagion that is far simpler than 
the models an epidemiologist 
would use to model disease spread or that 
a social scientist would use to model rumor spread. 
Nonetheless even this vastly over-simplified model 
will capture some of the patterns and variabilities of 
spread in a group.  

A model of contagious spread, whether of jokes or influenza, 
includes the following: 

* A *population*.  Typically each member of the population 
  represents a person, but we could as well have populations 
  of businesses or bacteria.  Each *individual* in the population 
  has a state that at least distinguishes between 
  *infected* and *uninfected* states.  A more complex 
  model of population might distinguish levels of 
  susceptibility and potential progression of states, 
  for example modelling a limited period of infection 
  followed by a period of immunity.  
 

*  A model of *proximity*:  Members of the population can 
   only make *contact* with a limited number of other individuals. 
   The model proximity can be very simple (e.g., neighboring 
   cells in a grid) or much more complex (social networks 
   of varying density).  It may be static (like the grid) 
   or dynamic (e.g., within a given distance among individuals 
   who are moving in space). 
   
* A model of *time*.  The simplest model is the ticking of 
  an imaginary clock, with the whole population potentially 
  changing state on each tick. 
   
We will consider only very simple grid models in which 
individual members are *proximate* if they are in 
adjacent cells (above, below, left, or right).  We will 
call the individuals in adjacent cells *neighbors*. 
We will model time with a ticking clock.  

The state of each individual in our model will be 
either *vulnerable*, *sick*, or *recovered*.  
We will divide sickness into two stages, 
*asymptomatic* (not yet showing symptoms of disease)
and *symptomatic*.  Some diseases can be spread 
before symptoms show.  Often the behavior of
asymptomatic people (who may not know they have 
been infected) differs from the behavior of 
people who know they are sick. 

# SIR and SEIR Models

The kind of model we are constructing is in the 
general class of *compartmental models* in epidemiology. 









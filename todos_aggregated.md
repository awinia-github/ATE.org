# ATE.org ToDos
This file contains a curated list of all ToDos for ATE.org.
Note that all ToDos, that have been migrated to Jira are removed from this list.


## .\src\ATE\apps\TODO.md
I presume that all these things are MQTT stuff. 
They should be migrated to ATE.equipment.TCC
(see the TODO.md there, and the README.md in ATE.equipment)

## .\src\ATE\equipment\README.md
This package contains EQUIPMENT, so anything that is *NOT* an INSTRUMENT.
Things that belong here :
    - probers (drivers)
    - handler (drivers)
    - TCC (Test Cell Controller)
  
    
We organize the contents per MANUFACTURER of the equipment
WE are also a manufacturer in a sense, but this applies only to TCC
so TCC will be at the top level as a 'Manufacturer' if you want.

## .\src\ATE\equipment\TCC\TODO.md
The Test Cell Controller 

--> this is where the broker is running ... maybe it is best to pack all
the MQTT stuff (at least the server part) here under ?

--> also the client stuff can reside here under I would say :-)

the launching scripts for all elements should reside in ATE.scripts, as upon
install these become available to the OS.

Let yourself be inspired by the 'skeleton.py' file that resides there or not, 
BUT *OBSERVE* the shebang !!!

## .\src\ATE\Instruments\README.md
This is a place holder directory where we will copy in all the stuff the
guys from the LAB and guys like Jonathan and the stuff from InvenSense I
got is placed.

basicaly these are primitive API's to some instrumentation

We will organize things hereunder in the following way:

    - Manufacturer
        - Equipment
            - Implementer
            
so that for example one can write in a test (or better, the common.py file) :

    from ATE.instruments.Keithley.K2000.Micornas import K2000 
    
this 'Implementer' level is needed to let different implementations live
side by side. The idea is that if a common implementation is used/selected, 
it will live one level up, so we can also do :

    from ATE.instruments.Keithley import K2000 
    
if one wants the "unified" implementation and still the shit from other 
implementers is available :-)

Also note that in the case of a 'plugin' the above could become:

    from foo.bar.jefke import K2000

and still the ATE.org system can past this in ! :tada:

now ... the point is that we can't maintain all implementations of everybody
in the TDK group ... so we will need to work with plug-in's (as we do anyway
for the 'import' stuff) OK, but when for example IC-Sense makes a test program
(for Verification to name something), and they use their 'libraries', then 
Micronas will have a problem running this program as they don't have the
referenced libraries installed ... we need thus to foresee a 'copy-in' from 
the libraries to the project !

This way we can define the Equipment level, and the 'Implementer' level is 
de-coupled, but not disfunctional :-)

## .\src\ATE\org\README.md
-->FIXME

## .\src\ATE\org\actions_on\device\TODO.md
### context menus on devices
    - Clone from
	
## .\src\ATE\org\actions_on\die\TODO.md
## logic on 'DieWizard'

When a Maskset is selected, the wizard needs to collect all A grade DIES for 
that maskset.
    - if there is none, then the grade dropdown box needs to gray out
      everything (except 'A') so no aleternative grade can be selected.
      
    - if there is A grades available, then (when something else as A grade
      is selected in grade), these 'A' grade DIES are displayed in the 
      'reference Grade' pulldown box.
      
If a Maskset is selected, the wizard needs to see if the selected mask set
is an ASIC or and ASSP. 

    - ASSP : the 'customer' IS an empty string
    - ASIC : the 'customer' is NOT an empty string

if the selected maskset is an ASIC, then the new die is by default 
also an ASIC, so the Type is filled in as 'ASIC', and in the customer field
the customer is filled in and both the pulldown box and the lineEdit are
disabled.

So only if the Maskset is an ASSP, we have both options available.

Note: work with 'set' of 
        - get_dies_for_hardware
        - get_dies_for_maskset
        - get_dies_for_grade
        - get_dies_for_customer
      for the above logic instead of custom functions in navigator.


## .\src\ATE\org\actions_on\package\TODO.md
### context menus on tree-view

#### context menus on dies
    - Clone from
    
#### context menus on die

    - View
    - Edit
    - Trace
    - <sep>
    - Delete (no 'make obsolete here')

	
## .\src\ATE\org\actions_on\product\TODO.md
### context menus on tree-view

#### context menus on products

    - Add
    - Clone from

#### context menus on product

    - View
    - Edit
    - Trace
    - <sep>
    - Delete (no 'make obsolete here')

## .\src\ATE\org\plugins\README.md
ATE.org is itself a plug-in (pluggy based) for Spyder.

ATE.org is a tester agnostic system to write (ASIC) test programs, however
all things have their order and place, so that:

1. One needs to write as little as possible code.
2. Developers can develop next to eachother and merge their work without problems.
3. Only test need writing, all the rest is 'configuring'.
4. A test can be developed and debugged as a unit. 
5. Support is available for Shmooing, reporting, ...

This is accomplished through a series of wizards that guides us through the process
and prevents us of making costly mistakes.

The ATE.org system is setup as a base system, and it accepts itself other plugins, 
from different sources. Each such plugin can provide ATE.org with one or more of 
the following (but at least **ONE**) :

1. Importers

The ATE.org system has some import hooks (most notably in some wizards).
For each of these hooks, a plugin can supply a 'stub'.

>Use case:
>   In the 'Maskset Wizard', some data needs to be filled in. 
>   Ofcourse this is an error-prune operation, what is more is that the data
>   that is asked will live somewhere on the 'company network'.
>   That is why there is an 'inport hook' present, so that (when implemented)
>   the stub will access (in whatever way) this data and siphones it to the
>   wizard, so that we have a quick, easy and error free modus-operandus.  

TODO: make a list of all import hooks

2. Exporters

The ATE.org system has some standard export hooks (most notably in the project tree).
For each of these hooks, a plugin can supply a 'stub'.

>Use case:
>   Say there is an export hook to generate a changelog of the project with 
>   respect to the previous version.
>   It is not un-thinkable that a specific company wants to have this in a 
>   company tailored format or even content.
>   An exporter hook can thus be provided to do so.

3. Documentation

Whenever a new project is created in ATE.org, the project automatically gets
a 'documentation' folder, that is filled in to the best of ATE.org's knowledge.
Given the fact that ATE.org is grown out of **automotive sensors**, the documentation
folder is filled with documents like the AEC documents, STDF documentation and so on.

>Use case:
>   Say a company is 'Medical' electronics, then a bunch of extra documentation
>   (of which ATE.org is ignorant about) could be needed to be inserted in the
>   documentation folder upon project creation.
>   A specific plugin could be made to extend the knowledge of ATE.org as the 
>   creator deams necessary.

4. Actuators

ATE.org is grown out of **automotive sensor** industry, and specificly for 
**sensors**, there is a 3th party in the mix ... the actuator. 
Examples of actuators are : magnetic field, light, acceleration, positionning, ... 
*ONE* type of actuator is usually build-in to a handler : **temperature**, but
more about that later. The point is that -we-can- but -we-will-not- control the
actuator from the test program. One is quickly seduced to do so, but the result is
that we get a test-program that is no longer portable from one setup to another, 
what is more is that (usually when shit hits the fan) we realize that also tha
actuator needs calibration, maintenance, exchanging, upgrading, and each time we
need to change the test-program ... in the automotive business, this is an
absolute **no-go** (eventhoug plenty of these companies do it this way!)
The solution is thus that the control of the actuator is out-sourced, if not
to the handler (because maybe a closed source commercial handler), then to the
Test Cell Controller (TCC, more about that later).
However, when we 'configure' a test program, we need to make up our mind what
kinds of actuators we are going to use (regardless of who controls them).
ATE.org provides some actuators, but it has no 'crystal ball', so any plugin
can add acctuators to ATE.org. (actually on the long run Actuators should be
pushed-out of ATE.org)

> Note: for now 'actuators' live in "ATE.org/src/ATE/actuators" and are organized
>       in directories based on the actuator type.

5. Equipment

With 'Equipment' we basically mean Handlers and Probers. In any setup we need
this. ATE.org has some widely used handlers and probers, however it should not
be the task of the ATE.org maintainers to maintain these implementations.
A hook allows us to push out (in a later stage) the Equipment to 3th parties
(maybe the manufacturers of these things?!?) and it allows for example a specific
company to handle their equipment themselves.

> Note: for now 'equipment' lives in "ATE.org/src/ATE/equipment" and are orginized
>       in derectores based on the equipment type (hander or prober),
>       then the manufacturer, and then the 'machine'.

6. Instruments

Instruments are basically electronical measurement devices (like you find in 
any electronic lab). For now ATE.org holds some such instruments to get started, 
but similarly to Equipment we want to push this out on the long run, on the other 
hand, ATE.org is tester/instrument agnostic system, meaning that we do need to 
tell ATE.org sooner or later what 'insturments' are used, thus : plugin!

> Note: for now the 'instruments' live in "ATE.org/src/ATE/instruments" and are 
>       organized in directories by manufacturer, and then model.

7. Testers

Testers (aka: ATE or Automatic Test Equipment), is basically a super instrument,
if you want, but the associated libraries are HUGE, and one uses only one
tester at a time (while we might use multiple instruments combined) that is 
why Testers are pulled out of 'Instruments'.


## .\src\ATE\org\sequencers\TODO.md
the stuff in Sequencers.py should be taken and moved to __init__.py as the
abstract base class tha is used to derive :
    - FixedTemperatureSequencer.py
    - VariableTemperatureSequencer.py
    - DevelopmentSequencer.py
    
## .\src\ATE\org\Templates\TODO.md
the ddirectory name should be changed from 'Templates' to 'templates'
to be consistent with the rest of the source tree

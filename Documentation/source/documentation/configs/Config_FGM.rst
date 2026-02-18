.. _FGM:

SU2 DataMiner Configuration for FGM 
===================================

.. contents:: :depth: 2


The following functions are used to access the options used specifically for FGM applications in *SU2 DataMiner*. 


Reaction Mechanism and Transport Model 
--------------------------------------

For Cantera flamelet calculations, a chemical kinetics model and a diffusion model have to be provided. Installation of Cantera comes with several popular chemical kinetics models such as *gri30*, but 
custom kinetics files can be used, as long as they are accessible from the current file location. An error will be raised if the provided kinetics file cannot be accessed.

.. autofunction:: Common.DataDrivenConfig.Config_FGM.SetReactionMechanism


.. autofunction:: Common.DataDrivenConfig.Config_FGM.GetReactionMechanism


1D chemistry simulations in Cantera can be performed with two options for the multi-component diffusion model: "unity-Lewis" or "multicomponent". When selecting 

.. autofunction:: Common.DataDrivenConfig.Config_FGM.SetTransportModel 


.. autofunction:: Common.DataDrivenConfig.Config_FGM.GetTransportModel 


Flamelet Types 
--------------

.. autofunction:: Common.DataDrivenConfig.Config_FGM.RunFreeFlames 


.. autofunction:: Common.DataDrivenConfig.Config_FGM.GenerateFreeFlames 


.. autofunction:: Common.DataDrivenConfig.Config_FGM.RunBurnerFlames


.. autofunction:: Common.DataDrivenConfig.Config_FGM.GenerateBurnerFlames 


.. autofunction:: Common.DataDrivenConfig.Config_FGM.RunEquilibrium


.. autofunction:: Common.DataDrivenConfig.Config_FGM.GenerateEquilibrium


Flamelet Manifold Resolution 
----------------------------


FGM Controlling Variables 
-------------------------


.. autofunction:: Common.DataDrivenConfig.Config_FGM.SetControllingVariables


.. autofunction:: Common.DataDrivenConfig.Config_FGM.GetControllingVariables
    

.. autofunction:: Common.DataDrivenConfig.Config_FGM.SetProgressVariableDefinition 


.. autofunction:: Common.DataDrivenConfig.Config_FGM.GetProgressVariableSpecies 


.. autofunction:: Common.DataDrivenConfig.Config_FGM.GetProgressVariableWeights 


.. autofunction:: Common.DataDrivenConfig.Config_FGM.SetDefaultProgressVariable 



Differential Diffusion 
----------------------

Passive Variables 
-----------------


Output Group Management
-----------------------

SU2 Configuration
-----------------






   

References
----------

.. _reluarticle:

Richard H.R Hahnloser et al. “Digital selection and analogue amplification coexist in a cortex-inspired silicon circuit”. In: Nature 405 (June 2000), pp. 947-951.

.. _eluarticle:

Djork-Arné Clevert, Thomas Unterthiner, and Sepp Hochreiter. “Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs)”. In: (Feb. 2016). URL:http://arxiv.org/abs/1511.07289

.. _geluarticle:

Dan Hendrycks and Kevin Gimpel. “Gaussian Error Linear Units (GELUs)”. In:(June 2023). URL: http://arxiv.org/abs/1606.08415.


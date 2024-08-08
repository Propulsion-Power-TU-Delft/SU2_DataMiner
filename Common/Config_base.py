###############################################################################################
#       #      _____ __  _____      ____        __        __  ____                   #        #
#       #     / ___// / / /__ \    / __ \____ _/ /_____ _/  |/  (_)___  ___  _____   #        #
#       #     \__ \/ / / /__/ /   / / / / __ `/ __/ __ `/ /|_/ / / __ \/ _ \/ ___/   #        #
#       #    ___/ / /_/ // __/   / /_/ / /_/ / /_/ /_/ / /  / / / / / /  __/ /       #        #
#       #   /____/\____//____/  /_____/\__,_/\__/\__,_/_/  /_/_/_/ /_/\___/_/        #        #
#       #                                                                            #        #
###############################################################################################

################################ FILE NAME: Config_base.py ####################################
#=============================================================================================#
# author: Evert Bunschoten                                                                    |
#    :PhD Candidate ,                                                                         |
#    :Flight Power and Propulsion                                                             |
#    :TU Delft,                                                                               |
#    :The Netherlands                                                                         |
#                                                                                             |
#                                                                                             |
# Description:                                                                                |
#  Base class for DataMiner configuration                                                     |
#                                                                                             |
# Version: 1.0.0                                                                              |
#                                                                                             |
#=============================================================================================#
import os 
import pyfiglet
import pickle
from Common.Properties import DefaultProperties 

class Config:
    """!
    @brief Base class for DataMiner configurations.


    """
    
    __banner_header = "SU2 DataMiner"
    _output_dir:str = "./"
    _config_name:str = "config"

    __concatenated_file_header:str=DefaultProperties.output_file_header
    __train_fraction:float = DefaultProperties.train_fraction
    __test_fraction:float = DefaultProperties.test_fraction
    _controlling_variables:list[str]

    _alpha_expo:float = DefaultProperties.init_learning_rate_expo
    _lr_decay:float = DefaultProperties.learning_rate_decay
    _batch_expo:int = DefaultProperties.batch_size_exponent
    _hidden_layer_architecture:list[int] = DefaultProperties.hidden_layer_architecture
    _activation_function:str = DefaultProperties.activation_function

    def __init__(self):
        """!
        @brief Class constructor

        """
        self._output_dir = os.getcwd()
        return 
    
    def PrintBanner(self):
        """!
        @brief Print information about the DataMiner configuration that describe the fluid data set and manifold configuration settings.

        """
        customfig = pyfiglet.Figlet(font="slant")
        print(customfig.renderText(self.__banner_header))
        return 
    
    def SetOutputDir(self, output_dir:str):
        """!
        @brief Define the fluid data output directory. This directory is set as the default storage directory for all storage processes in the DataMiner workflow.

        Parameters : 
            @param output_dir : str => storage directory.

        Exceptions :
            @exception Exception if specified directory does not exist on the current hardware.
        """
        if not os.path.isdir(output_dir):
            raise Exception("Invalid output data directory")
        else:
            self._output_dir = output_dir
        return 
    
    def GetOutputDir(self):
        """!
        @brief Get the current DataMiner configuration fluid storage directory.

        Exceptions:
            @exception Exception if the storage directory in the current configuration class is not present on the current hardware.

        """
        if not os.path.isdir(self._output_dir):
            raise Exception("Saved output directory not present on current machine.")
        else:
            return self._output_dir
    
    def SetConcatenationFileHeader(self, header:str=DefaultProperties.output_file_header):
        """!
        @brief Define the file name header for the collection of fluid data.

        Parameters : 
            @param header : str = DefaultProperties.output_file_header => file name header.

        """
        self.__concatenated_file_header = header 
        return 
    
    def GetConcatenationFileHeader(self):
        """!
        @brief Get the file name header for the fluid collection file.

        Returns :
            @return fluid data collection file header.
        """
        return self.__concatenated_file_header
    
    def SetConfigName(self, config_name:str):
        self._config_name = config_name 
        return 
    
    def GetConfigName(self):
        """!
        @brief [Function's description]

        Parameters : 
            @param self => [description]

        """
        return self._config_name 
    
    def SetControllingVariables(self, names_cv:list[str]):
        self._controlling_variables = []
        for c in names_cv:
            self._controlling_variables.append(c)
        return 
    
    def GetControllingVariables(self):
        return self._controlling_variables
    
    def SetTrainFraction(self, input:float=DefaultProperties.train_fraction):
        """!
        @brief [Function's description]

        Parameters : 
            @param self => [description]
            @param input : float = DefaultProperties.train_fraction => [description]

        """
        """
        Define the fraction of fluid data used for training multi-layer perceptrons.

        :param input: fluid data train fraction.
        :type input: float 
        :raise: Exception: if provided fraction is equal or higher than one.
        """
        if input >= 1:
            raise Exception("Training data fraction should be lower than one.")
        self.__train_fraction = input 
        return 
    
    def SetTestFraction(self, input:float=DefaultProperties.test_fraction):
        """!
        @brief [Function's description]

        Parameters : 
            @param self => [description]
            @param input : float = DefaultProperties.test_fraction => [description]

        """
        """
        Define the fraction of fluid data separate from the training data used for determining accuracy after training.

        :param input: fluid data test fraction.
        :type input: float
        :raise Exception: if provided fraction is equal or higher than one.
        """
        if input >= 1:
            raise Exception("Test data fraction should be lower than one.")
        self.__test_fraction = input 
        return 
    
    def GetTrainFraction(self):
        """!
        @brief [Function's description]

        Parameters : 
            @param self => [description]

        """
        """
        Get fluid data fraction used for multi-layer perceptron training.

        :return: fluid data train fraction.
        :rtype: float 
        """
        return self.__train_fraction
    
    def GetTestFraction(self):
        """!
        @brief [Function's description]

        Parameters : 
            @param self => [description]

        """
        """
        Get fluid data fraction used for determining accuracy after training.

        :return: fluid data test fraction.
        :rtype: float 
        """
        return self.__test_fraction
    
    def GetAlphaExpo(self):
        return self._alpha_expo
    
    def SetAlphaExpo(self, alpha_expo_in:float=DefaultProperties.init_learning_rate_expo):
        """Set initial learning rate decay parameter.

        :param alpha_expo: initial learning rate exponent (base 10), defaults to -2.6
        :type alpha_expo: float, optional
        :raises Exception: if initial learning rate exponent is positive.
        """

        if alpha_expo_in >= 0:
            raise Exception("Initial learning rate exponent should be negative.")
        self._alpha_expo = alpha_expo_in
        return 
    
    def GetLRDecay(self):
        return self._lr_decay
    
    def SetLRDecay(self, lr_decay_in:float=DefaultProperties.learning_rate_decay):
        self._lr_decay = lr_decay_in
        return 
    
    def SetBatchExpo(self, batch_expo_in:int=DefaultProperties.batch_size_exponent):
        self._batch_expo = batch_expo_in
        return 
    
    def GetBatchExpo(self):
        return self._batch_expo 
    
    def SetHiddenLayerArchitecture(self, hidden_layer_architecture:list[int]=DefaultProperties.hidden_layer_architecture):
        self._hidden_layer_architecture = []
        for n in hidden_layer_architecture:
            self._hidden_layer_architecture.append(n)
        return 
    def GetHiddenLayerArchitecture(self):
        return self._hidden_layer_architecture
    
    def SetActivationFunction(self, activation_function_in:str):
        self._activation_function = activation_function_in 
        return 
    
    def GetActivationFunction(self):
        return self._activation_function
    
    def SaveConfig(self):
        """
        Save the current FlameletAI configuration.

        :param file_name: configuration file name.
        :type file_name: str
        """

        file = open(self._config_name+'.cfg','wb')
        pickle.dump(self, file)
        file.close()
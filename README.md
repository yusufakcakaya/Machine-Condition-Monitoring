# Machine Condition Monitoring 🎰

***

### Mission

The company has collected audio samples of equipment working on normal and anomalous conditions. Their objective is to develop a machine learning model able to monitor the operations and identify anomalies in the sound pattern. The sounds are related with some machines like fan, pump, valve and slider.In this project, it is aimed to find an optimal solution using supervised machine learning and deep learning models. The implementation of this model can allow companies to operate the manufacturing equipment at full capacity and detect signs of failure before the damage is so critical that the production line has to be stopped.

![image](https://user-images.githubusercontent.com/46165841/156190888-7140d771-0cb0-4132-a529-a30c04a524cd.png)

While categorizing the properties of audio files, we know that there are various levels and abstraction.
**High level:** These are the level that can be heard and not disturbed by humans. These can be instrumentation, key, chords, melody, harmony, rhythm.
**Intermediate:** These we may have trouble perceiving. These include pitch, beat- related identifiers, note beginnings, ripple patterns, MFCCs, etc.
**Low level:** These contain features that humans cannot understand but can only be achieved with the help of machinery. Examples include amplitude envelope,energy, spectral center, spectral flux, zero crossing ratio, etc.

When we look at waveforms with frequency domain, we can extract band energy ratio, spectral centroid, and spectral flux properties with the help of Fourier Transform.As a result of our research, the features that are important to us are included in the domains I have listed above, and it has been observed that all of them can be accessed at the same time with the Time- frequency representation that includes each of these domains. Mel spectogram will be created with the help of the Short-Time Fourier Transform (STFT) and the desired properties will be obtained from here.

![image](https://user-images.githubusercontent.com/46165841/158340766-f1ef6ee4-12ae-44e9-ab99-494f38e3a11a.png)

Humans perceive sounds logarithmically. When the sound frequency range is high, it is easy for us to notice these sounds. For example, if we give an example, we can easily detect the difference between 300 hz and 700 hz, but it will not be easy to make this distinction when this range increases from 10000 to 20000. While making this distinction, the mel spectogram is used. The sounds we will be working with are machine sounds and in some places it will be almost difficult to tell the difference. Therefore, while designing the model, using a system separated according to their characteristics, not a human being who distinguishes sounds, indicates that it will be very effective in solving the sample problem. Mel-spectrogram is a spectrogram in which frequencies are converted to mel scale.

#### Which dataset?

Orijinal dataset can be downloaded on the following link:

- [Machine Condition Monitoring](https://zenodo.org/record/3384388#.YFIrNXnvJEY)

***
### Mission objectives

Week 1
- Be able to work and process data from audio format
- Find insights from data
- Get data and save features to csv
- Build machine learning models for predictive classification and/or regression
- Select the right performance metrics for model
- Evaluate the distribution of data points and evaluate its influence in the model
- Be able to identify underfitting or overfitting that might exist on the model

Week 2
- Tuning parameters of the model for better performance
- Build CNN model for classification(from numpy array)
- Build CNN model for classification(from png)
- Evaluate the model
- Be able to identify underfitting or overfitting that might exist on the model
- Save model
- Model prediction

Week 3
- Deployment


## Installation

- Pull requests are welcome.
- or ```https://github.com/yusufakcakaya/Machine-condition-monitoring.git```




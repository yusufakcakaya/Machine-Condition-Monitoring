# Machine Condition Monitoring 🎰

***

### Mission

  The company has collected audio samples of equipment working on normal and anomalous conditions. Their objective is to develop a machine learning model able to monitor the operations and identify anomalies in the sound pattern. The sounds are related with some machines like fan, pump, valve and slider.In this project, it is aimed to find an optimal solution using supervised machine learning and deep learning models. The implementation of this model can allow companies to operate the manufacturing equipment at full capacity and detect signs of failure before the damage is so critical that the production line has to be stopped.

![image](https://user-images.githubusercontent.com/46165841/156190888-7140d771-0cb0-4132-a529-a30c04a524cd.png)

  While categorizing the properties of audio files, we know that there are various levels and abstraction.
- **High level:** These are the level that can be heard and not disturbed by humans. These can be instrumentation, key, chords, melody, harmony, rhythm.
- **Intermediate:** These we may have trouble perceiving. These include pitch, beat- related identifiers, note beginnings, ripple patterns, MFCCs, etc.
- **Low level:** These contain features that humans cannot understand but can only be achieved with the help of machinery. Examples include amplitude envelope,energy, spectral center, spectral flux, zero crossing ratio, etc.

  When we look at waveforms with frequency domain, we can extract band energy ratio, spectral centroid, and spectral flux properties with the help of Fourier Transform.As a result of our research, the features that are important to us are included in the domains I have listed above, and it has been observed that all of them can be accessed at the same time with the Time- frequency representation that includes each of these domains. Mel spectogram will be created with the help of the Short-Time Fourier Transform (STFT) and the desired properties will be obtained from here.

![image](https://user-images.githubusercontent.com/46165841/158340766-f1ef6ee4-12ae-44e9-ab99-494f38e3a11a.png)

  Humans perceive sounds logarithmically. When the sound frequency range is high, it is easy for us to notice these sounds. For example, if we give an example, we can easily detect the difference between 300 hz and 700 hz, but it will not be easy to make this distinction when this range increases from 10000 to 20000. While making this distinction, the mel spectogram is used. The sounds we will be working with are machine sounds and in some places it will be almost difficult to tell the difference. Therefore, while designing the model, using a system separated according to their characteristics, not a human being who distinguishes sounds, indicates that it will be very effective in solving the sample problem. Mel-spectrogram is a spectrogram in which frequencies are converted to mel scale.

Three different approaches were followed:

1. **Supervised Machine Learning :**

  - Logistic Regression
  - KNN
  - SVM
  - Decision Tree
  - Random Forest
  - Naive Bayes
  
According to the model results, it is observed that the most suitable model for our data set is Random Forest and KNN.

```
Classification Report Random Forest: 
               precision    recall  f1-score   support

           0       0.91      0.98      0.95       816
           1       0.94      0.74      0.83       294

    accuracy                           0.92      1110
   macro avg       0.93      0.86      0.89      1110
weighted avg       0.92      0.92      0.92      1110

```

```
Classification Report KNN:
               precision    recall  f1-score   support

           0       0.92      0.97      0.94       816
           1       0.89      0.76      0.82       294

    accuracy                           0.91      1110
   macro avg       0.90      0.86      0.88      1110
weighted avg       0.91      0.91      0.91      1110

```




2. **Transfer learning** - Convolutional neural networks (CNN) - Takes in an image and uses existing pretrained model `VGG16` to predict  normal or abnormal.

```
 precision    recall  f1-score   support

    Abnormal       0.95      0.99      0.97        84
      Normal       0.99      0.96      0.97        93

    accuracy                           0.97       177
   macro avg       0.97      0.97      0.97       177
weighted avg       0.97      0.97      0.97       177

```

![download](https://user-images.githubusercontent.com/46165841/158364392-9d835226-d167-4406-8250-8897dcd8152e.png)

![download (1)](https://user-images.githubusercontent.com/46165841/158364417-cbc642d0-7331-4475-85c1-8cfdadbd2a56.png)

#### Which dataset?

Orijinal dataset can be downloaded on the following link:

- [Machine Condition Monitoring](https://zenodo.org/record/3384388#.YFIrNXnvJEY)

***
### Visuals

Here are sample visuals:
#### KNN ROC
![download (3)](https://user-images.githubusercontent.com/46165841/158364490-966e9e18-4a4e-4005-912d-9e2bb2ec1eb3.png)


#### Random Forest ROC
![download (2)](https://user-images.githubusercontent.com/46165841/158364447-cd2793ab-197c-477c-8d3d-247f5470d6e8.png)

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


***
### Timeline
Mar 2022



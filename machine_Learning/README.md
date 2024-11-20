## Galaxy Collapse - Description

### Dataset

The model is trained from [Galaxy Zoo (GalaxyZoo1_DR_table2.csv)](https://data.galaxyzoo.org/). The dataset has been preprocessed, cleaned and altered for the purpose of this challenge. **While taking a look at the dataset might be helpful, you do NOT need to use the original dataset to solve this challenge.**

### Objective

The model is a binary classification model that predicts if a galaxy is spiral or elliptical. First class is spiral and second class is elliptical.

In this challenge, you will be given 20 random data points representing 20 galaxies. Each data point has 10 dimensions: `NVOTE,P_EL,P_CW,P_ACW,P_EDGE,P_DK,P_MG,P_CS,P_EL_DEBIASED,P_CS_DEBIASED`. They are ordered in exactly the same way as the model was trained.

Your goal is to correctly predict the class of each galaxy. Connect to remote server for more guidance.
# RaySAttack Project
RayS Attack(https://arxiv.org/abs/2006.12792) ran on 50 samples from the validation set of CIFAR-10 dataset on pretrained victim model ViT-L-16

The project aimed to run the RayS black-box attack using 50 samples from the validation set of CIFAR-10 on a classifier of my choice, with additional code and information listed below

  • RayS attack code here: https://github.com/MetaMain/ViTRobust/blob/main/VisionTransformersRobustness/VisionTransformersRobustness/AttackWrappersRayS.py 
  • Example of how you'd run RayS attack on a model here: https://github.com/MetaMain/ViTRobust/blob/main/VisionTransformersRobustness/VisionTransformersRobustness/DefaultMethods.py  
  • Pre-trained classifiers here under the model section: https://github.com/MetaMain/ViTRobust 

Important Note: The code in this repository has the original root code from https://github.com/MetaMain/ViTRobust, modifications were made mainly in RayS.ipynb and generateImage.py

# Step by Step Guide

1. Install the packages listed in the Software Installation Section
2. Clone this repository and create a folder named "Models"
3. Download the ViT-L-16 here: https://drive.google.com/drive/folders/1VpbvFPAKMw4mpRJRblJcTwwIsC5A_A0r and place it in the "Models" folder
4. Open and run RayS.ipynb

# Software Installation

• pytorch==1.7.1  

• torchvision==0.8.2

• numpy==1.19.2 

• opencv-python==4.5.1.48 

• ml_collections

# Contact 

Please feel free to contact me at ziyimeng@brandeis.edu for discussions and questions

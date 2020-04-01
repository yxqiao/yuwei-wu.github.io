---
layout: post
title: Embryos 3D Images Transfer
date: 2020-02-16
Author: Yuwei Wu
categories: 
tags: [Porjects]
comments: true
toc: true
---




# Embryos-3D-Images-Transfer

This is a idea for auto match of chicken embryos 3D images. I do not have the medical knowledge and backgrounds so some parts of it include more details of terms and notions.


## 1.Problem Statement

The research is about to analysis the cardiac development under the influence of different genes. The process from CT to 3D has been done and our task is to rotate or say registrate the images to keep its consistent orentation of the heart so that the pathologists will find it easier to analyze the phenotype of the egg. The challenge is that the embroyo's 3D images are develop with it grows and the embryos can move in the egg so that the 3D match objects are not the same in each stage.(more specific details of its movement and development can be seen in <a href="#1" >[1]</a>  )


### 1.1 Some Explanation of the Items

#### (1) long axis of heart

Because the development of the embryos changes with time, the long axis orientation of heart also varies.

<img width="400" height="300" src="https://image.slidesharecdn.com/cardiacus-090930141613-phpapp02/95/cardiac-us-16-728.jpg?cb=1254320229"/>

### 1.2. Input Data

- (1) CT images

The images from micro CT. 

- (2) some labeled images from pathologists

Some couples of images, one is the original image, and the other is the processed images with correct orientation. So this question can be regarded as the supervised learning problems with input of images and output of transformed matrix or output images.

## 2.Assumptions

- (1) CT pictures has the enough precision (we use micro-CT)

- (2) The impact of motion artifacts and other artifacts has been reduced. 

<a href="#2" >[2]</a> has demonstrate how the motion artifact influence our images. It's assumed that some pictures with many artifacts have been remove and the images is not blur to influence the work of pathologists.  

- (3) The chicken embryos are in Ovo and in vivo

According to the question, they need to determine phenotype of each egg, so it's the case that we observe embryos in the eggshell and in vivo so that they may have movements. There are some [experiments](https://abt.ucpress.edu/content/74/9/628) as ex ovo and the observation is not quite similar.

- (4) The labeled data are well distributed.

It means the labeled data cover the whole developmenet process of the embryo. Because the phenotype of chicken embryos changed dramatically if we lost some stages of this development, it may cause error with the use of labeled data. Also, we can consider the labeled data as ground truth (the labeled data has been filtraded). If the learning diffcults of the images are not well distributed, there are some strategies as imbalance sampling.

- (5) The missing data, error images have been removed. (all data is valid)

Just to make this question more spefific and only focus on the algorithms (in actual industrial field, it is often the case to have error input data). If the data has not been prepocessing, we can just write some scripts to check and select the valid data.

- (6) The rotation is rigid transformation.

## 3. Learning to Rotate

Actually for the traditional method, we can define the axis of heart in the images, learn the features and use some match algorithms to match it to the correct orientation. Due to the fact that we have labeled data, so we can use these to train our network and then get the rotation. 

### 3.1 Preprocessing

#### 3.1.1 Clean and Filter Data 

If the images are not as perfect as our assumptions, we need to clean and reconstruct the data first. There's something we can do:
- Check the scale, size or other information of the images.
- Remove some images if they do not contain useful info.
- If needed, apply some filters to process the data.

#### 3.1.2 Input and Output Forms

  - Deal with 3D Images

There are usually two ways to deal with 3D detection problem. Firstly we can reconstruct from the 3T images to 3D structures or we use only the 2D features and put it in our network.

  - (1) object reconstruction

In the problem description, they get the resulting 3d images and then do some rotations. We can use many tools with a lot of reconstruction algorithms to build the 3D images, such as the ASTRA Toolbox. Or, as there are a lot of types of medical images as dcm，nii.gz，nrrd，mha，mhd and we use dcm pydicom to get access to dcm data and itk to process it. Also, we can get the rotation information by calculate the rotation matrix from the orignal images and processed images 

  - (2) using 2D features.

According to this paper [Is 2D Information Enough For ViewpointEstimation?](http://www.bmva.org/bmvc/2014/files/paper048.pdf), we can also explore for our specific case, whether it's better to only use the 3T slices.

- Output Form

- (1) 3D Orientation
yaw, pitch, and roll, then we can use the pose to correct our 3D images to the right and consistent orientation.

- (2) rotated view

3D images(it may not be very practical)

#### 3.1.3 Data Augmentation

It depends on our demand and the quality of data.

#### 3.1.4 Background Segementation

Because the position of the heart in the embryo can change and not proper to match the whole 3D image of the embryo, therefore we can try to analyze the performance that extract or partition the cardiac part and then match it. (Matlab also has the segementation toolbox)

### Related Work
[RotNet](https://github.com/d4nst/RotNet): application on 2D rotation correctness (CNN)
[SSD-6D](https://github.com/wadimkehl/ssd-6d) interesting one to set the orientation estimation as the classification problem.

I don't do relevant work about medical data before, because the network should be fit to the case, I find that U-Net is quite popular in Biomedical field, maybe we can start at it as a baseline. [U-Net: Convolutional Networks for BiomedicalImage Segmentation](https://arxiv.org/pdf/1505.04597.pdf)

### 3.3 Train and Tune the Model

The strategies that should be used really depends. Firstly we need to see the performance of the it using pretrained model and then figure out how to tune the parameters or revise the network.

### 3.4 Evaluation

This process is necessary for us to create a evaluation metric for the rotation result. For this case, because the target is very obvious, we can use the rotation ratio as our evaluation metrics.

## 4.Conclusion

## 5.Other Discussion

Last year, kaggle has a competition [RSNA Intracranial Hemorrhage Detection](https://www.kaggle.com/c/rsna-intracranial-hemorrhage-detection/) that use the 3D images to build an algorithm to detect acute intracranial hemorrhage. I do not research more about the types of heart disease and mutation. But maybe the presence and degree of cardiac abnormalities can also be labeled and we can directly use these and machine learning method to process more images.

## 6.Informal Reference

<a id="1"/> 1.[Embryonic development of Columba livia(Aves: Columbiformes) from an altricial-precocial perspective](https://www.researchgate.net/publication/260764808_Embryonic_development_of_Columba_liviaAves_Columbiformes_from_an_altricial-precocial_perspective)

<a id="2"/> 2.[Motion-Artifact-Free In Vivo Imaging Utilizing Narcotized Avian Embryos In Ovo](https://www.researchgate.net/publication/44677254_Motion-Artifact-Free_In_Vivo_Imaging_Utilizing_Narcotized_Avian_Embryos_In_Ovo)


<a id="3"/> 3.[Quantitative Three-DimensionalAnalysis of Embryonic ChickMorphogenesis Via MicrocomputedTomography](https://anatomypubs.onlinelibrary.wiley.com/doi/pdf/10.1002/ar.21276)

<a id="4"/> 4.[Automated Segmentation and Object Classification ofCT Images: Application toIn VivoMolecular Imaging ofAvian Embryos](http://downloads.hindawi.com/journals/ijbi/2013/508474.pdf)

5.[Automatic Photo Orientation Detection with Convolutional Neural Networks](https://www.cs.toronto.edu/~guerzhoy/oriviz/crv17.pdf)

6.[3D ShapeNets: A Deep Representation for Volumetric Shapes](https://vision.princeton.edu/projects/2014/3DShapeNets/paper.pdf)

7.[Kaggle competition Autonomous Driving: predict vehicle angle in different settings](https://www.kaggle.com/c/pku-autonomous-driving)


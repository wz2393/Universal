# Universal Style Transfer

This project is based on the paper [Universal Style Transfer via Feature Transforms.](https://arxiv.org/pdf/1705.08086.pdf) and our target is to reproduce the algorithm. The key idea is to train a encoder(Vgg-19 in this project and we use a pre-trained one) to extract features and build a 4 different level decoders to reconstruct the image. Between the encoder and the decoders we apply a WCT layer in order to: 1)implement SVD on original content and style images; 2)whitening and coloring; 3)reconstruct the image with blended features depending on parameter alpha.

![image](network.png)

## Samples
<div align=center><img width="244" height="244" src="data/content/028.jpg" >
<img width = "244" height="244" src ="data/style/088.jpg">
<img width = "244" height="244" src="data/output/028_088_trensferred.jpg">
<br>
<img width="244" height="244" src="data/content/05.jpg" >
<img width = "244" height="244" src ="data/style/09.jpg">
<img width = "244" height="244" src="data/output/05_09_trensferred.jpg">
<br>
<img width="244" height="244" src="data/content/028.jpg" >
<img width = "244" height="244" src ="data/style/088.jpg">
<img width = "244" height="244" src="data/output/028_088_trensferred.jpg">
 <br> 
 <div align=left>  

## Different Style Weight

We set alpha = 0.2, 0.4, 0.6, 0.8, 1.0 to observe the difference.
<div align=center><img width="244" height="244" src="data/content/004.jpg" >
<img width = "244" height="244" src ="data/output/004_s5_trensferred2.jpg">
<img width = "244" height="244" src="data/output/004_s5_trensferred4.jpg">
<br>
<img width="244" height="244" src="data/output/004_s5_trensferred6.jpg" >
<img width = "244" height="244" src ="data/output/004_s5_trensferred8.jpg">
<img width = "244" height="244" src="data/output/004_s5_trensferred10.jpg">
 <br> 
 <div align=left>  

## Different Scale
Difference between original scale and 1/3 original scale.
<div align=center><img width="244" height="244" src="data/content/04.jpg" >
<img width = "244" height="244" src ="data/output/04_brick1_trensferred1.jpg">
<img width = "244" height="244" src="data/output/04_brick1_trensferred2.jpg">
 <br> 
 <div align=left>

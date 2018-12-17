# Universal Style Transfer

This project is based on the paper [Universal Style Transfer via Feature Transforms.](https://arxiv.org/pdf/1705.08086.pdf) and our target is to reproduce the algorithm. The key idea is to train a encoder(Vgg-19 in this project and we use a pre-trained one) to extract features and build a 4 different level decoders to reconstruct the image. Between the encoder and the decoders we apply a WCT layer in order to: 1)implement SVD on original content and style images; 2)whitening and coloring; 3)reconstruct the image with blended features depending on parameter alpha.

![image](network.png)

## Samples
<div align=center><img width="244" height="244" src="data/content/028.jpg" >
<img width = "244" height="244" src ="data/style/088.jpg">
<img width = "244" height="244" src="data/output/028_088_trensferred.jpg">
<br>
<img width="244" height="244" src="https://github.com/zhangcliff/WCT-based-style-transfer/blob/master/content/im2.jpg" >
<img width = "244" height="244" src ="https://github.com/zhangcliff/WCT-based-style-transfer/blob/master/style/s2.jpg">
<img width = "244" height="244" src="https://github.com/zhangcliff/WCT-based-style-transfer/blob/master/result/result_3.jpg">
<br>
<img width="244" height="244" src="https://github.com/zhangcliff/WCT-based-style-transfer/blob/master/content/im3.jpg" >
<img width = "244" height="244" src ="https://github.com/zhangcliff/WCT-based-style-transfer/blob/master/style/s3.jpg">
<img width = "244" height="244" src="https://github.com/zhangcliff/WCT-based-style-transfer/blob/master/result/result_4.jpg">
<br>
<img width="244" height="244" src="https://github.com/zhangcliff/WCT-based-style-transfer/blob/master/content/im1.jpg" >
<img width = "244" height="244" src ="https://github.com/zhangcliff/WCT-based-style-transfer/blob/master/style/s1.jpg">
<img width = "244" height="244" src="https://github.com/zhangcliff/WCT-based-style-transfer/blob/master/result/result_2.jpg">
 <br> 
 <div align=left>  
 ## 

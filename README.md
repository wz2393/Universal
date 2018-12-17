# Universal Style Transfer

This project is based on the paper [Universal Style Transfer via Feature Transforms.](https://arxiv.org/pdf/1705.08086.pdf) and our target is to reproduce the algorithm. The key idea is to train a encoder(Vgg-19 in this project and we use a pre-trained one) to extract features and build a 4 different level decoders to reconstruct the image. Between the encoder and the decoders we apply a WCT layer in order to: 1)implement SVD on original content and style images; 2)whitening and coloring; 3)reconstruct the image with blended features depending on parameter alpha.

![image](network.png)

## Samples
<div align=center><img width="244" height="244" src="https://github.com/zhangcliff/WCT-based-style-transfer/blob/master/content/im4.jpg" >
<img width = "244" height="244" src ="https://github.com/zhangcliff/WCT-based-style-transfer/blob/master/style/s5.jpg">
<img width = "244" height="244" src="https://github.com/zhangcliff/WCT-based-style-transfer/blob/master/result/result_1.jpg">
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
  
## Test
1 download the pre-trained vgg19 weights [VGG19](https://pan.baidu.com/s/1zpsUu-V9taVBoaqBLK_OuQ)
 <br>
2 download the 4 trained decoders [weights](https://pan.baidu.com/s/1wencvm0bESOU_s5k2wRmYQ)
```shell
mkdir models
```
and put the trained decoders weights to models folder
 <br>
Then run :
```shell
python test_all_layer.py --content_path /path/to/content_img --style_path /path/to/style_img  --output_path /path/to/result_img --pretrained_vgg path/to/vgg19 --alpha 1
 ```
## Train
1 download the content images from [coco](http://msvocds.blob.core.windows.net/coco2014/train2014.zip)
<br>
2 make tfrecord file 
```shell
mkdir tfrecords
python gen_tfrecords.py
```
<br>
3 we need to train decoders for layer relu1-4 seprartely. For example, if we want to train decoder for relu4 , wo can run as :

```shell
python train.py --target_layer relu4 --pretrained_path path/to/vgg19 --max_iterator 20000 --checkpoint_path path/to/save_checkpoint --tfrecord_path path/to/tfrecord  --batch_size 8
```

## Reference
1、[https://github.com/eridgd/WCT-TF](https://github.com/eridgd/WCT-TF)

2、[https://github.com/machrisaa/tensorflow-vgg](https://github.com/machrisaa/tensorflow-vgg)
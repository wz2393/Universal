from model.wct_model import WCT_test
from model.img_utils import load_img
import matplotlib.pyplot as plt
import time
# parameters
pretrained_vgg_path = 'model/model_data/vgg19.npy'
content_path = 'data/content/04.jpg'
style_path = 'data/style/antimonocromatismo.jpg'
output_path = 'data/output/04_trensferred3.jpg'
alpha = 0.5
    
def transfer_picture(pretrained_vgg_path,
                     content_path,
                     style_path,
                     output_path,
                     alpha,
                     scale):
    model = WCT_test(
                     pretrained_vgg = pretrained_vgg_path,
                     content_path = content_path,
                     style_path = style_path,
                     output_path = output_path,
                     alpha = alpha,
                     scale = scale
                     )
    startT = time.time()
    model.transfer()
    endT = time.time()
    costT = endT - startT
    img = load_img(output_path)
    plt.imshow(img/255)
    plt.show()
    print('Transfer done! Cost {} secs with Surface Pro 4.'.format(costT))
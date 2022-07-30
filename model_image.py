import torch
import torch.nn as nn
from PIL import Image
from pathlib2 import Path
import torchvision
from torchvision import transforms
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import matplotlib.pyplot as plt


label_dict = {'acer': 39,'adidas': 35,'adobe': 30,'amazon': 31,'android': 34,'apple': 36,'bose': 38,'coca-cola': 33,'dell': 37,'disney': 32,'gap': 24,
'google': 26,'gucci': 28,'hp': 29,'intel': 27,'kelloggs': 21,'kit-kat': 20,'lays': 22,'lego': 23,'lenovo': 25,'louis-vuitton': 13,'maggi': 16,
'mirinda': 12,'nike': 18,'nissan': 14,'nokia': 10,'oppo': 17,'oreo': 11,'panasonic': 19,'pepsi': 15,'playstation': 2,
'polo': 5,'reebok': 0,'samsung': 6,'sony': 4,'sprite': 8,'unilever': 9,'victoria-secret-pink': 7,'visa': 3,'yamaha': 1}

number_dict = dict((v,k) for k,v in label_dict.items())

device = 'cpu'

detector = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
num_classes = 2
in_features = detector.roi_heads.box_predictor.cls_score.in_features
detector.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
detector.to(device)
detector.load_state_dict(torch.load(
    "resnet.pth", map_location=torch.device('cpu')))
detector.eval()

class ClassifierModel(nn.Module):
    def __init__(self,backbone):
        super().__init__()
        self.backbone = backbone
        self.loss = nn.CrossEntropyLoss()
        self.normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

    def forward(self,ref,ind=None):
        B,C,H,W = ref.shape
        ref=ref/255.0
        ref = self.normalize(ref)
        pred_ref = self.backbone(ref)
        if self.training:
            loss = self.loss(pred_ref,ind)
            return loss
        else:
            return int(torch.argmax(pred_ref).numpy())


backbone = torchvision.models.resnet50(pretrained=True)
backbone.fc = nn.Linear(2048, 40)
backbone.to(device)
Classify = ClassifierModel(backbone)
Classify.to(device)
Classify.load_state_dict(torch.load(
    "Classifier.pth", map_location=torch.device('cpu')))
Classify.eval()


def get_detected_image(tensor,model):
    preds = model(tensor)
    ind=torchvision.ops.nms(preds[0]['boxes'],preds[0]['scores'],0)
    ind = ind.tolist()
    preds[0]['boxes'] = preds[0]['boxes'][ind]
    preds[0]['scores'] = preds[0]['scores'][ind]
    maxa = torch.argmax(preds[0]['scores'])
    preds[0]['boxes'] = preds[0]['boxes'][maxa].unsqueeze(0)
    xmin,ymin,xmax,ymax = preds[0]['boxes'][0][0],preds[0]['boxes'][0][1],preds[0]['boxes'][0][2],preds[0]['boxes'][0][3]
    xmin,ymin,xmax,ymax = int(xmin),int(ymin),int(xmax),int(ymax)
    tensor = tensor[:,:,xmin:xmax,ymin:ymax]
    tensor = transforms.Resize((256,256))(tensor)
    return tensor


def predict_image(pil_img,model):
    img = transforms.ToTensor()(pil_img).type(torch.FloatTensor)
    img = transforms.Resize((256,256))(img)
    img = img.unsqueeze(0)
    img = get_detected_image(img,detector)
    pred_ind = model(img)
    return number_dict[pred_ind]

if __name__ == '__main__':
    img = Image.open("google.png").convert("RGB")
    print(predict_image(img,Classify))



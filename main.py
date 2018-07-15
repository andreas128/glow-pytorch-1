from builder import build
from vision.datasets import CelebADataset, MNISTDataset
from torchvision import transforms
from train import Trainer
from config import JsonConfig


hparams = JsonConfig("hparams.json")
built = build(hparams, True)
dataset = MNISTDataset("./datasets",
                       transforms.Compose([transforms.CenterCrop(hparams.Data.center_crop),
                                           transforms.Resize(hparams.Data.resize),
                                           transforms.ToTensor()]))
# dataset = CelebADataset("/home/chaiyujin/Downloads/Dataset/CelebA",
#                         transforms.Compose([
#                                            transforms.CenterCrop(hparams.Data.center_crop),
#                                            transforms.Resize(hparams.Data.resize),
#                                            transforms.ToTensor()]))

trainer = Trainer(**built, dataset=dataset, hparams=hparams)
trainer.train()

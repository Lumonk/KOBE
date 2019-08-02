import os
import pickle
import torch
import utils
import yaml
from argparse import Namespace

config = yaml.load(open(r"C:\Users\flitt\Desktop\research\KOBE\configs\aspect_user_knowledge.yaml", "r"))
config = Namespace(**config)


print("loading data...\n")
data = pickle.load(open(config.data + "data.pkl", "rb"))
# retrieve data, due to the problem of path.
data["train"]["length"] = int(data["train"]["length"] * config.scale)
data["train"]["srcF"] = os.path.join(config.data, "train.src.id")
data["train"]["original_srcF"] = os.path.join(config.data, "train.src.str")
data["train"]["tgtF"] = os.path.join(config.data, "train.tgt.id")
data["train"]["original_tgtF"] = os.path.join(config.data, "train.tgt.str")
data["test"]["srcF"] = os.path.join(config.data, "test.src.id")
data["test"]["original_srcF"] = os.path.join(config.data, "test.src.str")
data["test"]["tgtF"] = os.path.join(config.data, "test.tgt.id")
data["test"]["original_tgtF"] = os.path.join(config.data, "test.tgt.str")

if config.knowledge:
    train_set = utils.BiKnowledgeDataset(
        os.path.join(config.data, 'train.supporting_facts'),
        infos=data['train'], char=config.char)
    
    
    valid_set = utils.BiKnowledgeDataset(
        os.path.join(config.data, 'test.supporting_facts'),
        infos=data['test'], char=config.char)
    print(valid_set[4])
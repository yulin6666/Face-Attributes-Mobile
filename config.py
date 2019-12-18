import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # sets device for model and PyTorch tensors

# Model parameters
image_w = 224
image_h = 224
im_size = 224
channel = 3

# Training parameters
num_workers = 1  # for data-loading; right now, only 1 works with h5py
grad_clip = 5.  # clip gradients at an absolute value of
print_freq = 100  # print training/validation stats  every __ batches
checkpoint = None  # path to checkpoint, None if none
loss_ratio = 100

# Data parameters
num_samples = 382401
train_ratio = 0.9
num_train = int(num_samples * train_ratio)
DATA_DIR = 'data'
IMG_DIR = '/Users/yulin9/Documents/project/AI/dataset/CASIA-WebFace'
PARTLY_IMG_DIR = 'data/CASIA-WebFace-test'
pickle_file = DATA_DIR + '/' + 'CASIA-WebFace.pkl'
partly_pickle_file = DATA_DIR + '/' + 'CASIA-WebFace-partly.pkl'
partly_pickle_file_aligned = DATA_DIR + '/' + 'CASIA-WebFace--partly-aligned.pkl'
pickle_file_aligned = DATA_DIR + '/' + 'CASIA-WebFace-aligned.pkl'

# name_list = ['age', 'pitch', 'roll', 'yaw', 'beauty', 'expression', 'face_prob', 'face_shape', 'face_type',
#              'gender', 'glasses', 'race']
name_list = ['beauty']

expression_dict = {0: 'none', 1: 'smile', 2: 'laugh'}
face_shape_dict = {0: 'square', 1: 'oval', 2: 'heart', 3: 'round', 4: 'triangle'}
face_type_dict = {0: 'human', 1: 'cartoon'}
gender_dict = {0: 'female', 1: 'male'}
glasses_dict = {0: 'none', 1: 'sun', 2: 'common'}
race_dict = {0: 'yellow', 1: 'white', 2: 'black', 3: 'arabs'}

# paths of various location

images_path = "./dataset/images/"
annotations_path = "./dataset/annotations/xmls/"
tfrecord_path = 'pets_data.tfrecord'

# classes
classes = ['cat', 'dog']


# Model _Parameters
IMG_SIZE = 416
N_classes = 2
batch_size = 32
prefetch_batch_buffer = 8
learning_rate = 0.001

import torch


class Config:
    device = torch.device("cuda:0")
    # device = torch.device("cpu")

    train_epochs = 15
    batch_size = 128
    learning_rate = 2e-3
    l2_regularization = 1e-6
    learning_rate_decay = 0.99

    user_count = 5541  # Parameter of TransNet-EXT. Got from output of preprocess.py
    item_count = 3568
    review_count = 10  # max review count
    review_length = 80  # max review length
    lowest_review_count = 2  # reviews wrote by a user/item will be delete if its amount less than such value.
    PAD_WORD = '<UNK>'

    kernel_count = 100
    kernel_size = 3

    dropout_prob = 0.5

    cnn_out_dim = 50

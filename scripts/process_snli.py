import os
import jsonlines

train = '/home/hongru/fairseq/snli/snli_1.0_train.jsonl'
valid = '/home/hongru/fairseq/snli/snli_1.0_dev.jsonl'
test = '/home/hongru/fairseq/snli/snli_1.0_test.jsonl'

def preprocess(in_file, pre_file, hyp_file, label):
    pre = open(pre_file, 'w')
    pre.close()
    hyp = open(hyp_file, 'w')
    hyp.close()

    pre = open(pre_file, 'a')
    hyp = open(hyp_file, 'a')
    with jsonlines.open(in_file) as reader:
        for datum in reader:
            if datum['gold_label'] == label:
                pre.write(' '.join(datum['sentence1'].lower()[:-1].split() + ['.'])+'\n')
                hyp.write(' '.join(datum['sentence2'].lower()[:-1].split() + ['.'])+'\n')


dir_ = '/home/hongru/fairseq/snli-tokenized-en-de'
train_pre = 'train.pre'
train_hyp = 'train.hyp'
valid_pre = 'valid.pre'
valid_hyp = 'valid.hyp'
test_pre = 'test.pre'
test_hyp = 'test.hyp'

if not os.path.exists(dir_):
    os.mkdir(dir_)

label = 'entailment'
preprocess(test, os.path.join(dir_, train_pre), os.path.join(dir_, train_hyp), label)
preprocess(test, os.path.join(dir_, valid_pre), os.path.join(dir_, valid_hyp), label)
preprocess(test, os.path.join(dir_, test_pre), os.path.join(dir_, test_hyp), label)

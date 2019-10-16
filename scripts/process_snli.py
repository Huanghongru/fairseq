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
    tot, cnt = 0, 0
    with jsonlines.open(in_file) as reader:
        for datum in reader:
            tot += 1
            if datum['gold_label'] == label:
                cnt += 1
                pre.write(' '.join(datum['sentence1'].lower()[:-1].split() + ['.'])+'\n')
                hyp.write(' '.join(datum['sentence2'].lower()[:-1].split() + ['.'])+'\n')
        print("retrieve {} {} pairs from total {} pairs".format(cnt, label, tot))
    pre.close()
    hyp.close()


dir_ = '/home/hongru/fairseq/examples/translation/snli-tokenized.en-de'
train_pre = 'train.en'
train_hyp = 'train.de'
valid_pre = 'valid.en'
valid_hyp = 'valid.de'
test_pre = 'test.en'
test_hyp = 'test.de'

if not os.path.exists(dir_):
    os.mkdir(dir_)

label = 'contradiction'
preprocess(train, os.path.join(dir_, train_pre), os.path.join(dir_, train_hyp), label)
preprocess(valid, os.path.join(dir_, valid_pre), os.path.join(dir_, valid_hyp), label)
preprocess(test, os.path.join(dir_, test_pre), os.path.join(dir_, test_hyp), label)

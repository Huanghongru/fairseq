
def make_fake(out_file, pre, hyp, label):
    d3,d4,d5,d6,d7,d8 = "()","()","()","()","()","()"
    trg_file = open(out_file, "w")
    trg_file.close()

    trg_file = open(out_file, "a")

    for i in range(len(pre)):
        new_data_line = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (label, pre[i], hyp[i], d3, d4, d5, d6, d7, d8, label)

        trg_file.write(new_data_line)
    trg_file.close()


def get_pre_hyp(in_file):
    pre = []
    hyp = []
    with open(in_file, 'r') as f:
        l = f.readline()
        while l:
            if l[0] == 'S':
                hyp.append(' '.join(l.split()[1:]))
            if l[0] == 'H':
                pre.append(' '.join(l.split()[2:]))
            l = f.readline()
    return pre, hyp

p, h = get_pre_hyp('ent.res')
make_fake('snli_ent.txt', p, h, 'entailment')

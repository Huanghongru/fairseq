fairseq-generate data-bin/snli-tokenized.en-de \
    --path checkpoints/checkpoint_best.pt \
    --batch-size 128 --beam 5 --remove-bpe

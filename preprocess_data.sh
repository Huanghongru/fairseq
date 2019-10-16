TEXT=examples/translation/snli-tokenized.en-de
fairseq-preprocess --source-lang de --target-lang en \
	--trainpref $TEXT/train --validpref $TEXT/valid --testpref $TEXT/test \
	--destdir data-bin/snli-tokenized.en-de \
	--workers 20

Create a poker AI that is an order of magnitude more powerful than monkersolver or gto wizard.
CFR-R-NaD is an implementation of google deep mind's stratego solver
https://arxiv.org/abs/2206.15378


Steps:
1.
run generate random.py.
use this to create terrabytes of pretraining data for your LLM.

2.
create a tokenizer vocabulary, I reccomend translating the output of generate random into discrete tokens as you see fit and adding those discrete tokens to thhe tokenizer generator.
https://github.com/wesboyt/huggingface_onehot_tokenizer_generator/blob/main/generate_onehot_tokenizer.py

3.
define your huggingface config, this decides the model type, shape, and vocabulary size.
https://huggingface.co/Cheng98/llama-39m/blob/main/config.json


4.
copy and run, use help parameter to understand the options.
https://github.com/huggingface/transformers/blob/main/examples/pytorch/language-modeling/run_clm.py

5.
revamp cfr_R-NaD to align with your tokenization structure, Mine is specific to my interpretaton of the simplest possible representation focusing on the smallest onehot token domain possible.





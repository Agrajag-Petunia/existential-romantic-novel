Existential Romantic Novel
=============================

Overview
--------------

The code provided simply reads in multiple novels from the data directory and builds a markov model with a word size of 3. We then generate text for each chapter using the model. The source material (in the `data` directory) is an assortment of romantic and existentialist novels from project gutenberg (all public domain). I planned on finding more/better source material, but didn't get around to it. The resulting novel is stored in data/novel.txt and is mostly unreadable, but occasionally has amusing sentences.

NOTE: I take no responsiblity for the content of the source novels or the generated text. Read at your own risk (obviously).


Running
----------

Just do `python3.5 run.py` in the repo directory. The `run.py` contains all of the hard coded parameters and some documentation (sorry :(). The `src` directory just contains the `textgenerator.py` which just implements the generic text generation model and `utils.py` which contains some simple text cleaning functions.

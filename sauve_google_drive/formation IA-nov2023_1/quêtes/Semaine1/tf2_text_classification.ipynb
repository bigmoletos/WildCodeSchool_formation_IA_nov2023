{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Ic4_occAAiAT"
   },
   "source": [
    "##### Copyright 2019 The TensorFlow Hub Authors.\n",
    "\n",
    "Licensed under the Apache License, Version 2.0 (the \"License\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "cellView": "both",
    "execution": {
     "iopub.execute_input": "2022-12-14T12:47:13.005311Z",
     "iopub.status.busy": "2022-12-14T12:47:13.004704Z",
     "iopub.status.idle": "2022-12-14T12:47:13.008860Z",
     "shell.execute_reply": "2022-12-14T12:47:13.008279Z"
    },
    "id": "ioaprt5q5US7"
   },
   "outputs": [],
   "source": [
    "# Copyright 2019 The TensorFlow Hub Authors. All Rights Reserved.\n",
    "#\n",
    "# Licensed under the Apache License, Version 2.0 (the \"License\");\n",
    "# you may not use this file except in compliance with the License.\n",
    "# You may obtain a copy of the License at\n",
    "#\n",
    "#     http://www.apache.org/licenses/LICENSE-2.0\n",
    "#\n",
    "# Unless required by applicable law or agreed to in writing, software\n",
    "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
    "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
    "# See the License for the specific language governing permissions and\n",
    "# limitations under the License.\n",
    "# =============================================================================="
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "cellView": "form",
    "execution": {
     "iopub.execute_input": "2022-12-14T12:47:13.011903Z",
     "iopub.status.busy": "2022-12-14T12:47:13.011426Z",
     "iopub.status.idle": "2022-12-14T12:47:13.014658Z",
     "shell.execute_reply": "2022-12-14T12:47:13.014090Z"
    },
    "id": "yCl0eTNH5RS3"
   },
   "outputs": [],
   "source": [
    "#@title MIT License\n",
    "#\n",
    "# Copyright (c) 2017 François Chollet\n",
    "#\n",
    "# Permission is hereby granted, free of charge, to any person obtaining a\n",
    "# copy of this software and associated documentation files (the \"Software\"),\n",
    "# to deal in the Software without restriction, including without limitation\n",
    "# the rights to use, copy, modify, merge, publish, distribute, sublicense,\n",
    "# and/or sell copies of the Software, and to permit persons to whom the\n",
    "# Software is furnished to do so, subject to the following conditions:\n",
    "#\n",
    "# The above copyright notice and this permission notice shall be included in\n",
    "# all copies or substantial portions of the Software.\n",
    "#\n",
    "# THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n",
    "# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n",
    "# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL\n",
    "# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n",
    "# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING\n",
    "# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER\n",
    "# DEALINGS IN THE SOFTWARE."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ItXfxkxvosLH"
   },
   "source": [
    "# Text Classification with Movie Reviews"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "MfBg1C5NB3X0"
   },
   "source": [
    "<table class=\"tfo-notebook-buttons\" align=\"left\">\n",
    "  <td>\n",
    "    <a target=\"_blank\" href=\"https://www.tensorflow.org/hub/tutorials/tf2_text_classification\"><img src=\"https://www.tensorflow.org/images/tf_logo_32px.png\" />View on TensorFlow.org</a>\n",
    "  </td>\n",
    "  <td>\n",
    "    <a target=\"_blank\" href=\"https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/tf2_text_classification.ipynb\"><img src=\"https://www.tensorflow.org/images/colab_logo_32px.png\" />Run in Google Colab</a>\n",
    "  </td>\n",
    "  <td>\n",
    "    <a target=\"_blank\" href=\"https://github.com/tensorflow/hub/blob/master/examples/colab/tf2_text_classification.ipynb\"><img src=\"https://www.tensorflow.org/images/GitHub-Mark-32px.png\" />View on GitHub</a>\n",
    "  </td>\n",
    "  <td>\n",
    "    <a href=\"https://storage.googleapis.com/tensorflow_docs/hub/examples/colab/tf2_text_classification.ipynb\"><img src=\"https://www.tensorflow.org/images/download_logo_32px.png\" />Download notebook</a>\n",
    "  </td>\n",
    "  <td>\n",
    "    <a href=\"https://tfhub.dev/google/collections/nnlm/1\"><img src=\"https://www.tensorflow.org/images/hub_logo_32px.png\" />See TF Hub models</a>\n",
    "  </td>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Eg62Pmz3o83v"
   },
   "source": [
    "This notebook classifies movie reviews as *positive* or *negative* using the text of the review. This is an example of *binary*—or two-class—classification, an important and widely applicable kind of machine learning problem. \n",
    "\n",
    "We'll use the [IMDB dataset](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb) that contains the text of 50,000 movie reviews from the [Internet Movie Database](https://www.imdb.com/). These are split into 25,000 reviews for training and 25,000 reviews for testing. The training and testing sets are *balanced*, meaning they contain an equal number of positive and negative reviews. \n",
    "\n",
    "This notebook uses [tf.keras](https://www.tensorflow.org/api_docs/python/tf/keras), a high-level API to build and train models in TensorFlow, and [TensorFlow Hub](https://www.tensorflow.org/hub), a library and platform for transfer learning. For a more advanced text classification tutorial using `tf.keras`, see the [MLCC Text Classification Guide](https://developers.google.com/machine-learning/guides/text-classification/)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "qrk8NjzhSBh-"
   },
   "source": [
    "### More models\n",
    "[Here](https://tfhub.dev/s?module-type=text-embedding) you can find more expressive or performant models that you could use to generate the text embedding."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Q4DN769E2O_R"
   },
   "source": [
    "## Setup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:47:13.018172Z",
     "iopub.status.busy": "2022-12-14T12:47:13.017685Z",
     "iopub.status.idle": "2022-12-14T12:47:15.776382Z",
     "shell.execute_reply": "2022-12-14T12:47:15.775687Z"
    },
    "id": "2ew7HTbPpCJH"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-12-14 12:47:13.964082: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory\n",
      "2022-12-14 12:47:13.964172: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory\n",
      "2022-12-14 12:47:13.964182: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Version:  2.11.0\n",
      "Eager mode:  True\n",
      "Hub version:  0.12.0\n",
      "GPU is available\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "import tensorflow as tf\n",
    "import tensorflow_hub as hub\n",
    "import tensorflow_datasets as tfds\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "print(\"Version: \", tf.__version__)\n",
    "print(\"Eager mode: \", tf.executing_eagerly())\n",
    "print(\"Hub version: \", hub.__version__)\n",
    "print(\"GPU is\", \"available\" if tf.config.list_physical_devices('GPU') else \"NOT AVAILABLE\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "iAsKG535pHep"
   },
   "source": [
    "## Download the IMDB dataset\n",
    "\n",
    "The IMDB dataset is available on [TensorFlow datasets](https://github.com/tensorflow/datasets). The following code downloads the IMDB dataset to your machine (or the colab runtime):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:47:15.780302Z",
     "iopub.status.busy": "2022-12-14T12:47:15.779567Z",
     "iopub.status.idle": "2022-12-14T12:47:21.355454Z",
     "shell.execute_reply": "2022-12-14T12:47:21.354718Z"
    },
    "id": "zXXx5Oc3pOmN"
   },
   "outputs": [],
   "source": [
    "train_data, test_data = tfds.load(name=\"imdb_reviews\", split=[\"train\", \"test\"], \n",
    "                                  batch_size=-1, as_supervised=True)\n",
    "\n",
    "train_examples, train_labels = tfds.as_numpy(train_data)\n",
    "test_examples, test_labels = tfds.as_numpy(test_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "l50X3GfjpU4r"
   },
   "source": [
    "## Explore the data \n",
    "\n",
    "Let's take a moment to understand the format of the data. Each example is a sentence representing the movie review and a corresponding label. The sentence is not preprocessed in any way. The label is an integer value of either 0 or 1, where 0 is a negative review, and 1 is a positive review."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:47:21.359675Z",
     "iopub.status.busy": "2022-12-14T12:47:21.359151Z",
     "iopub.status.idle": "2022-12-14T12:47:21.362857Z",
     "shell.execute_reply": "2022-12-14T12:47:21.362282Z"
    },
    "id": "y8qCnve_-lkO"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training entries: 25000, test entries: 25000\n"
     ]
    }
   ],
   "source": [
    "print(\"Training entries: {}, test entries: {}\".format(len(train_examples), len(test_examples)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "RnKvHWW4-lkW"
   },
   "source": [
    "Let's print first 10 examples."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:47:21.365670Z",
     "iopub.status.busy": "2022-12-14T12:47:21.365219Z",
     "iopub.status.idle": "2022-12-14T12:47:21.371721Z",
     "shell.execute_reply": "2022-12-14T12:47:21.371183Z"
    },
    "id": "QtTS4kpEpjbi"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([b\"This was an absolutely terrible movie. Don't be lured in by Christopher Walken or Michael Ironside. Both are great actors, but this must simply be their worst role in history. Even their great acting could not redeem this movie's ridiculous storyline. This movie is an early nineties US propaganda piece. The most pathetic scenes were those when the Columbian rebels were making their cases for revolutions. Maria Conchita Alonso appeared phony, and her pseudo-love affair with Walken was nothing but a pathetic emotional plug in a movie that was devoid of any real meaning. I am disappointed that there are movies like this, ruining actor's like Christopher Walken's good name. I could barely sit through it.\",\n",
       "       b'I have been known to fall asleep during films, but this is usually due to a combination of things including, really tired, being warm and comfortable on the sette and having just eaten a lot. However on this occasion I fell asleep because the film was rubbish. The plot development was constant. Constantly slow and boring. Things seemed to happen, but with no explanation of what was causing them or why. I admit, I may have missed part of the film, but i watched the majority of it and everything just seemed to happen of its own accord without any real concern for anything else. I cant recommend this film at all.',\n",
       "       b'Mann photographs the Alberta Rocky Mountains in a superb fashion, and Jimmy Stewart and Walter Brennan give enjoyable performances as they always seem to do. <br /><br />But come on Hollywood - a Mountie telling the people of Dawson City, Yukon to elect themselves a marshal (yes a marshal!) and to enforce the law themselves, then gunfighters battling it out on the streets for control of the town? <br /><br />Nothing even remotely resembling that happened on the Canadian side of the border during the Klondike gold rush. Mr. Mann and company appear to have mistaken Dawson City for Deadwood, the Canadian North for the American Wild West.<br /><br />Canadian viewers be prepared for a Reefer Madness type of enjoyable howl with this ludicrous plot, or, to shake your head in disgust.',\n",
       "       b'This is the kind of film for a snowy Sunday afternoon when the rest of the world can go ahead with its own business as you descend into a big arm-chair and mellow for a couple of hours. Wonderful performances from Cher and Nicolas Cage (as always) gently row the plot along. There are no rapids to cross, no dangerous waters, just a warm and witty paddle through New York life at its best. A family film in every sense and one that deserves the praise it received.',\n",
       "       b'As others have mentioned, all the women that go nude in this film are mostly absolutely gorgeous. The plot very ably shows the hypocrisy of the female libido. When men are around they want to be pursued, but when no \"men\" are around, they become the pursuers of a 14 year old boy. And the boy becomes a man really fast (we should all be so lucky at this age!). He then gets up the courage to pursue his true love.',\n",
       "       b\"This is a film which should be seen by anybody interested in, effected by, or suffering from an eating disorder. It is an amazingly accurate and sensitive portrayal of bulimia in a teenage girl, its causes and its symptoms. The girl is played by one of the most brilliant young actresses working in cinema today, Alison Lohman, who was later so spectacular in 'Where the Truth Lies'. I would recommend that this film be shown in all schools, as you will never see a better on this subject. Alison Lohman is absolutely outstanding, and one marvels at her ability to convey the anguish of a girl suffering from this compulsive disorder. If barometers tell us the air pressure, Alison Lohman tells us the emotional pressure with the same degree of accuracy. Her emotional range is so precise, each scene could be measured microscopically for its gradations of trauma, on a scale of rising hysteria and desperation which reaches unbearable intensity. Mare Winningham is the perfect choice to play her mother, and does so with immense sympathy and a range of emotions just as finely tuned as Lohman's. Together, they make a pair of sensitive emotional oscillators vibrating in resonance with one another. This film is really an astonishing achievement, and director Katt Shea should be proud of it. The only reason for not seeing it is if you are not interested in people. But even if you like nature films best, this is after all animal behaviour at the sharp edge. Bulimia is an extreme version of how a tormented soul can destroy her own body in a frenzy of despair. And if we don't sympathise with people suffering from the depths of despair, then we are dead inside.\",\n",
       "       b'Okay, you have:<br /><br />Penelope Keith as Miss Herringbone-Tweed, B.B.E. (Backbone of England.) She\\'s killed off in the first scene - that\\'s right, folks; this show has no backbone!<br /><br />Peter O\\'Toole as Ol\\' Colonel Cricket from The First War and now the emblazered Lord of the Manor.<br /><br />Joanna Lumley as the ensweatered Lady of the Manor, 20 years younger than the colonel and 20 years past her own prime but still glamourous (Brit spelling, not mine) enough to have a toy-boy on the side. It\\'s alright, they have Col. Cricket\\'s full knowledge and consent (they guy even comes \\'round for Christmas!) Still, she\\'s considerate of the colonel enough to have said toy-boy her own age (what a gal!)<br /><br />David McCallum as said toy-boy, equally as pointlessly glamourous as his squeeze. Pilcher couldn\\'t come up with any cover for him within the story, so she gave him a hush-hush job at the Circus.<br /><br />and finally:<br /><br />Susan Hampshire as Miss Polonia Teacups, Venerable Headmistress of the Venerable Girls\\' Boarding-School, serving tea in her office with a dash of deep, poignant advice for life in the outside world just before graduation. Her best bit of advice: \"I\\'ve only been to Nancherrow (the local Stately Home of England) once. I thought it was very beautiful but, somehow, not part of the real world.\" Well, we can\\'t say they didn\\'t warn us.<br /><br />Ah, Susan - time was, your character would have been running the whole show. They don\\'t write \\'em like that any more. Our loss, not yours.<br /><br />So - with a cast and setting like this, you have the re-makings of \"Brideshead Revisited,\" right?<br /><br />Wrong! They took these 1-dimensional supporting roles because they paid so well. After all, acting is one of the oldest temp-jobs there is (YOU name another!)<br /><br />First warning sign: lots and lots of backlighting. They get around it by shooting outdoors - \"hey, it\\'s just the sunlight!\"<br /><br />Second warning sign: Leading Lady cries a lot. When not crying, her eyes are moist. That\\'s the law of romance novels: Leading Lady is \"dewy-eyed.\"<br /><br />Henceforth, Leading Lady shall be known as L.L.<br /><br />Third warning sign: L.L. actually has stars in her eyes when she\\'s in love. Still, I\\'ll give Emily Mortimer an award just for having to act with that spotlight in her eyes (I wonder . did they use contacts?)<br /><br />And lastly, fourth warning sign: no on-screen female character is \"Mrs.\" She\\'s either \"Miss\" or \"Lady.\"<br /><br />When all was said and done, I still couldn\\'t tell you who was pursuing whom and why. I couldn\\'t even tell you what was said and done.<br /><br />To sum up: they all live through World War II without anything happening to them at all.<br /><br />OK, at the end, L.L. finds she\\'s lost her parents to the Japanese prison camps and baby sis comes home catatonic. Meanwhile (there\\'s always a \"meanwhile,\") some young guy L.L. had a crush on (when, I don\\'t know) comes home from some wartime tough spot and is found living on the street by Lady of the Manor (must be some street if SHE\\'s going to find him there.) Both war casualties are whisked away to recover at Nancherrow (SOMEBODY has to be \"whisked away\" SOMEWHERE in these romance stories!)<br /><br />Great drama.',\n",
       "       b'The film is based on a genuine 1950s novel.<br /><br />Journalist Colin McInnes wrote a set of three \"London novels\": \"Absolute Beginners\", \"City of Spades\" and \"Mr Love and Justice\". I have read all three. The first two are excellent. The last, perhaps an experiment that did not come off. But McInnes\\'s work is highly acclaimed; and rightly so. This musical is the novelist\\'s ultimate nightmare - to see the fruits of one\\'s mind being turned into a glitzy, badly-acted, soporific one-dimensional apology of a film that says it captures the spirit of 1950s London, and does nothing of the sort.<br /><br />Thank goodness Colin McInnes wasn\\'t alive to witness it.',\n",
       "       b'I really love the sexy action and sci-fi films of the sixties and its because of the actress\\'s that appeared in them. They found the sexiest women to be in these films and it didn\\'t matter if they could act (Remember \"Candy\"?). The reason I was disappointed by this film was because it wasn\\'t nostalgic enough. The story here has a European sci-fi film called \"Dragonfly\" being made and the director is fired. So the producers decide to let a young aspiring filmmaker (Jeremy Davies) to complete the picture. They\\'re is one real beautiful woman in the film who plays Dragonfly but she\\'s barely in it. Film is written and directed by Roman Coppola who uses some of his fathers exploits from his early days and puts it into the script. I wish the film could have been an homage to those early films. They could have lots of cameos by actors who appeared in them. There is one actor in this film who was popular from the sixties and its John Phillip Law (Barbarella). Gerard Depardieu, Giancarlo Giannini and Dean Stockwell appear as well. I guess I\\'m going to have to continue waiting for a director to make a good homage to the films of the sixties. If any are reading this, \"Make it as sexy as you can\"! I\\'ll be waiting!',\n",
       "       b'Sure, this one isn\\'t really a blockbuster, nor does it target such a position. \"Dieter\" is the first name of a quite popular German musician, who is either loved or hated for his kind of acting and thats exactly what this movie is about. It is based on the autobiography \"Dieter Bohlen\" wrote a few years ago but isn\\'t meant to be accurate on that. The movie is filled with some sexual offensive content (at least for American standard) which is either amusing (not for the other \"actors\" of course) or dumb - it depends on your individual kind of humor or on you being a \"Bohlen\"-Fan or not. Technically speaking there isn\\'t much to criticize. Speaking of me I find this movie to be an OK-movie.'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_examples[:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "IFtaCHTdc-GY"
   },
   "source": [
    "Let's also print the first 10 labels."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:47:21.374706Z",
     "iopub.status.busy": "2022-12-14T12:47:21.374203Z",
     "iopub.status.idle": "2022-12-14T12:47:21.378281Z",
     "shell.execute_reply": "2022-12-14T12:47:21.377665Z"
    },
    "id": "tvAjVXOWc6Mj"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, 1, 1, 1, 0, 0, 0, 0])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_labels[:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "LLC02j2g-llC"
   },
   "source": [
    "## Build the model\n",
    "\n",
    "The neural network is created by stacking layers—this requires three main architectural decisions:\n",
    "\n",
    "* How to represent the text?\n",
    "* How many layers to use in the model?\n",
    "* How many *hidden units* to use for each layer?\n",
    "\n",
    "In this example, the input data consists of sentences. The labels to predict are either 0 or 1.\n",
    "\n",
    "One way to represent the text is to convert sentences into embeddings vectors. We can use a pre-trained text embedding as the first layer, which will have two advantages:\n",
    "*   we don't have to worry about text preprocessing,\n",
    "*   we can benefit from transfer learning.\n",
    "\n",
    "For this example we will use a model from [TensorFlow Hub](https://www.tensorflow.org/hub) called [google/nnlm-en-dim50/2](https://tfhub.dev/google/nnlm-en-dim50/2).\n",
    "\n",
    "There are two other models to test for the sake of this tutorial:\n",
    "* [google/nnlm-en-dim50-with-normalization/2](https://tfhub.dev/google/nnlm-en-dim50-with-normalization/2) - same as [google/nnlm-en-dim50/2](https://tfhub.dev/google/nnlm-en-dim50/2), but with additional text normalization to remove punctuation. This can help to get better coverage of in-vocabulary embeddings for tokens on your input text.\n",
    "* [google/nnlm-en-dim128-with-normalization/2](https://tfhub.dev/google/nnlm-en-dim128-with-normalization/2) - A larger model with an embedding dimension of 128 instead of the smaller 50."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "In2nDpTLkgKa"
   },
   "source": [
    "Let's first create a Keras layer that uses a TensorFlow Hub model to embed the sentences, and try it out on a couple of input examples. Note that the output shape of the produced embeddings is a expected: `(num_examples, embedding_dimension)`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:47:21.381370Z",
     "iopub.status.busy": "2022-12-14T12:47:21.380806Z",
     "iopub.status.idle": "2022-12-14T12:47:23.897825Z",
     "shell.execute_reply": "2022-12-14T12:47:23.897177Z"
    },
    "id": "_NUbzVeYkgcO"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:Please fix your imports. Module tensorflow.python.training.tracking.data_structures has been moved to tensorflow.python.trackable.data_structures. The old module will be deleted in version 2.11.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:Please fix your imports. Module tensorflow.python.training.tracking.data_structures has been moved to tensorflow.python.trackable.data_structures. The old module will be deleted in version 2.11.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<tf.Tensor: shape=(3, 50), dtype=float32, numpy=\n",
       "array([[ 0.5423194 , -0.01190171,  0.06337537,  0.0686297 , -0.16776839,\n",
       "        -0.10581177,  0.168653  , -0.04998823, -0.31148052,  0.07910344,\n",
       "         0.15442258,  0.01488661,  0.03930155,  0.19772716, -0.12215477,\n",
       "        -0.04120982, -0.27041087, -0.21922147,  0.26517656, -0.80739075,\n",
       "         0.25833526, -0.31004202,  0.2868321 ,  0.19433866, -0.29036498,\n",
       "         0.0386285 , -0.78444123, -0.04793238,  0.41102988, -0.36388886,\n",
       "        -0.58034706,  0.30269453,  0.36308962, -0.15227163, -0.4439151 ,\n",
       "         0.19462997,  0.19528405,  0.05666233,  0.2890704 , -0.28468323,\n",
       "        -0.00531206,  0.0571938 , -0.3201319 , -0.04418665, -0.08550781,\n",
       "        -0.55847436, -0.2333639 , -0.20782956, -0.03543065, -0.17533456],\n",
       "       [ 0.56338924, -0.12339553, -0.10862677,  0.7753425 , -0.07667087,\n",
       "        -0.15752274,  0.01872334, -0.08169781, -0.3521876 ,  0.46373403,\n",
       "        -0.08492758,  0.07166861, -0.00670818,  0.12686071, -0.19326551,\n",
       "        -0.5262643 , -0.32958236,  0.14394784,  0.09043556, -0.54175544,\n",
       "         0.02468163, -0.15456744,  0.68333143,  0.09068333, -0.45327246,\n",
       "         0.23180094, -0.8615696 ,  0.3448039 ,  0.12838459, -0.58759046,\n",
       "        -0.40712303,  0.23061076,  0.48426905, -0.2712814 , -0.5380918 ,\n",
       "         0.47016335,  0.2257274 , -0.00830665,  0.28462422, -0.30498496,\n",
       "         0.04400366,  0.25025868,  0.14867125,  0.4071703 , -0.15422425,\n",
       "        -0.06878027, -0.40825695, -0.31492147,  0.09283663, -0.20183429],\n",
       "       [ 0.7456156 ,  0.21256858,  0.1440033 ,  0.52338624,  0.11032254,\n",
       "         0.00902788, -0.36678016, -0.08938274, -0.24165548,  0.33384597,\n",
       "        -0.111946  , -0.01460045, -0.00716449,  0.19562715,  0.00685217,\n",
       "        -0.24886714, -0.42796353,  0.1862    , -0.05241097, -0.664625  ,\n",
       "         0.13449019, -0.22205493,  0.08633009,  0.43685383,  0.2972681 ,\n",
       "         0.36140728, -0.71968895,  0.05291242, -0.1431612 , -0.15733941,\n",
       "        -0.15056324, -0.05988007, -0.08178931, -0.15569413, -0.09303784,\n",
       "        -0.18971168,  0.0762079 , -0.02541647, -0.27134502, -0.3392682 ,\n",
       "        -0.10296471, -0.27275252, -0.34078008,  0.20083308, -0.26644838,\n",
       "         0.00655449, -0.05141485, -0.04261916, -0.4541363 ,  0.20023566]],\n",
       "      dtype=float32)>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = \"https://tfhub.dev/google/nnlm-en-dim50/2\"\n",
    "hub_layer = hub.KerasLayer(model, input_shape=[], dtype=tf.string, trainable=True)\n",
    "hub_layer(train_examples[:3])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "dfSbV6igl1EH"
   },
   "source": [
    "Let's now build the full model:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:47:23.901926Z",
     "iopub.status.busy": "2022-12-14T12:47:23.901348Z",
     "iopub.status.idle": "2022-12-14T12:47:24.353421Z",
     "shell.execute_reply": "2022-12-14T12:47:24.352805Z"
    },
    "id": "xpKOoWgu-llD"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From /tmpfs/src/tf_docs_env/lib/python3.9/site-packages/tensorflow/python/autograph/pyct/static_analysis/liveness.py:83: Analyzer.lamba_check (from tensorflow.python.autograph.pyct.static_analysis.liveness) is deprecated and will be removed after 2023-09-23.\n",
      "Instructions for updating:\n",
      "Lambda fuctions will be no more assumed to be used in the statement where they are used, or at least in the same block. https://github.com/tensorflow/tensorflow/issues/56089\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From /tmpfs/src/tf_docs_env/lib/python3.9/site-packages/tensorflow/python/autograph/pyct/static_analysis/liveness.py:83: Analyzer.lamba_check (from tensorflow.python.autograph.pyct.static_analysis.liveness) is deprecated and will be removed after 2023-09-23.\n",
      "Instructions for updating:\n",
      "Lambda fuctions will be no more assumed to be used in the statement where they are used, or at least in the same block. https://github.com/tensorflow/tensorflow/issues/56089\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"sequential\"\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "_________________________________________________________________\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Layer (type)                Output Shape              Param #   \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=================================================================\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " keras_layer (KerasLayer)    (None, 50)                48190600  \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                                                 \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " dense (Dense)               (None, 16)                816       \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                                                 \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " dense_1 (Dense)             (None, 1)                 17        \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                                                 \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=================================================================\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total params: 48,191,433\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Trainable params: 48,191,433\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Non-trainable params: 0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "_________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "model = tf.keras.Sequential()\n",
    "model.add(hub_layer)\n",
    "model.add(tf.keras.layers.Dense(16, activation='relu'))\n",
    "model.add(tf.keras.layers.Dense(1))\n",
    "\n",
    "model.summary()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "6PbKQ6mucuKL"
   },
   "source": [
    "The layers are stacked sequentially to build the classifier:\n",
    "\n",
    "1. The first layer is a TensorFlow Hub layer. This layer uses a pre-trained Saved Model to map a sentence into its embedding vector. The model that we are using ([google/nnlm-en-dim50/2](https://tfhub.dev/google/nnlm-en-dim50/2)) splits the sentence into tokens, embeds each token and then combines the embedding. The resulting dimensions are: `(num_examples, embedding_dimension)`.\n",
    "2. This fixed-length output vector is piped through a fully-connected (`Dense`) layer with 16 hidden units.\n",
    "3. The last layer is densely connected with a single output node. This outputs logits: the log-odds of the true class, according to the model."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "0XMwnDOp-llH"
   },
   "source": [
    "### Hidden units\n",
    "\n",
    "The above model has two intermediate or \"hidden\" layers, between the input and output. The number of outputs (units, nodes, or neurons) is the dimension of the representational space for the layer. In other words, the amount of freedom the network is allowed when learning an internal representation.\n",
    "\n",
    "If a model has more hidden units (a higher-dimensional representation space), and/or more layers, then the network can learn more complex representations. However, it makes the network more computationally expensive and may lead to learning unwanted patterns—patterns that improve performance on training data but not on the test data. This is called *overfitting*, and we'll explore it later."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "L4EqVWg4-llM"
   },
   "source": [
    "### Loss function and optimizer\n",
    "\n",
    "A model needs a loss function and an optimizer for training. Since this is a binary classification problem and the model outputs a probability (a single-unit layer with a sigmoid activation), we'll use the `binary_crossentropy` loss function. \n",
    "\n",
    "This isn't the only choice for a loss function, you could, for instance, choose `mean_squared_error`. But, generally, `binary_crossentropy` is better for dealing with probabilities—it measures the \"distance\" between probability distributions, or in our case, between the ground-truth distribution and the predictions.\n",
    "\n",
    "Later, when we are exploring regression problems (say, to predict the price of a house), we will see how to use another loss function called mean squared error.\n",
    "\n",
    "Now, configure the model to use an optimizer and a loss function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:47:24.360226Z",
     "iopub.status.busy": "2022-12-14T12:47:24.359649Z",
     "iopub.status.idle": "2022-12-14T12:47:24.374257Z",
     "shell.execute_reply": "2022-12-14T12:47:24.373694Z"
    },
    "id": "Mr0GP-cQ-llN"
   },
   "outputs": [],
   "source": [
    "model.compile(optimizer='adam',\n",
    "              loss=tf.losses.BinaryCrossentropy(from_logits=True),\n",
    "              metrics=[tf.metrics.BinaryAccuracy(threshold=0.0, name='accuracy')])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "hCWYwkug-llQ"
   },
   "source": [
    "## Create a validation set\n",
    "\n",
    "When training, we want to check the accuracy of the model on data it hasn't seen before. Create a *validation set* by setting apart 10,000 examples from the original training data. (Why not use the testing set now? Our goal is to develop and tune our model using only the training data, then use the test data just once to evaluate our accuracy)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:47:24.377515Z",
     "iopub.status.busy": "2022-12-14T12:47:24.376977Z",
     "iopub.status.idle": "2022-12-14T12:47:24.380307Z",
     "shell.execute_reply": "2022-12-14T12:47:24.379753Z"
    },
    "id": "-NpcXY9--llS"
   },
   "outputs": [],
   "source": [
    "x_val = train_examples[:10000]\n",
    "partial_x_train = train_examples[10000:]\n",
    "\n",
    "y_val = train_labels[:10000]\n",
    "partial_y_train = train_labels[10000:]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "35jv_fzP-llU"
   },
   "source": [
    "## Train the model\n",
    "\n",
    "Train the model for 40 epochs in mini-batches of 512 samples. This is 40 iterations over all samples in the `x_train` and `y_train` tensors. While training, monitor the model's loss and accuracy on the 10,000 samples from the validation set:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:47:24.383464Z",
     "iopub.status.busy": "2022-12-14T12:47:24.382872Z",
     "iopub.status.idle": "2022-12-14T12:49:50.967426Z",
     "shell.execute_reply": "2022-12-14T12:49:50.966643Z"
    },
    "id": "tXSGrjWZ-llW"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 46s - loss: 0.7374 - accuracy: 0.4609"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.7238 - accuracy: 0.4883 "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.7195 - accuracy: 0.4909"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 4s - loss: 0.7167 - accuracy: 0.4897"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 4s - loss: 0.7122 - accuracy: 0.4926"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 4s - loss: 0.7108 - accuracy: 0.4922"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 3s - loss: 0.7084 - accuracy: 0.4941"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 3s - loss: 0.7067 - accuracy: 0.4956"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 3s - loss: 0.7047 - accuracy: 0.4980"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 3s - loss: 0.7030 - accuracy: 0.5016"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 3s - loss: 0.7011 - accuracy: 0.5071"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 3s - loss: 0.6993 - accuracy: 0.5142"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 2s - loss: 0.6978 - accuracy: 0.5197"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 2s - loss: 0.6957 - accuracy: 0.5272"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 2s - loss: 0.6937 - accuracy: 0.5341"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 2s - loss: 0.6921 - accuracy: 0.5393"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 2s - loss: 0.6899 - accuracy: 0.5454"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 2s - loss: 0.6878 - accuracy: 0.5521"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.6862 - accuracy: 0.5552"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.6842 - accuracy: 0.5602"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.6827 - accuracy: 0.5635"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 1s - loss: 0.6809 - accuracy: 0.5685"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 1s - loss: 0.6791 - accuracy: 0.5740"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 1s - loss: 0.6773 - accuracy: 0.5798"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.6754 - accuracy: 0.5850"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.6739 - accuracy: 0.5892"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.6717 - accuracy: 0.5941"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.6696 - accuracy: 0.5989"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.6681 - accuracy: 0.6020"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.6674 - accuracy: 0.6038"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 7s 185ms/step - loss: 0.6674 - accuracy: 0.6038 - val_loss: 0.6107 - val_accuracy: 0.7183\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 2/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.5920 - accuracy: 0.7539"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.5869 - accuracy: 0.7676"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.5880 - accuracy: 0.7624"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 4s - loss: 0.5877 - accuracy: 0.7573"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 4s - loss: 0.5892 - accuracy: 0.7492"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 4s - loss: 0.5885 - accuracy: 0.7497"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 3s - loss: 0.5901 - accuracy: 0.7441"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 3s - loss: 0.5872 - accuracy: 0.7495"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 3s - loss: 0.5853 - accuracy: 0.7480"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 3s - loss: 0.5816 - accuracy: 0.7523"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 3s - loss: 0.5796 - accuracy: 0.7541"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 2s - loss: 0.5778 - accuracy: 0.7562"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 2s - loss: 0.5760 - accuracy: 0.7585"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 2s - loss: 0.5733 - accuracy: 0.7613"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 2s - loss: 0.5723 - accuracy: 0.7616"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 2s - loss: 0.5699 - accuracy: 0.7626"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.5681 - accuracy: 0.7645"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.5661 - accuracy: 0.7656"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.5647 - accuracy: 0.7664"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.5632 - accuracy: 0.7662"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 1s - loss: 0.5600 - accuracy: 0.7686"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.5557 - accuracy: 0.7726"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.5527 - accuracy: 0.7732"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.5508 - accuracy: 0.7742"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.5496 - accuracy: 0.7739"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.5477 - accuracy: 0.7755"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.5474 - accuracy: 0.7755"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 5s 161ms/step - loss: 0.5474 - accuracy: 0.7755 - val_loss: 0.5007 - val_accuracy: 0.7969\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 3/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.4481 - accuracy: 0.8555"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.4596 - accuracy: 0.8408"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.4556 - accuracy: 0.8483"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 4s - loss: 0.4563 - accuracy: 0.8457"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 4s - loss: 0.4555 - accuracy: 0.8426"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 4s - loss: 0.4530 - accuracy: 0.8444"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 3s - loss: 0.4508 - accuracy: 0.8411"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 3s - loss: 0.4493 - accuracy: 0.8392"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 3s - loss: 0.4461 - accuracy: 0.8426"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 2s - loss: 0.4443 - accuracy: 0.8427"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 2s - loss: 0.4419 - accuracy: 0.8434"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 2s - loss: 0.4421 - accuracy: 0.8422"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 2s - loss: 0.4405 - accuracy: 0.8419"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 2s - loss: 0.4378 - accuracy: 0.8436"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 2s - loss: 0.4362 - accuracy: 0.8451"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 2s - loss: 0.4361 - accuracy: 0.8448"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.4330 - accuracy: 0.8471"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.4302 - accuracy: 0.8482"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.4292 - accuracy: 0.8479"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.4282 - accuracy: 0.8484"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 1s - loss: 0.4255 - accuracy: 0.8503"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 1s - loss: 0.4227 - accuracy: 0.8518"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.4197 - accuracy: 0.8518"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.4175 - accuracy: 0.8528"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.4174 - accuracy: 0.8516"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.4158 - accuracy: 0.8523"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.4142 - accuracy: 0.8522"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.4135 - accuracy: 0.8528"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 5s 166ms/step - loss: 0.4135 - accuracy: 0.8528 - val_loss: 0.3994 - val_accuracy: 0.8423\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 4/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.3264 - accuracy: 0.8965"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.3236 - accuracy: 0.9014"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.3298 - accuracy: 0.8965"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 4s - loss: 0.3322 - accuracy: 0.8926"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 4s - loss: 0.3300 - accuracy: 0.8922"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 4s - loss: 0.3252 - accuracy: 0.8939"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 3s - loss: 0.3253 - accuracy: 0.8920"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 3s - loss: 0.3255 - accuracy: 0.8921"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 3s - loss: 0.3235 - accuracy: 0.8924"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 3s - loss: 0.3237 - accuracy: 0.8916"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 3s - loss: 0.3239 - accuracy: 0.8897"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 3s - loss: 0.3226 - accuracy: 0.8905"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 2s - loss: 0.3191 - accuracy: 0.8919"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 2s - loss: 0.3184 - accuracy: 0.8922"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 2s - loss: 0.3160 - accuracy: 0.8934"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 2s - loss: 0.3147 - accuracy: 0.8945"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.3132 - accuracy: 0.8947"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.3115 - accuracy: 0.8954"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 1s - loss: 0.3079 - accuracy: 0.8959"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 1s - loss: 0.3071 - accuracy: 0.8957"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.3068 - accuracy: 0.8947"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.3061 - accuracy: 0.8944"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.3043 - accuracy: 0.8955"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.3035 - accuracy: 0.8957"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.3023 - accuracy: 0.8955"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.3019 - accuracy: 0.8955"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 5s 156ms/step - loss: 0.3019 - accuracy: 0.8955 - val_loss: 0.3448 - val_accuracy: 0.8572\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 5/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.2593 - accuracy: 0.9102"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.2555 - accuracy: 0.9111"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.2597 - accuracy: 0.9069"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 4s - loss: 0.2507 - accuracy: 0.9131"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 4s - loss: 0.2468 - accuracy: 0.9156"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 3s - loss: 0.2477 - accuracy: 0.9141"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 3s - loss: 0.2476 - accuracy: 0.9132"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 3s - loss: 0.2457 - accuracy: 0.9148"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 3s - loss: 0.2449 - accuracy: 0.9154"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 3s - loss: 0.2413 - accuracy: 0.9187"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 3s - loss: 0.2414 - accuracy: 0.9181"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 2s - loss: 0.2397 - accuracy: 0.9188"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 2s - loss: 0.2400 - accuracy: 0.9187"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 2s - loss: 0.2371 - accuracy: 0.9202"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 2s - loss: 0.2357 - accuracy: 0.9208"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 2s - loss: 0.2347 - accuracy: 0.9215"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 2s - loss: 0.2335 - accuracy: 0.9219"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 2s - loss: 0.2331 - accuracy: 0.9222"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.2328 - accuracy: 0.9221"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.2310 - accuracy: 0.9229"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.2294 - accuracy: 0.9239"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 1s - loss: 0.2284 - accuracy: 0.9242"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 1s - loss: 0.2276 - accuracy: 0.9244"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.2256 - accuracy: 0.9246"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.2242 - accuracy: 0.9253"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.2234 - accuracy: 0.9259"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.2222 - accuracy: 0.9263"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.2214 - accuracy: 0.9265"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.2213 - accuracy: 0.9267"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 5s 170ms/step - loss: 0.2213 - accuracy: 0.9267 - val_loss: 0.3119 - val_accuracy: 0.8652\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 6/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 0.1925 - accuracy: 0.9316"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 5s - loss: 0.1772 - accuracy: 0.9404"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.1746 - accuracy: 0.9427"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 4s - loss: 0.1754 - accuracy: 0.9443"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 4s - loss: 0.1775 - accuracy: 0.9438"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 4s - loss: 0.1786 - accuracy: 0.9440"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 3s - loss: 0.1789 - accuracy: 0.9442"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 3s - loss: 0.1788 - accuracy: 0.9434"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 3s - loss: 0.1775 - accuracy: 0.9431"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 2s - loss: 0.1730 - accuracy: 0.9468"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 2s - loss: 0.1734 - accuracy: 0.9470"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 2s - loss: 0.1732 - accuracy: 0.9466"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 2s - loss: 0.1722 - accuracy: 0.9479"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.1713 - accuracy: 0.9487"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.1702 - accuracy: 0.9490"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.1700 - accuracy: 0.9486"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.1681 - accuracy: 0.9498"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.1674 - accuracy: 0.9508"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.1663 - accuracy: 0.9515"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 1s - loss: 0.1658 - accuracy: 0.9520"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 1s - loss: 0.1656 - accuracy: 0.9520"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.1649 - accuracy: 0.9522"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.1639 - accuracy: 0.9528"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.1632 - accuracy: 0.9532"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.1629 - accuracy: 0.9533"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.1613 - accuracy: 0.9537"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.1612 - accuracy: 0.9538"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 5s 157ms/step - loss: 0.1612 - accuracy: 0.9538 - val_loss: 0.3001 - val_accuracy: 0.8714\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 7/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.1486 - accuracy: 0.9492"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.1338 - accuracy: 0.9629"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.1330 - accuracy: 0.9635"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 4s - loss: 0.1275 - accuracy: 0.9668"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 4s - loss: 0.1240 - accuracy: 0.9691"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 4s - loss: 0.1266 - accuracy: 0.9674"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 3s - loss: 0.1258 - accuracy: 0.9671"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 3s - loss: 0.1253 - accuracy: 0.9670"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 3s - loss: 0.1229 - accuracy: 0.9689"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 2s - loss: 0.1227 - accuracy: 0.9682"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 2s - loss: 0.1220 - accuracy: 0.9688"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 2s - loss: 0.1206 - accuracy: 0.9697"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 2s - loss: 0.1209 - accuracy: 0.9696"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 2s - loss: 0.1195 - accuracy: 0.9707"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 2s - loss: 0.1189 - accuracy: 0.9708"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.1183 - accuracy: 0.9714"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.1181 - accuracy: 0.9716"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 0.1169 - accuracy: 0.9721"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.1161 - accuracy: 0.9722"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.1151 - accuracy: 0.9724"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.1159 - accuracy: 0.9721"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.1163 - accuracy: 0.9716"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.1161 - accuracy: 0.9712"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.1161 - accuracy: 0.9712"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 4s 146ms/step - loss: 0.1161 - accuracy: 0.9712 - val_loss: 0.2985 - val_accuracy: 0.8740\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 8/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.0962 - accuracy: 0.9766"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.1009 - accuracy: 0.9736"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.0937 - accuracy: 0.9753"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 3s - loss: 0.0923 - accuracy: 0.9773"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 3s - loss: 0.0928 - accuracy: 0.9782"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 3s - loss: 0.0894 - accuracy: 0.9807"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 3s - loss: 0.0878 - accuracy: 0.9819"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 3s - loss: 0.0863 - accuracy: 0.9820"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 3s - loss: 0.0849 - accuracy: 0.9828"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 2s - loss: 0.0853 - accuracy: 0.9826"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 2s - loss: 0.0851 - accuracy: 0.9826"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 2s - loss: 0.0842 - accuracy: 0.9829"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0843 - accuracy: 0.9825"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.0839 - accuracy: 0.9829"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0843 - accuracy: 0.9825"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0841 - accuracy: 0.9826"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.0845 - accuracy: 0.9824"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 1s - loss: 0.0844 - accuracy: 0.9824"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 0.0840 - accuracy: 0.9827"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.0836 - accuracy: 0.9827"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0834 - accuracy: 0.9828"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.0836 - accuracy: 0.9825"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0836 - accuracy: 0.9824"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0836 - accuracy: 0.9822"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0832 - accuracy: 0.9824"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 5s 153ms/step - loss: 0.0832 - accuracy: 0.9824 - val_loss: 0.3023 - val_accuracy: 0.8761\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 9/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.0613 - accuracy: 0.9883"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0612 - accuracy: 0.9863"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.0602 - accuracy: 0.9870"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 4s - loss: 0.0614 - accuracy: 0.9868"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 4s - loss: 0.0614 - accuracy: 0.9875"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 3s - loss: 0.0615 - accuracy: 0.9869"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 3s - loss: 0.0616 - accuracy: 0.9873"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 3s - loss: 0.0623 - accuracy: 0.9876"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 3s - loss: 0.0608 - accuracy: 0.9887"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 2s - loss: 0.0616 - accuracy: 0.9888"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 2s - loss: 0.0618 - accuracy: 0.9886"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 2s - loss: 0.0613 - accuracy: 0.9889"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 2s - loss: 0.0611 - accuracy: 0.9891"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 2s - loss: 0.0610 - accuracy: 0.9896"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 2s - loss: 0.0607 - accuracy: 0.9897"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 2s - loss: 0.0606 - accuracy: 0.9898"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0601 - accuracy: 0.9899"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.0599 - accuracy: 0.9900"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 1s - loss: 0.0598 - accuracy: 0.9900"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 1s - loss: 0.0600 - accuracy: 0.9901"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.0607 - accuracy: 0.9896"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0605 - accuracy: 0.9895"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0600 - accuracy: 0.9897"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0596 - accuracy: 0.9898"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0596 - accuracy: 0.9897"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0595 - accuracy: 0.9897"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 5s 155ms/step - loss: 0.0595 - accuracy: 0.9897 - val_loss: 0.3126 - val_accuracy: 0.8755\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 10/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.0406 - accuracy: 0.9980"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0398 - accuracy: 0.9980"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.0459 - accuracy: 0.9967"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 2s - loss: 0.0454 - accuracy: 0.9958"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 2s - loss: 0.0444 - accuracy: 0.9958"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 2s - loss: 0.0444 - accuracy: 0.9956"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 2s - loss: 0.0428 - accuracy: 0.9963"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 2s - loss: 0.0423 - accuracy: 0.9966"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 2s - loss: 0.0420 - accuracy: 0.9964"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 1s - loss: 0.0427 - accuracy: 0.9960"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 0.0425 - accuracy: 0.9961"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0429 - accuracy: 0.9960"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0430 - accuracy: 0.9957"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0430 - accuracy: 0.9954"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0429 - accuracy: 0.9953"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.0429 - accuracy: 0.9953"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 1s - loss: 0.0428 - accuracy: 0.9952"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0425 - accuracy: 0.9952"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.0427 - accuracy: 0.9952"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0428 - accuracy: 0.9949"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0429 - accuracy: 0.9949"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0428 - accuracy: 0.9950"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0428 - accuracy: 0.9951"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 4s 140ms/step - loss: 0.0428 - accuracy: 0.9951 - val_loss: 0.3225 - val_accuracy: 0.8736\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 11/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.0333 - accuracy: 0.9961"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0360 - accuracy: 0.9961"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.0351 - accuracy: 0.9961"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 4s - loss: 0.0353 - accuracy: 0.9966"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 3s - loss: 0.0332 - accuracy: 0.9971"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 3s - loss: 0.0339 - accuracy: 0.9967"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 2s - loss: 0.0331 - accuracy: 0.9970"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 2s - loss: 0.0329 - accuracy: 0.9971"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 2s - loss: 0.0322 - accuracy: 0.9973"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 2s - loss: 0.0322 - accuracy: 0.9974"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 0.0319 - accuracy: 0.9974"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0317 - accuracy: 0.9976"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.0317 - accuracy: 0.9976"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0316 - accuracy: 0.9976"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0315 - accuracy: 0.9978"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.0315 - accuracy: 0.9979"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.0323 - accuracy: 0.9977"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0320 - accuracy: 0.9978"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.0317 - accuracy: 0.9979"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0313 - accuracy: 0.9980"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0311 - accuracy: 0.9980"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0309 - accuracy: 0.9979"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0309 - accuracy: 0.9979"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 4s 141ms/step - loss: 0.0309 - accuracy: 0.9979 - val_loss: 0.3355 - val_accuracy: 0.8735\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 12/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.0212 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 2s - loss: 0.0231 - accuracy: 0.9993"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 3s - loss: 0.0226 - accuracy: 0.9995"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 2s - loss: 0.0229 - accuracy: 0.9993"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 2s - loss: 0.0227 - accuracy: 0.9992"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 2s - loss: 0.0226 - accuracy: 0.9990"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 2s - loss: 0.0224 - accuracy: 0.9988"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 2s - loss: 0.0222 - accuracy: 0.9989"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 0.0227 - accuracy: 0.9988"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0227 - accuracy: 0.9988"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.0224 - accuracy: 0.9988"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0226 - accuracy: 0.9988"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0226 - accuracy: 0.9987"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 0.0222 - accuracy: 0.9988"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 0.0221 - accuracy: 0.9989"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.0220 - accuracy: 0.9989"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0220 - accuracy: 0.9990"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.0219 - accuracy: 0.9989"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0220 - accuracy: 0.9990"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0219 - accuracy: 0.9990"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0219 - accuracy: 0.9989"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0219 - accuracy: 0.9989"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 4s 136ms/step - loss: 0.0219 - accuracy: 0.9989 - val_loss: 0.3517 - val_accuracy: 0.8734\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 13/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 5s - loss: 0.0142 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0157 - accuracy: 0.9990"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.0142 - accuracy: 0.9993"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 4s - loss: 0.0140 - accuracy: 0.9995"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 4s - loss: 0.0138 - accuracy: 0.9996"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 4s - loss: 0.0144 - accuracy: 0.9993"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 3s - loss: 0.0148 - accuracy: 0.9992"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 3s - loss: 0.0151 - accuracy: 0.9993"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 3s - loss: 0.0150 - accuracy: 0.9991"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 3s - loss: 0.0149 - accuracy: 0.9992"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 3s - loss: 0.0149 - accuracy: 0.9993"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 2s - loss: 0.0150 - accuracy: 0.9994"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 2s - loss: 0.0153 - accuracy: 0.9993"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0154 - accuracy: 0.9993"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0153 - accuracy: 0.9993"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.0153 - accuracy: 0.9993"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0152 - accuracy: 0.9994"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.0153 - accuracy: 0.9994"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 1s - loss: 0.0152 - accuracy: 0.9995"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 0.0156 - accuracy: 0.9994"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.0155 - accuracy: 0.9993"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0156 - accuracy: 0.9992"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0155 - accuracy: 0.9992"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 4s 131ms/step - loss: 0.0155 - accuracy: 0.9992 - val_loss: 0.3677 - val_accuracy: 0.8710\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 14/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.0103 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0117 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 2s - loss: 0.0119 - accuracy: 0.9996"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 2s - loss: 0.0118 - accuracy: 0.9997"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 2s - loss: 0.0115 - accuracy: 0.9997"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 2s - loss: 0.0113 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 2s - loss: 0.0113 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 2s - loss: 0.0113 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 2s - loss: 0.0116 - accuracy: 0.9996"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 2s - loss: 0.0116 - accuracy: 0.9997"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 2s - loss: 0.0115 - accuracy: 0.9997"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 2s - loss: 0.0115 - accuracy: 0.9997"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0113 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0112 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0114 - accuracy: 0.9996"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0118 - accuracy: 0.9995"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.0117 - accuracy: 0.9995"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.0115 - accuracy: 0.9996"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0113 - accuracy: 0.9996"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0113 - accuracy: 0.9997"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0113 - accuracy: 0.9997"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 4s 127ms/step - loss: 0.0113 - accuracy: 0.9997 - val_loss: 0.3825 - val_accuracy: 0.8713\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 15/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.0084 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 2s - loss: 0.0097 - accuracy: 0.9993"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 2s - loss: 0.0087 - accuracy: 0.9996"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 2s - loss: 0.0086 - accuracy: 0.9997"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 1s - loss: 0.0086 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 1s - loss: 0.0085 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 1s - loss: 0.0083 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 1s - loss: 0.0083 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 1s - loss: 0.0083 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 0.0082 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0087 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0086 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.0086 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0086 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0087 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.0086 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 0.0085 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0086 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0085 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0084 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0084 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 4s 130ms/step - loss: 0.0084 - accuracy: 0.9999 - val_loss: 0.3984 - val_accuracy: 0.8693\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 16/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 0.0059 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0065 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 3s - loss: 0.0065 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 1s - loss: 0.0070 - accuracy: 0.9997"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 1s - loss: 0.0068 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 1s - loss: 0.0067 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 1s - loss: 0.0066 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 1s - loss: 0.0065 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 1s - loss: 0.0066 - accuracy: 0.9998"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 1s - loss: 0.0066 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0066 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.0066 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0066 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0066 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.0066 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 0.0065 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.0066 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.0065 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0065 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0065 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0065 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0065 - accuracy: 0.9999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 4s 131ms/step - loss: 0.0065 - accuracy: 0.9999 - val_loss: 0.4091 - val_accuracy: 0.8698\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 17/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.0054 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0052 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.0055 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 4s - loss: 0.0054 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 3s - loss: 0.0055 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 3s - loss: 0.0055 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 2s - loss: 0.0055 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 1s - loss: 0.0054 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 0.0053 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0053 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.0053 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0053 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 0.0053 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 0.0053 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0052 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0052 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0051 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0051 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 110ms/step - loss: 0.0051 - accuracy: 1.0000 - val_loss: 0.4210 - val_accuracy: 0.8690\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 18/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.0048 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0046 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.0045 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 2s - loss: 0.0042 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 2s - loss: 0.0042 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 2s - loss: 0.0042 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 2s - loss: 0.0041 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 1s - loss: 0.0042 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 0.0042 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0042 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0041 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0041 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 0s - loss: 0.0041 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 0.0041 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0041 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.0041 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0041 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0042 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 4s 118ms/step - loss: 0.0042 - accuracy: 1.0000 - val_loss: 0.4316 - val_accuracy: 0.8690\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 19/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 0.0037 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0035 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 2s - loss: 0.0036 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 2s - loss: 0.0035 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 2s - loss: 0.0035 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 2s - loss: 0.0035 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 2s - loss: 0.0035 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 1s - loss: 0.0035 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 0.0035 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0035 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 0s - loss: 0.0034 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 0.0034 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0034 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.0034 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0034 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0034 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0034 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0035 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 101ms/step - loss: 0.0035 - accuracy: 1.0000 - val_loss: 0.4417 - val_accuracy: 0.8690\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 20/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 0.0030 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0030 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 3s - loss: 0.0031 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 3s - loss: 0.0031 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 2s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 2s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 2s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 2s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 2s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0029 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 4s 126ms/step - loss: 0.0029 - accuracy: 1.0000 - val_loss: 0.4514 - val_accuracy: 0.8690\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 21/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.0028 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 0s - loss: 0.0028 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 1s - loss: 0.0026 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 1s - loss: 0.0026 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 1s - loss: 0.0026 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 1s - loss: 0.0026 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 1s - loss: 0.0026 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 1s - loss: 0.0025 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 0.0025 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0025 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0025 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.0025 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0025 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0025 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 0s - loss: 0.0025 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 0.0025 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0025 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.0025 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0025 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 112ms/step - loss: 0.0025 - accuracy: 1.0000 - val_loss: 0.4609 - val_accuracy: 0.8677\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 22/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 0.0020 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 2s - loss: 0.0023 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 2s - loss: 0.0023 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 2s - loss: 0.0023 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 2s - loss: 0.0023 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 2s - loss: 0.0022 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 2s - loss: 0.0023 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 2s - loss: 0.0022 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 2s - loss: 0.0022 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 2s - loss: 0.0022 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0021 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0022 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0022 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 0s - loss: 0.0022 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 0.0022 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0021 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.0021 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0021 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0022 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0021 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 117ms/step - loss: 0.0021 - accuracy: 1.0000 - val_loss: 0.4689 - val_accuracy: 0.8677\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 23/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 0.0016 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 0.0018 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 4s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 2s - loss: 0.0018 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 2s - loss: 0.0018 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 2s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 2s - loss: 0.0018 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 2s - loss: 0.0018 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 2s - loss: 0.0018 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 2s - loss: 0.0018 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 2s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 1s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0019 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 4s 140ms/step - loss: 0.0019 - accuracy: 1.0000 - val_loss: 0.4764 - val_accuracy: 0.8683\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 24/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 0.0018 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0016 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 2s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 2s - loss: 0.0018 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 2s - loss: 0.0018 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 2s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 2s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 1s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.0016 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 115ms/step - loss: 0.0017 - accuracy: 1.0000 - val_loss: 0.4831 - val_accuracy: 0.8681\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 25/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.0017 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0016 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 2s - loss: 0.0016 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 2s - loss: 0.0016 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 2s - loss: 0.0016 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 2s - loss: 0.0015 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 2s - loss: 0.0015 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 1s - loss: 0.0015 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 1s - loss: 0.0015 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 0.0015 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0015 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0015 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0015 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 1s - loss: 0.0015 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 0.0015 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0015 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0015 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0015 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 4s 115ms/step - loss: 0.0015 - accuracy: 1.0000 - val_loss: 0.4905 - val_accuracy: 0.8679\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 26/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 1s - loss: 0.0013 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 2s - loss: 0.0014 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 2s - loss: 0.0014 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 2s - loss: 0.0013 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 2s - loss: 0.0014 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 1s - loss: 0.0014 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 0.0013 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0013 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0013 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 0s - loss: 0.0013 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 0s - loss: 0.0013 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 0.0013 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 0.0013 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0013 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0013 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0013 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0013 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 101ms/step - loss: 0.0013 - accuracy: 1.0000 - val_loss: 0.4973 - val_accuracy: 0.8675\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 27/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 0s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 1s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 1s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 1s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 1s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 1s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 0s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0012 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 115ms/step - loss: 0.0012 - accuracy: 1.0000 - val_loss: 0.5031 - val_accuracy: 0.8680\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 28/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 2s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 2s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 2s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 1s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 1s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 1s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 0s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 0.0011 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 115ms/step - loss: 0.0011 - accuracy: 1.0000 - val_loss: 0.5094 - val_accuracy: 0.8682\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 29/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 8.9673e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 2s - loss: 9.4121e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 2s - loss: 9.6585e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 1s - loss: 9.6112e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 1s - loss: 9.4627e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 1s - loss: 9.5676e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 1s - loss: 9.7117e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 9.7113e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 9.7027e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 0s - loss: 9.7428e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 9.7339e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 9.7461e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 9.7082e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 9.6927e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 2s 85ms/step - loss: 9.6927e-04 - accuracy: 1.0000 - val_loss: 0.5151 - val_accuracy: 0.8674\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 30/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 8.2724e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 9.4666e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 1s - loss: 9.4043e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 1s - loss: 9.1186e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 2s - loss: 9.1512e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 2s - loss: 9.0563e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 2s - loss: 9.0471e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 1s - loss: 8.8579e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 8.8225e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 8.7778e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 8.8367e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 0s - loss: 8.8347e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 8.7572e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 8.7421e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 8.7295e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 8.7731e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 8.7951e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 8.8498e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 8.8408e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 105ms/step - loss: 8.8408e-04 - accuracy: 1.0000 - val_loss: 0.5207 - val_accuracy: 0.8670\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 31/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 8.6618e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 2s - loss: 7.9032e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 1s - loss: 8.3645e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 1s - loss: 8.3308e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 1s - loss: 8.2761e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 1s - loss: 8.0926e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 1s - loss: 8.0741e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 8.0317e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 8.0732e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 0s - loss: 8.0006e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 8.0126e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 8.0519e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 8.0733e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 8.1054e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 8.0958e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 8.1034e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 96ms/step - loss: 8.1034e-04 - accuracy: 1.0000 - val_loss: 0.5259 - val_accuracy: 0.8671\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 32/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 7.5749e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 0s - loss: 7.4282e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 1s - loss: 7.5746e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 1s - loss: 7.6688e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 1s - loss: 7.4262e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 1s - loss: 7.5133e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 1s - loss: 7.4291e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 0s - loss: 7.5322e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 0s - loss: 7.5358e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 0s - loss: 7.5298e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 0s - loss: 7.5086e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 7.4916e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 7.4377e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 7.4340e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 7.4201e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 7.4257e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 7.4726e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 7.4637e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 101ms/step - loss: 7.4637e-04 - accuracy: 1.0000 - val_loss: 0.5310 - val_accuracy: 0.8669\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 33/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 7.9582e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 0s - loss: 7.5172e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 1s - loss: 7.2230e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 1s - loss: 7.4030e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 1s - loss: 7.2269e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 1s - loss: 7.1781e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 1s - loss: 7.1335e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 0s - loss: 6.9823e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 0s - loss: 6.9427e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 0s - loss: 6.9245e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 6.8393e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 6.8584e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 6.8614e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 6.8929e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 6.8753e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 2s 85ms/step - loss: 6.8753e-04 - accuracy: 1.0000 - val_loss: 0.5363 - val_accuracy: 0.8668\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 34/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 5.3109e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 6.8149e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 6.4164e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 4s - loss: 6.8004e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 3s - loss: 6.7505e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 3s - loss: 6.5857e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 3s - loss: 6.5135e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 2s - loss: 6.3974e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 1s - loss: 6.3106e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 6.2763e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 0s - loss: 6.2954e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 0s - loss: 6.2805e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 6.2777e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 6.2988e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 6.3376e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 6.3466e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 89ms/step - loss: 6.3466e-04 - accuracy: 1.0000 - val_loss: 0.5411 - val_accuracy: 0.8666\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 35/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 5.8586e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 5.7255e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 3s - loss: 6.0258e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 3s - loss: 5.8580e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 2s - loss: 5.8903e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 2s - loss: 5.9236e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 2s - loss: 5.8159e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 2s - loss: 5.8813e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "14/30 [=============>................] - ETA: 1s - loss: 5.8891e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 5.8377e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 1s - loss: 5.9325e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 1s - loss: 5.9050e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 1s - loss: 5.9120e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 5.8980e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 5.9157e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 5.9501e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 5.8890e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 5.8873e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 110ms/step - loss: 5.8873e-04 - accuracy: 1.0000 - val_loss: 0.5458 - val_accuracy: 0.8665\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 36/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 5.5315e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 0s - loss: 5.8226e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 1s - loss: 5.8293e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 1s - loss: 5.7883e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 1s - loss: 5.5737e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 1s - loss: 5.5343e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 1s - loss: 5.5081e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 1s - loss: 5.5599e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 1s - loss: 5.5091e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 0s - loss: 5.4693e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 5.4822e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 5.4974e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 5.4791e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 5.4648e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 5.4746e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 5.4755e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 90ms/step - loss: 5.4755e-04 - accuracy: 1.0000 - val_loss: 0.5502 - val_accuracy: 0.8663\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 37/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 5.4676e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 2s - loss: 4.8790e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/30 [====>.........................] - ETA: 2s - loss: 4.7866e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 2s - loss: 4.9952e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 1s - loss: 4.8520e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 1s - loss: 4.9962e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 1s - loss: 5.0077e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 0s - loss: 5.1383e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/30 [================>.............] - ETA: 0s - loss: 5.1305e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 0s - loss: 5.1380e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 0s - loss: 5.1972e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 0s - loss: 5.1906e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "22/30 [=====================>........] - ETA: 0s - loss: 5.2064e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 5.1120e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 5.0866e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 5.0999e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 86ms/step - loss: 5.0999e-04 - accuracy: 1.0000 - val_loss: 0.5548 - val_accuracy: 0.8659\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 38/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 5.4977e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 1s - loss: 4.8318e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 1s - loss: 4.6514e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8/30 [=======>......................] - ETA: 1s - loss: 4.6808e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/30 [==========>...................] - ETA: 1s - loss: 4.7210e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 1s - loss: 4.7753e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 1s - loss: 4.7368e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 1s - loss: 4.7918e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 0s - loss: 4.8842e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 0s - loss: 4.8868e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/30 [======================>.......] - ETA: 0s - loss: 4.8532e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 4.8339e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "26/30 [=========================>....] - ETA: 0s - loss: 4.8052e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 4.8154e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/30 [============================>.] - ETA: 0s - loss: 4.7770e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 4.7631e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 3s 95ms/step - loss: 4.7631e-04 - accuracy: 1.0000 - val_loss: 0.5590 - val_accuracy: 0.8662\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 39/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 0s - loss: 4.6355e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 2/30 [=>............................] - ETA: 4s - loss: 4.8090e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/30 [==>...........................] - ETA: 4s - loss: 4.6662e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 6/30 [=====>........................] - ETA: 1s - loss: 4.5218e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/30 [========>.....................] - ETA: 1s - loss: 4.5488e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "12/30 [===========>..................] - ETA: 0s - loss: 4.4350e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/30 [==============>...............] - ETA: 0s - loss: 4.4368e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 0s - loss: 4.4082e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 0s - loss: 4.4056e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/30 [===================>..........] - ETA: 0s - loss: 4.4370e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 0s - loss: 4.4485e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 4.4988e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 4.4851e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/30 [==========================>...] - ETA: 0s - loss: 4.4762e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 4.4598e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 2s 69ms/step - loss: 4.4598e-04 - accuracy: 1.0000 - val_loss: 0.5629 - val_accuracy: 0.8665\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 40/40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/30 [>.............................] - ETA: 4s - loss: 3.7949e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 4/30 [===>..........................] - ETA: 0s - loss: 4.0127e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/30 [======>.......................] - ETA: 0s - loss: 3.9780e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "10/30 [=========>....................] - ETA: 0s - loss: 3.9704e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/30 [============>.................] - ETA: 0s - loss: 3.9960e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "16/30 [===============>..............] - ETA: 0s - loss: 4.0581e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "18/30 [=================>............] - ETA: 0s - loss: 4.1009e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/30 [==================>...........] - ETA: 0s - loss: 4.1310e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/30 [====================>.........] - ETA: 0s - loss: 4.1254e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "24/30 [=======================>......] - ETA: 0s - loss: 4.1550e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/30 [========================>.....] - ETA: 0s - loss: 4.1848e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "28/30 [===========================>..] - ETA: 0s - loss: 4.1973e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - ETA: 0s - loss: 4.1837e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "30/30 [==============================] - 2s 70ms/step - loss: 4.1837e-04 - accuracy: 1.0000 - val_loss: 0.5671 - val_accuracy: 0.8660\n"
     ]
    }
   ],
   "source": [
    "history = model.fit(partial_x_train,\n",
    "                    partial_y_train,\n",
    "                    epochs=40,\n",
    "                    batch_size=512,\n",
    "                    validation_data=(x_val, y_val),\n",
    "                    verbose=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "9EEGuDVuzb5r"
   },
   "source": [
    "## Evaluate the model\n",
    "\n",
    "And let's see how the model performs. Two values will be returned. Loss (a number which represents our error, lower values are better), and accuracy."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:49:50.971402Z",
     "iopub.status.busy": "2022-12-14T12:49:50.971116Z",
     "iopub.status.idle": "2022-12-14T12:49:53.524944Z",
     "shell.execute_reply": "2022-12-14T12:49:53.524050Z"
    },
    "id": "zOMKywn4zReN"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      "  1/782 [..............................] - ETA: 20s - loss: 0.8099 - accuracy: 0.7812"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 17/782 [..............................] - ETA: 2s - loss: 0.7173 - accuracy: 0.8382 "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 32/782 [>.............................] - ETA: 2s - loss: 0.7141 - accuracy: 0.8408"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 48/782 [>.............................] - ETA: 2s - loss: 0.6486 - accuracy: 0.8483"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 64/782 [=>............................] - ETA: 2s - loss: 0.6606 - accuracy: 0.8501"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 80/782 [==>...........................] - ETA: 2s - loss: 0.6322 - accuracy: 0.8520"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 96/782 [==>...........................] - ETA: 2s - loss: 0.6349 - accuracy: 0.8512"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "112/782 [===>..........................] - ETA: 2s - loss: 0.6192 - accuracy: 0.8535"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "128/782 [===>..........................] - ETA: 2s - loss: 0.6192 - accuracy: 0.8533"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "144/782 [====>.........................] - ETA: 2s - loss: 0.6177 - accuracy: 0.8524"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "161/782 [=====>........................] - ETA: 1s - loss: 0.6144 - accuracy: 0.8540"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "177/782 [=====>........................] - ETA: 1s - loss: 0.6103 - accuracy: 0.8547"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "194/782 [======>.......................] - ETA: 1s - loss: 0.6136 - accuracy: 0.8518"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "210/782 [=======>......................] - ETA: 1s - loss: 0.6147 - accuracy: 0.8515"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "227/782 [=======>......................] - ETA: 1s - loss: 0.6246 - accuracy: 0.8501"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "244/782 [========>.....................] - ETA: 1s - loss: 0.6307 - accuracy: 0.8499"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "261/782 [=========>....................] - ETA: 1s - loss: 0.6372 - accuracy: 0.8481"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "278/782 [=========>....................] - ETA: 1s - loss: 0.6331 - accuracy: 0.8482"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "295/782 [==========>...................] - ETA: 1s - loss: 0.6365 - accuracy: 0.8475"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "311/782 [==========>...................] - ETA: 1s - loss: 0.6334 - accuracy: 0.8477"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "327/782 [===========>..................] - ETA: 1s - loss: 0.6360 - accuracy: 0.8468"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "344/782 [============>.................] - ETA: 1s - loss: 0.6323 - accuracy: 0.8482"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "360/782 [============>.................] - ETA: 1s - loss: 0.6288 - accuracy: 0.8493"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "376/782 [=============>................] - ETA: 1s - loss: 0.6295 - accuracy: 0.8492"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "393/782 [==============>...............] - ETA: 1s - loss: 0.6291 - accuracy: 0.8497"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "409/782 [==============>...............] - ETA: 1s - loss: 0.6337 - accuracy: 0.8488"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "425/782 [===============>..............] - ETA: 1s - loss: 0.6349 - accuracy: 0.8478"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "441/782 [===============>..............] - ETA: 1s - loss: 0.6318 - accuracy: 0.8484"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "458/782 [================>.............] - ETA: 1s - loss: 0.6295 - accuracy: 0.8487"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "474/782 [=================>............] - ETA: 0s - loss: 0.6322 - accuracy: 0.8485"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "490/782 [=================>............] - ETA: 0s - loss: 0.6300 - accuracy: 0.8490"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "506/782 [==================>...........] - ETA: 0s - loss: 0.6356 - accuracy: 0.8488"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "522/782 [===================>..........] - ETA: 0s - loss: 0.6340 - accuracy: 0.8490"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "538/782 [===================>..........] - ETA: 0s - loss: 0.6383 - accuracy: 0.8483"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "555/782 [====================>.........] - ETA: 0s - loss: 0.6395 - accuracy: 0.8476"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "572/782 [====================>.........] - ETA: 0s - loss: 0.6410 - accuracy: 0.8474"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "589/782 [=====================>........] - ETA: 0s - loss: 0.6392 - accuracy: 0.8474"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "606/782 [======================>.......] - ETA: 0s - loss: 0.6388 - accuracy: 0.8476"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "623/782 [======================>.......] - ETA: 0s - loss: 0.6384 - accuracy: 0.8477"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "639/782 [=======================>......] - ETA: 0s - loss: 0.6379 - accuracy: 0.8477"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "654/782 [========================>.....] - ETA: 0s - loss: 0.6356 - accuracy: 0.8480"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "670/782 [========================>.....] - ETA: 0s - loss: 0.6351 - accuracy: 0.8479"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "687/782 [=========================>....] - ETA: 0s - loss: 0.6363 - accuracy: 0.8478"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "703/782 [=========================>....] - ETA: 0s - loss: 0.6369 - accuracy: 0.8476"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "719/782 [==========================>...] - ETA: 0s - loss: 0.6368 - accuracy: 0.8478"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "735/782 [===========================>..] - ETA: 0s - loss: 0.6381 - accuracy: 0.8479"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "751/782 [===========================>..] - ETA: 0s - loss: 0.6387 - accuracy: 0.8480"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "768/782 [============================>.] - ETA: 0s - loss: 0.6392 - accuracy: 0.8478"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "782/782 [==============================] - 2s 3ms/step - loss: 0.6398 - accuracy: 0.8477\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.639793336391449, 0.8477200269699097]\n"
     ]
    }
   ],
   "source": [
    "results = model.evaluate(test_examples, test_labels)\n",
    "\n",
    "print(results)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "z1iEXVTR0Z2t"
   },
   "source": [
    "This fairly naive approach achieves an accuracy of about 87%. With more advanced approaches, the model should get closer to 95%."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5KggXVeL-llZ"
   },
   "source": [
    "## Create a graph of accuracy and loss over time\n",
    "\n",
    "`model.fit()` returns a `History` object that contains a dictionary with everything that happened during training:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:49:53.528921Z",
     "iopub.status.busy": "2022-12-14T12:49:53.528260Z",
     "iopub.status.idle": "2022-12-14T12:49:53.533905Z",
     "shell.execute_reply": "2022-12-14T12:49:53.533008Z"
    },
    "id": "VcvSXvhp-llb"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['loss', 'accuracy', 'val_loss', 'val_accuracy'])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "history_dict = history.history\n",
    "history_dict.keys()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "nRKsqL40-lle"
   },
   "source": [
    "There are four entries: one for each monitored metric during training and validation. We can use these to plot the training and validation loss for comparison, as well as the training and validation accuracy:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:49:53.537253Z",
     "iopub.status.busy": "2022-12-14T12:49:53.536712Z",
     "iopub.status.idle": "2022-12-14T12:49:53.706945Z",
     "shell.execute_reply": "2022-12-14T12:49:53.706168Z"
    },
    "id": "nGoYf2Js-lle"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "acc = history_dict['accuracy']\n",
    "val_acc = history_dict['val_accuracy']\n",
    "loss = history_dict['loss']\n",
    "val_loss = history_dict['val_loss']\n",
    "\n",
    "epochs = range(1, len(acc) + 1)\n",
    "\n",
    "# \"bo\" is for \"blue dot\"\n",
    "plt.plot(epochs, loss, 'bo', label='Training loss')\n",
    "# b is for \"solid blue line\"\n",
    "plt.plot(epochs, val_loss, 'b', label='Validation loss')\n",
    "plt.title('Training and validation loss')\n",
    "plt.xlabel('Epochs')\n",
    "plt.ylabel('Loss')\n",
    "plt.legend()\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-14T12:49:53.710185Z",
     "iopub.status.busy": "2022-12-14T12:49:53.709734Z",
     "iopub.status.idle": "2022-12-14T12:49:53.867179Z",
     "shell.execute_reply": "2022-12-14T12:49:53.866394Z"
    },
    "id": "6hXx-xOv-llh"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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xo0bo0GDBpg+fTp8fX3Ru3fvqtotIiIismCyJ0BRUVG4ceMGZsyYgYyMDLRt2xZbt27VDWJOS0uDjY1+R1VycjJ2796N33//3WCb7733HvLy8jB69Gjcvn0bnTt3xtatW+Hg4FDp+0NERESWT/Z5gCwR5wEiIiKqfqrNPEBEREREcmACRERERFaHCRARERFZHSZAREREZHWYABEREZHVYQJEREREVocJEBEREVkdJkBERERkdZgAERERkdVhAkRERERWhwkQERERWR0mQERERGR1mAARERGR1WECRERERFaHCRARERFZHSZAREREZHWYABEREZHVYQJEREREVocJEBEREVkdJkBERERkdZgAERERkdVhAkRERERWhwkQERERWR0mQERERGR1mAARERGR1WECRERERFaHCRARERFZHSZAREREZHWYABEREZHVYQJEREREVocJEBEREVkd2ROgRYsWISgoCA4ODggLC8PBgwdLrX/79m2MHTsWPj4+UKlUaNKkCbZs2aJ7fdasWVAoFHpLs2bNKns3iIiIqBqxlfPN165di5iYGCxZsgRhYWGIj49HZGQkkpOTUa9evWL1CwsL8dxzz6FevXpYv349/Pz8cOnSJbi7u+vVa9myJbZt26Zbt7WVdTeJiIjIwsiaGcybNw+jRo3CiBEjAABLlizB5s2bsWzZMkyZMqVY/WXLluHWrVvYu3cv7OzsAABBQUHF6tna2sLb27tSYyciIqLqS7ZTYIWFhTh06BAiIiIeBGNjg4iICOzbt8/gNj///DM6duyIsWPHwsvLC61atcLHH38MtVqtV+/cuXPw9fVFw4YNMWTIEKSlpVXqvhAREVH1IlsPUFZWFtRqNby8vPTKvby8cObMGYPbXLhwAX/88QeGDBmCLVu24Pz583jzzTdRVFSEmTNnAgDCwsKwYsUKNG3aFOnp6Zg9ezbCw8Nx8uRJ1KpVy2C7BQUFKCgo0K3n5OSYaS+JiIjIElWrwTEajQb16tXD119/DaVSidDQUFy9ehVz587VJUDdu3fX1W/dujXCwsIQGBiIH3/8ESNHjjTYblxcHGbPnl0l+0BERETyk+0UmIeHB5RKJTIzM/XKMzMzSxy/4+PjgyZNmkCpVOrKmjdvjoyMDBQWFhrcxt3dHU2aNMH58+dLjCU2NhbZ2dm65fLly+XYIyIiIqouZOsB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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.clf()   # clear figure\n",
    "\n",
    "plt.plot(epochs, acc, 'bo', label='Training acc')\n",
    "plt.plot(epochs, val_acc, 'b', label='Validation acc')\n",
    "plt.title('Training and validation accuracy')\n",
    "plt.xlabel('Epochs')\n",
    "plt.ylabel('Accuracy')\n",
    "plt.legend()\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "oFEmZ5zq-llk"
   },
   "source": [
    "In this plot, the dots represent the training loss and accuracy, and the solid lines are the validation loss and accuracy.\n",
    "\n",
    "Notice the training loss *decreases* with each epoch and the training accuracy *increases* with each epoch. This is expected when using a gradient descent optimization—it should minimize the desired quantity on every iteration.\n",
    "\n",
    "This isn't the case for the validation loss and accuracy—they seem to peak after about twenty epochs. This is an example of overfitting: the model performs better on the training data than it does on data it has never seen before. After this point, the model over-optimizes and learns representations *specific* to the training data that do not *generalize* to test data.\n",
    "\n",
    "For this particular case, we could prevent overfitting by simply stopping the training after twenty or so epochs. Later, you'll see how to do this automatically with a callback."
   ]
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [],
   "name": "basic-text-classification.ipynb",
   "private_outputs": true,
   "provenance": [],
   "toc_visible": true
  },
  "kernelspec": {
   "display_name": "Python 3",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}

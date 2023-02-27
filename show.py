{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a56eee08",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/env python3\n",
    "# -*- coding: utf-8 -*-\n",
    "\n",
    "import random\n",
    "\n",
    "with open(\"./hyakunin.txt\", encoding=\"utf-8\") as f:\n",
    "    wakas = [s.strip() for s in f.readlines()]\n",
    "\n",
    "print(wakas[random.randrange(len(wakas))])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

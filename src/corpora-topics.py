import os
import urllib
from xml.dom.minidom import parse, getDOMImplementation
import xml.dom.minidom
import gensim
import scipy
import pandas
from collections import defaultdict
from pprint import pprint


def cleanedCorpus(string):
    """ Generates """
    DOMTree = xml.dom.minidom.parse(urllib.urlopen(string))
                                               
    entries = DOMTree.getElementsByTagName("entry")
    abstracts = []
    
    # clean documents of punctuation and prepositions and then store unique words
    for entry in entries:
        cleaned = entry.getElementsByTagName("summary")[0].firstChild.data
        cleaned = "".join(c for c in cleaned if c not in ('!', '.', ","))
        abstracts.append(cleaned)
    
    stoplist = set('is that this are should when which or an two we if new results  = leq theory show not it all may one such there be for a of the and to in by with on at from about as through after over without before under'.split())
    texts = [[word for word in abstract.lower().split() if word not in stoplist] for abstract in abstracts]
        
    return texts
    
def cleanToMm(texts, snippet):
    """ Takes cleaned DOM Object and returns array of Market Matrix Object and its dictionary"""
        # tokenize unique words
    dictionary = gensim.corpora.Dictionary(texts)
    path = "\tmp\_" + snippet
    dictionary.save(path + ".dict")
    
    # convert docs to vectorized corpus
    vec_corpus = [dictionary.doc2bow(text) for text in texts]
    
    # and save it in Market Matrix format
    gensim.corpora.MmCorpus.serialize(path + ".mm", vec_corpus)
    mmCorpus = gensim.corpora.MmCorpus(path + ".mm")

    return [mmCorpus, dictionary]

def main():
    
    corpus = cleanedCorpus("http://export.arxiv.org/api/query?search_query=cat:math.LO+OR+cat:astro-ph+OR+cat:stat.TH&start=0&max_results=100")
    mmCorpus = cleanToMm(corpus, "electron")
    


    # generate latent semantic index
    lsi = gensim.models.LsiModel(corpus=mmCorpus[0], id2word=mmCorpus[1], num_topics=6)
    
    pprint(lsi.print_topics(num_topics=6, num_words=6))
    print("============================================")
    
    """
    automata = cleanedCorpus("http://export.arxiv.org/api/query?search_query=all:automata&start=0&max_results=15")
    mmAutomata = cleanToMm(corpus, "automata")
    mmCorpus[1].merge_with(mmAutomata[1])
    lsi.id2word=mmCorpus[1]
    lsi.add_documents(mmAutomata[0])
    
    pprint(lsi.print_topics(num_topics=5, num_words=6))
    """
main()

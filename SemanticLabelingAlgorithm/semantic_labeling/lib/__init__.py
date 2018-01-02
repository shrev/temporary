from elasticsearch import Elasticsearch

import os
import sys

sys.path.append(os.getcwd()+"/../search")

from indexer import Indexer
from searcher import Searcher

__author__ = 'alse'
elastic_search = Elasticsearch()
indexer = Indexer(elastic_search)
searcher = Searcher(elastic_search)

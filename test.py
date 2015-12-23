from optparse import OptionParser
from digSparkUtil.dictUtil import as_dict, dict_minus
from pyspark import SparkContext
import json
import ast

def test(inputFile,outpuFile,**kwargs):
    options = {"numHashes":kwargs.get("numHashes",100) ,
               "numItemsInBand": kwargs.get("numItemsInBand",10),
               "computeSimilarity": kwargs.get("computeSimilarity",False),
               "computeIdenticalClusters":kwargs.get("computeIdenticalClusters",False),
               "threshold":kwargs.get("threshold",0.0),
               "base":kwargs.get("base",""),
               "topk":kwargs.get("topk",""),
               "numPartitions":kwargs.get("numPartitions",10),
               "candidatesName":kwargs.get("candidatesName","candidates")
               }
    for key,value in options.iteritems():
        print key,value

def f(x):
    print x
    #cluster_data = ast.literal_eval(x[1])
    #print json.loads(x[1])['cluster']


def test2():
    sc = SparkContext()
    rdd = sc.textFile('/Users/rajagopal/Desktop/github_repos/dig-unicode/ht_data/LSH/clusters2')
    rdd.foreach(f)


if __name__ == '__main__':

    '''#input to this is always a sequencefile of type json
    parser = OptionParser()
    #arguments for minhashing
    parser.add_option("-n", "--numHashes", dest="numHashes", type="int",
                      help="number of minhashes", default=100)
    parser.add_option("-b", "--numItemsInBand", dest="numItemsInBand", type="int",
                      help="number of items in each band", default=10)

    #arguments for clustering
    parser.add_option("-s", "--computeSimilarity", action="store_true",
                      dest="computeSimilarity", default=False, help="compute similarity")
    parser.add_option("-j", "--computeIdenticalClusters", action="store_true",
                      dest="computeIdenticalClusters", default=False, help="compute identical clusters")
    parser.add_option("-t", "--threshold", type="float",
                      dest="threshold", default=0.0, help="similarity threshold")
    parser.add_option("-e", "--base", dest="base", type="string",
                      help="base file", default="")
    parser.add_option("-k", "--topk", dest="topk", type="int",
                      help="top n matches", default=3)
    parser.add_option("-x", "--numPartitions", dest="numPartitions", type="int",
                      help="number of partitions", default=10)
    parser.add_option("-z", "--candidatesName", dest="candidates_name", type="string",
                        help="name for json element for matching candidates", default="candidates")

    (c_options, args) = parser.parse_args()
    c_options.threshold=0.1
    kwargs = as_dict(c_options)
    test(None,None,**kwargs)
        '''
    test2()
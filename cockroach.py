#!/usr/bin/python
from kazoo.client import KazooClient

class Topic(object):
    def __init__(self,name):
        self.name=name
        self.parititions=[]

class Offset(object):
    def __init__(self,topic,partition,KazooClient()):
        self.topic=topic
        self.partition=partition
        self.offset=offset

class Consumer(object):
    def __init__(self,id,zk_client):
        self.id=id
        self.version=id
        subcscriptions[]

class ConsumerGroup(object):
    def __init__(self,gid,KazooClient()):
        self.gid=gid    
        self.zk_client=zk_client
        self.offsets=self.get_offsets()
        self.owners=self.get_owners()
        self.consumers=self.get_consumers()

    def get_owners(self):
        owners=[]
        for topic in self.zk_client.get_children("/consumers/%s/owners" % (self.gid) )
            for partition in self.zk_client.get_children("/consumers/%s/owners/%s" % (self.gid,topic,partition) )

    def get_offsets(self):
        offsets=[]
        for topic in self.zk_client.get_children("/consumers/%s/offsets" % (self.gid) ):
            for partition_id in self.zk_client.get_children("/consumers/%s/offsets/%s" % (self.gid,topic))
                offsets.add(Offset(topic,parttion))
        return offsets
            
class CockRroach(object):
    def __init__(self,zkHost):
        self.ConsumerGroups=[]
        self.zk_client=KazooClient(hosts=zkHost)
        self.zk_client.start()
        if self.zk_client.exists("/consumers"):
          for cg_name in self.zk_client.get_children("/consumers"):
            ConsumerGroups.add(ConsumerGroup(cg_name,self.zk))
           
    
if __name__ == '__main__' :
    import argparse

    count=0

    parser = argparse.ArgumentParser(description="Cleanup stale consumer groups from ZooKeeper")
    parser.add_argument('zk', help="zookeeper host",default="aquzoosys031010.c031.digitalriverws.net:2182")

    args = parser.parse_args()
    topic=HDFS_topic(topic=args.topic,user=args.hdfs_user,server=args.hdfs_server,port=args.hdfs_port,\
                     hdfs_tmp=args.hdfs_tmp,web_port=args.web_port,base=args.base)
    try:
        topic.merge(args.start,args.end)
    except Exception as err:
        print err
        exit



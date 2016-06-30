#!/usr/bin/python
from kazoo.client import KazooClient

class Topic(object):
    def __init__(self,name):
        self.name=name
        self.parititions=[]

class Offset(object):
    def __init__(self,Topic,zk_client):
        self.topic=Topic

class Consumer(object):
    def __init__(self,id,zk_client):
        self.id=id
        self.version=id
        subcscriptions[]

class ConsumerGroup(object):
    def __init__(self,gid,zk_client):
        self.gid=gid    
        self.offsets=self.get_offsets()
        self.owners=self.get_owners()
        self.consumers=self.get_consumers()

class ConsumerGroups(object):
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



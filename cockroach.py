#!/usr/bin/python
from kazoo.client import KazooClient
from datetime import datetime

class Topic(object):
    def __init__(self,name):
        self.name=name
        self.parititions=[]

class Offset(object):
    def __init__(self,topic,partition,offset,mtime):
        self.topic=topic
        self.partition=partition
        self.offset=offset
        self.mtime=datetime.fromtimestamp(mtime/1000)

    def __str__(self):
        return "Offset-->topic:%s,partition:%s,offset:%s, last seen: %s\n" % \
               (self.topic,self.partition,self.offset,self.mtime)

class Consumer(object):
    def __init__(self,id,KazooClient):
        self.id=id
        self.version=id
        subcscriptions=[]

class ConsumerGroup(object):
    def __init__(self,gid,KazooClient):
        self.gid=gid    
        self.zk_client=KazooClient;
        self.offsets=self.get_offsets()
    #    self.owners=self.get_owners()
    #    self.consumers=self.get_consumers()

    def __str__(self):
        ret= "CG: %s last seen: %s\n" % (self.gid,self.last_seen())
        for offset in self.offsets:
            ret += "--offset: %s/%s %s mtime: %s\n" % (offset.topic,offset.partition, offset.offset,offset.mtime)

        return ret

    def last_seen(self):
        if len(self.offsets):
            last_seen=self.offsets[0]
        else:
            last_seen=Offset("None",None,None,1)

        for offset in self.offsets:
            if offset.mtime > last_seen.mtime:
                last_seen=offset

        #print "Last seen: %s"  % (last_seen)
        return last_seen
        
    def get_offsets(self):
        offsets=[]
        #print "Processing %s", self.gid
        if self.zk_client.exists("/consumers/%s/offsets" % (self.gid) ):
           for topic in self.zk_client.get_children("/consumers/%s/offsets" % (self.gid) ):
               for partition_id in self.zk_client.get_children("/consumers/%s/offsets/%s" % (self.gid,topic)):
                   (data,stat)=self.zk_client.get("/consumers/%s/offsets/%s/%s" % (self.gid,topic,partition_id))
                   offsets.append(Offset(topic,partition_id,data,stat.mtime))

        return offsets

    #def get_owners(self):
    #    owners=[]
    #    for topic in self.zk_client.get_children("/consumers/%s/owners" % (self.gid) ):
    #        for partition in self.zk_client.get_children("/consumers/%s/owners/%s" % (self.gid,topic,partition) ):
    #            pass
            
class CockRoach(object):
    def __init__(self,zkHost):
        self.ConsumerGroups=[]
        self.zk_client=KazooClient(hosts=zkHost)
        self.zk_client.start()
        if self.zk_client.exists("/consumers"):
          for cg_name in self.zk_client.get_children("/consumers"):
            self.ConsumerGroups.append(ConsumerGroup(cg_name,self.zk_client))


    def __str__(self):
        ret=""
        for consumer in self.ConsumerGroups:
            ret += "%s\n" % (consumer)
        return ret

    
if __name__ == '__main__' :
    import argparse

    count=0

    parser = argparse.ArgumentParser(description="Cleanup stale consumer groups from ZooKeeper")
    parser.add_argument('zk', help="zookeeper host",default="aquzoosys031010.c031.digitalriverws.net:2182")

    args = parser.parse_args()
    cockroach=CockRoach(zkHost="aquzoosys031010:2182")
    print "CockRoach: %s" % (cockroach)

#!/usr/bin/python
""" Simple Zookeeper/Kafka library """
from kazoo.client import KazooClient
from datetime import datetime

class Topic(object):
    """ Defines Topic object """
    def __init__(self, name):
        self.name = name
        self.parititions=[]

class Offset(object):
    """ Offset class describes offset for a topic/partition on zookeeper """"
    def __init__(self, topic, partition, offset, mtime):
        self.topic = topic
        self.partition = partition
        self.offset = offset
        self.mtime = datetime.fromtimestamp(mtime/1000)

    def __str__(self):
        return "Offset-->topic:%s,partition:%s,offset:%s, last seen: %s\n" % \
               (self.topic, self.partition, self.offset, self.mtime)

class Consumer(object):
    """ Consumer class describes a consumer registered on zk """
    def __init__(self, cid, KazooClient):
        self.cid = cid
        self.version = cid
        subcscriptions = []

class ConsumerGroup(object):
    """ ConsumerGroup class describes a KafkaConsumer group stored on Zookeeper """
    def __init__(self, gid, KzClient):
        self.gid = gid
        self.zk_client = KzClient
        self.offsets = self.get_offsets()
    #    self.owners=self.get_owners()
    #    self.consumers=self.get_consumers()

    def __str__(self):
        ret = "CG: %s last seen: %s\n" % (self.gid, self.last_seen())
        #for offset in self.offsets:
        #    ret += "--offset: %s/%s %s mtime: %s\n" % (offset.topic,offset.partition, offset.offset,offset.mtime)
        return ret

    def last_seen(self):
        """ Last seen method returns when a consumer group was last used by any consumer """
        if len(self.offsets):
            last_seen = self.offsets[0]
        else:
            last_seen = Offset("None", None, None, 1)

        for offset in self.offsets:
            if offset.mtime > last_seen.mtime:
                last_seen = offset

        #print "Last seen: %s"  % (last_seen)
        return last_seen

    def get_offsets(self):
        """ get_offsets method returns offsets for each/topic partition for the ConsumerGroup"""
        offsets = []
        #print "Processing %s", self.gid
        if self.zk_client.exists("/consumers/%s/offsets" % (self.gid)):
           for topic in self.zk_client.get_children("/consumers/%s/offsets" % (self.gid)):
               for partition_id in self.zk_client.get_children("/consumers/%s/offsets/%s" % (self.gid, topic)):
                   (data, stat) = self.zk_client.get("/consumers/%s/offsets/%s/%s" % (self.gid, topic, partition_id))
                   offsets.append(Offset(topic, partition_id, data, stat.mtime))

        return offsets

    #def get_owners(self):
    #    owners=[]
    #    for topic in self.zk_client.get_children("/consumers/%s/owners" % (self.gid) ):
    #        for partition in self.zk_client.get_children("/consumers/%s/owners/%s" % (self.gid,topic,partition) ):
    #            pass

class CockRoach(object):
    def __init__(self, zkHost):
        self.ConsumerGroups = []
        self.zk_client = KazooClient(hosts=zkHost)
        self.zk_client.start()
        self.stale_max_days = 30
        if self.zk_client.exists("/consumers"):
            for cg_name in self.zk_client.get_children("/consumers"):
                self.ConsumerGroups.append(ConsumerGroup(cg_name, \
                                                         self.zk_client))

    def get_stale_cgroups(self):
        """get_stale_cgroups returns ConsumerGroups that were not used for stale_max_days""""
        ret = []
        for cg in self.ConsumerGroups:
            delta = datetime.now() - cg.last_seen().mtime
            if delta.days > self.stale_max_days:
                print "Stale: %s" % (cg)
                ret.append(cg)
        return ret

    def __str__(self):
        ret = ""
        for consumer in self.ConsumerGroups:
            ret += "%s" % (consumer)
        return ret


if __name__ == '__main__':
    import argparse

    count = 0

    parser = argparse.ArgumentParser(description=\
                                     "Cleanup stale consumer groups from ZooKeeper")
    parser.add_argument('zk', help = "zookeeper host", default = "aquzoosys031010.c031.digitalriverws.net:2182")

    args = parser.parse_args()
    cockroach = CockRoach(zkHost="aquzoosys031010:2182")
#    print "CockRoach: %s" % (cockroach)
    cockroach.get_stale_cgroups()

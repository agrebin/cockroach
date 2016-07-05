#!/usr/bin/python
""" Simple Zookeeper/Kafka library """
__author__ = "Adrian Grebin <adrian.grebin@gmail.com>"
from kazoo.client import KazooClient
from datetime import datetime

class Topic(object):
    """ Defines Topic object """
    def __init__(self, name):
        self.name = name
        self.parititions=[]

class Offset(object):
    """ Offset class describes offset for a topic/partition on zookeeper """
    def __init__(self, topic, partition, offset, mtime):
        self.topic = topic
        self.partition = partition
        self.offset = offset
        self.mtime = datetime.fromtimestamp(mtime/1000)

    def __str__(self):
        return "Offset-->topic:%s,partition:%s,offset:%s, last seen: %s" % \
               (self.topic, self.partition, self.offset, self.mtime)

class Consumer(object):
    """ Consumer class describes a consumer registered on zk """
    def __init__(self, cid, KazooClient):
        self.cid = cid
        self.version = cid
        subcscriptions = []

class ConsumerGroup(object):
    """ ConsumerGroup class describes a KafkaConsumer group stored on Zookeeper """
    def __init__(self, gid, KzClient, show_offsets=False):
        self.gid = gid
        self.zk_client = KzClient
        self.offsets = self.get_offsets()
        self.show_offsets = show_offsets
    #    self.owners=self.get_owners()
    #    self.consumers=self.get_consumers()

    def __str__(self):
        ret = "CG: %s last seen: %s" % (self.gid, self.last_seen())
        if self.show_offsets:
            for offset in self.offsets:
                ret += "--offset: %s/%s %s mtime: %s" % (offset.topic,offset.partition, offset.offset,offset.mtime)
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
    def __init__(self, zkHost, stale_max_days=30, assume_yes=False, preview=False):
        self.ConsumerGroups = []
        self.zk_client = KazooClient(hosts=zkHost)
        self.zk_client.start()
        self.stale_max_days = stale_max_days
        self.assume_yes = assume_yes
        self.preview = preview
        if self.zk_client.exists("/consumers"):
            for cg_name in self.zk_client.get_children("/consumers"):
                self.ConsumerGroups.append(ConsumerGroup(cg_name, \
                                                         self.zk_client))

    def get_stale_cgroups(self, display):
        """
           get_stale_cgroups returns ConsumerGroups
           that were not used for stale_max_days
        """
        ret = []
        for consumergroup in self.ConsumerGroups:
            delta = datetime.now() - consumergroup.last_seen().mtime
            if delta.days > self.stale_max_days:
                if display:
                    print "Stale: %s" % (consumergroup)
                ret.append(consumergroup)
        return ret

    def delete_stale_cgroups(self):
        """ Delete consumer groups that are considered stale"""
        stale_cgroups = self.get_stale_cgroups(display=False)
        for stale_cg in stale_cgroups:
            print stale_cg
            if self.assume_yes is False:
                confirm = raw_input("Delete?")
            else:
                confirm = "Y"

            if confirm == "Y":
                self.delete_cgroup(stale_cg)

    def delete_cgroup(self, consumergroup):
        """Deletes a consumer Group"""
        print "Deleting %s" % (consumergroup.gid)
        if self.preview is False:
          self.zk_client.delete("/consumers/%s" % (consumergroup.gid), version=-1, recursive=True)
          print "executed"
        else:
            print "pass"


    def __str__(self):
        ret = ""
        for consumer in self.ConsumerGroups:
            ret += "%s" % (consumer)
        return ret


if __name__ == '__main__':
    import argparse

    argparser = argparse.ArgumentParser(description=\
                                     "Cleanup stale consumer groups from ZooKeeper")
    argparser.add_argument('zk', help="zookeeper host", default="aquzoosys031010.c031.digitalriverws.net:2182")
    argparser.add_argument('--stale', help="Search for Stale ConsumerGroups (just print)", default=False, action='store_true')
    argparser.add_argument('--delete_stale', help="Delete Stale ConsumerGroups", default=False, action='store_true')
    argparser.add_argument('--stale_max_days', type=int, help="Define after how many days a CG is considered stale", default=30)
    argparser.add_argument('--YES', help="Assume Yes on all questions", default=False, action='store_true')
    argparser.add_argument('--preview', help="Do not execute any modifications", default=False, action='store_true')

    args = argparser.parse_args()
    cockroach = CockRoach(zkHost=args.zk, stale_max_days=args.stale_max_days, assume_yes=args.YES, preview=args.preview)

    if args.stale:
        cockroach.get_stale_cgroups(display=True)
    elif args.delete_stale:
        cockroach.delete_stale_cgroups()
    else:
        print "CockRoach: %s" % (cockroach)

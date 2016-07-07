# CockRoach
## Python tool/api to manage Kafka clusters
CockRoach is intended to provide an easy way to manage and automate Kafka clusters maintenance from command line or as an API.

Each time a kafka consumer is registered through a Consumer Group, it gets registered on Kafka's Zookeper store, and it never gets removed, it starts to build up and makes difficult to find inromation about it.

CockRoach at this point has implemented methods to list stale groups (and also delete them if necessary) based on the modification time of the latest offset consumed on each of the topics handled by that Consumer Group.

## Requirements:
Requires python 2.7+, kazoo
Just pip install -r requirements.txt

## Running cli and parameters
    usage: cockroach.py [-h] [--stale] [--delete_stale]
                        [--stale_max_days STALE_MAX_DAYS] [--YES] [--preview]
                        zk
    
    Cleanup stale consumer groups from ZooKeeper
    
    positional arguments:
      zk                    zookeeper host
    
    optional arguments:
      -h, --help            show this help message and exit
      --stale               Search for Stale ConsumerGroups (just print)
      --delete_stale        Delete Stale ConsumerGroups
      --stale_max_days STALE_MAX_DAYS
                            Define after how many days a CG is considered stale
      --YES                 Assume Yes on all questions
      --preview             Do not execute any modifications

## SAMPLE RUN
-bash-4.2$ ./cockroach.py  aquzoosys031010:2182
Stale: CG: console-consumer-71425 last seen: Offset-->topic:Subscriptions.Arctic.usageSubscriptionReceivedPaymentForUsageStatement,partition:3,offset:14, last seen: 2016-02-26 20:05:17
Stale: CG: console-consumer-86181 last seen: Offset-->topic:drwp_payments,partition:0,offset:3408061, last seen: 2015-11-18 21:44:06
Stale: CG: logitech-read-2 last seen: Offset-->topic:gc_rum_raw,partition:26,offset:18753964, last seen: 2016-04-20 13:06:28
Stale: CG: console-consumer-79279 last seen: Offset-->topic:jetstream-agg,partition:7,offset:16528141, last seen: 2016-02-02 17:49:25
Stale: CG: mark_read last seen: Offset-->topic:gc_rum,partition:3,offset:47221675, last seen: 2015-09-14 21:27:18
Stale: CG: console-consumer-90019 last seen: Offset-->topic:Subscriptions.Arctic.usageSubscriptionReceivedPaymentForUsageStatement,partition:3,offset:14, last seen: 2016-02-26 19:07:09
Stale: CG: console-consumer-1618 last seen: Offset-->topic:ms_pv_fiveminutes,partition:18,offset:2, last seen: 2015-11-18 21:44:00
Stale: CG: gc_rum_test_local2 last seen: Offset-->topic:gc_rum,partition:2,offset:16340694, last seen: 2015-08-05 20:57:27
Stale: CG: gc_rum_test_local3 last seen: Offset-->topic:gc_rum,partition:6,offset:21844162, last seen: 2015-08-10 15:58:14
Stale: CG: console-consumer-67828 last seen: Offset-->topic:drwp-transactions,partition:48,offset:187543, last seen: 2016-02-18 15:13:00
Stale: CG: gc_rum_test_local4 last seen: Offset-->topic:gc_rum,partition:3,offset:22689053, last seen: 2015-08-10 18:45:23
Stale: CG: flume-mirror-channel last seen: Offset-->topic:drwp-iso-prd-mirrored,partition:0,offset:692953, last seen: 2015-09-22 16:12:22
Stale: CG: console-consumer-92592 last seen: Offset-->topic:gc_pv_fiveminutes,partition:0,offset:6482, last seen: 2015-09-17 20:18:25
Stale: CG: schema-registry-bschulteVB-8081 last seen: Offset-->topic:None,partition:None,offset:None, last seen: 1970-01-01 00:00:00
Stale: CG: kettle_sys_group_test last seen: Offset-->topic:gc_rum_raw,partition:32,offset:564011, last seen: 2015-09-03 00:23:03
Stale: CG: console-consumer-57816 last seen: Offset-->topic:Subscriptions.Arctic.usageSubscriptionProvision,partition:2,offset:140, last seen: 2016-02-19 19:03:09
Stale: CG: console-consumer-27659 last seen: Offset-->topic:gc_pv,partition:0,offset:7322, last seen: 2015-08-21 17:06:49
Stale: CG: GDFJDLFJ_100 last seen: Offset-->topic:gc_rum_raw,partition:19,offset:18764606, last seen: 2016-04-12 18:48:28
Stale: CG: console-consumer-11239 last seen: Offset-->topic:gc_pv,partition:0,offset:221191, last seen: 2015-09-11 18:05:21
Stale: CG: console-consumer-67031 last seen: Offset-->topic:gc_pv,partition:5,offset:69, last seen: 2015-08-20 22:09:01
Stale: CG: console-consumer-47349 last seen: Offset-->topic:Subscriptions.Arctic.pricelockSubscriptionRenewal,partition:2,offset:3556, last seen: 2016-05-04 14:31:54
Stale: CG: onramp1 last seen: Offset-->topic:gc_rum,partition:2,offset:44039904, last seen: 2015-09-17 21:28:27
Stale: CG: onramp last seen: Offset-->topic:gc_rum_replay,partition:1,offset:25, last seen: 2015-04-27 15:36:06
Stale: CG: console-consumer-16985 last seen: Offset-->topic:gc_rum_k,partition:0,offset:1186188, last seen: 2015-08-06 21:59:32
Stale: CG: flume-sys last seen: Offset-->topic:gc_rum_raw,partition:46,offset:11134721, last seen: 2016-02-16 20:19:02
Stale: CG: cdm-read-2 last seen: Offset-->topic:drwp-transactions,partition:12,offset:31227, last seen: 2015-10-16 11:40:28
Stale: CG: onramplocal last seen: Offset-->topic:gc_rum,partition:5,offset:110070938, last seen: 2016-02-26 20:41:56
Stale: CG: MARK_READ_890 last seen: Offset-->topic:gc_rum_enriched_out,partition:2,offset:5503, last seen: 2016-01-12 04:41:44
Stale: CG: TEST_TEST last seen: Offset-->topic:gc_rum_enriched_in,partition:29,offset:12822, last seen: 2016-01-27 20:55:13
Stale: CG: event_stream_processor last seen: Offset-->topic:gc_rum,partition:0,offset:487967943, last seen: 2015-07-10 21:54:45
Stale: CG: console-consumer-71516 last seen: Offset-->topic:Subscriptions.Arctic.pricelockSubscriptionCancel,partition:2,offset:28, last seen: 2016-04-21 18:44:44
Stale: CG: mark_test_read last seen: Offset-->topic:drwp-iso,partition:3,offset:400, last seen: 2015-09-17 16:32:01
Stale: CG: MARK_READ_889 last seen: Offset-->topic:gc_rum_enriched_out,partition:27,offset:6292, last seen: 2016-01-11 23:45:37
Stale: CG: 1 last seen: Offset-->topic:None,partition:None,offset:None, last seen: 1970-01-01 00:00:00
Stale: CG: console-consumer-62196 last seen: Offset-->topic:drwp-iso,partition:3,offset:400, last seen: 2016-05-13 17:19:52

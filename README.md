# EXAMPLE README FROM ANOTHER REPO
# Snappymerge
## Python tool to merge files in hdfs flume topics to save hdfs storage space (author: Adrian Grebin <agrein@digitalriver.com>)

## Requirements:
Requires python 2.7+,python-hdfs,snakebite and dateutils: you can run sudo pip install -r requirements.txt to meet them

## SUMMARY
	usage: snappymerge.py [-h] [--hdfs_user HDFS_USER] [--hdfs_server HDFS_SERVER]
	                      [--hdfs_port HDFS_PORT] [--hdfs_tmp HDFS_TMP]
	                      [--web_port WEB_PORT] [--base BASE] [--start START]
	                      [--end END]
	                      topic
	
	Merge daily historical snappy files into one to save hdfs space
	
	positional arguments:
	  topic                 Topic name relative to --base
	
	optional arguments:
	  -h, --help            show this help message and exit
	  --hdfs_user HDFS_USER
	                        HDFS user name (default: current user)
	  --hdfs_server HDFS_SERVER
	                        HDFS server name or ip (default:
	                        aquhmstsys022001.c022.digitalriverws.net)
	  --hdfs_port HDFS_PORT
	                        HDFS server port number (default:8020)
	  --hdfs_tmp HDFS_TMP   HDFS temporary dir to store files to be merged
	                        (default:/user/hduser/tmp)
	  --web_port WEB_PORT   HDFS server WEB port number (default:50070)
	  --base BASE           Alternate hdfs base path for topic
	                        (default:/user/aqueduct/flume)
	  --start START         Start Date inclusive (default: from beginning)
	  --end END             End Date inclusive (default: to end)

## SAMPLE RUN
	-bash-4.2$ ./snappymerge.py gc_rum --base /user/hduser
	INFO: Trying to merge gc_rum from 2016-5-24 to 2016-5-31

	INFO: processing  2016-5-24
	INFO: DAYPATH:  ['/user/hduser/gc_rum/2016-5-24/']
	INFO: MERGING  /user/hduser/gc_rum/2016-5-24/
	[]
	INFO: DELETING original files in  /user/hduser/gc_rum/2016-5-24/
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-24/gc_rum-2016-05-23.1464044404729.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-24/gc_rum-2016-05-24.1464048000674.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-24/gc_rum-2016-05-24.1464048000675.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-24/gc_rum-2016-05-24.1464048000676.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-24/gc_rum-2016-05-24.1464048000677.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-24/gc_rum-2016-05-24.1464048000678.snappy
	INFO: UPLOADING merged (./2016-01-06.754369-merged.snappy) to /user/hduser/gc_rum/2016-5-24/
	WARNING: 2016-05-25 not found in gc_rum, trying next day
	WARNING: 2016-05-26 not found in gc_rum, trying next day
	WARNING: 2016-05-27 not found in gc_rum, trying next day
	WARNING: 2016-05-28 not found in gc_rum, trying next day
	WARNING: 2016-05-29 not found in gc_rum, trying next day
	INFO: processing  2016-5-30
	INFO: DAYPATH:  ['/user/hduser/gc_rum/2016-5-30/']
	INFO: MERGING  /user/hduser/gc_rum/2016-5-30/
	[]
	INFO: DELETING original files in  /user/hduser/gc_rum/2016-5-30/
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-30/gc_rum-2016-05-29.1464562806989.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-30/gc_rum-2016-05-30.1464566401621.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-30/gc_rum-2016-05-30.1464566401622.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-30/gc_rum-2016-05-30.1464566401623.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-30/gc_rum-2016-05-30.1464566401624.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-30/gc_rum-2016-05-30.1464566401625.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-30/gc_rum-2016-05-30.1464566401626.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-30/gc_rum-2016-05-30.1464566401627.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-30/gc_rum-2016-05-30.1464566401628.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-30/gc_rum-2016-05-30.1464566401629.snappy
	INFO: Deleting original file  /user/hduser/gc_rum/2016-5-30/gc_rum-2016-05-30.1464566401630.snappy
	INFO: UPLOADING merged (./2016-01-06.919472-merged.snappy) to /user/hduser/gc_rum/2016-5-30/
	INFO: processing  2016-5-31
	INFO: DAYPATH:  ['/user/hduser/gc_rum/2016-5-31/']
	WARNING: ['/user/hduser/gc_rum/2016-5-31/'] contains a non snappy file (/user/hduser/gc_rum/2016-5-31/gc_rum-2016-05-31.1464652803133.snappy._COPYING_), moving *snappy to /user/hduser/tmp/snappymerge-2016-5-31-tmp getmerge there

	INFO: MOVING files to  /user/hduser/tmp/snappymerge-2016-5-31-tmp
	[]
	INFO: MERGING files in  /user/hduser/tmp/snappymerge-2016-5-31-tmp
	[]
	INFO: UPLOADING merged (./2016-01-06.028256-merged.snappy) to /user/hduser/gc_rum/2016-5-31/
	INFO: Deleting files on  /user/hduser/tmp/snappymerge-2016-5-31-tmp


#!/usr/bin/env bash

hadoop jar ../hadoop-streaming-2.7.3.jar \
-D  mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D  mapreduce.partition.keycomparator.options="-k1 -k2" \
-D mapreduce.partition.keypartitioner.options="-k1" \
-D  num.key.fields.for.partition=1 \
-D  stream.num.map.output.key.field=1 \
-input /data/assignments/ex2/part1/large/ \
-output /user/s1308424/assignment2/task1/ \
-mapper mapper.py \
-file mapper.py \
-combiner combiner.py \
-file combiner.py \
-reducer reducer.py \
-file reducer.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


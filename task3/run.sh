#!/usr/bin/env bash

hadoop jar ../hadoop-streaming-2.7.3.jar \
-D  mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D  mapreduce.partition.keypartitioner.options="-k1nr" \
-D  mapreduce.partition.keycomparator.options="-k1nr" \
-D  stream.num.map.output.key.field=1 \
-D  num.key.fields.for.partition=1 \
-input ../data/part2/stackLarge.txt \
-output output1 \
-mapper mapper.py \
-file mapper.py \
-combiner combiner.py \
-file combiner.py \
-reducer reducer.py \
-file reducer.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


hadoop jar ../hadoop-streaming-2.7.3.jar \
-D  mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D  mapreduce.partition.keycomparator.options="-k1nr" \
-D  stream.num.map.output.key.field=1 \
-input output1 \
-output output2 \
-mapper mapper2.py \
-file mapper2.py \
-combiner combiner.py \
-file combiner.py \
-reducer reducer.py \
-file reducer.py

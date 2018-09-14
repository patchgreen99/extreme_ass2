#!/usr/bin/env bash

hadoop jar ../hadoop-streaming-2.7.3.jar \
-D  mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D  mapreduce.partition.keypartitioner.options=-k1,1 \
-D  mapreduce.partition.keycomparator.options=-k1,1nr \
-D  stream.num.map.output.key.field=1 \
-D  mapred.reduce.tasks=1 \
-input ../data/part2/stackSmall.txt \
-output output/ \
-mapper mapper.py \
-file mapper.py \
-combiner "head -n 10" \
-reducer "head -n 10"
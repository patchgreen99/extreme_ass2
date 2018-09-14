#!/usr/bin/env bash

hadoop jar ../hadoop-streaming-2.7.3.jar \
-D  mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D  num.key.fields.for.partition=1 \
-D  mapreduce.map.output.field.seperator="." \
-D  mapreduce.partition.keycomparator.options="-k1,1n -k2,2n" \
-D  stream.num.map.output.key.field=1 \
-input ../data/part2/stackLarge.txt \
-output output1/ \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py

hadoop jar ../hadoop-streaming-2.7.3.jar \
-D  mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D  mapreduce.partition.keypartitioner.options=-k1,1 \
-D  mapreduce.partition.keycomparator.options=-k1,1nr \
-D  stream.num.map.output.key.field=1 \
-input output1/ \
-output output2/ \
-mapper mapper2.py \
-file mapper2.py \
-combiner combiner2.py \
-file combiner2.py \
-reducer reducer2.py \
-file reducer2.py

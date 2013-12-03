#!/bin/bash
#PBS -N job_cpu_image
#PBS -l nodes=1:gpus=1,walltime=10:00:00
#PBS -d /home/odeshmukh/work/project/Base

for i in {1..14}
do
  ./a.out -f $i -x 8192 -y 8192 >> log_filter
done
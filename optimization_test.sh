#!/bin/bash

maxIter=(  100 200 300 400 500 600 700 800 900 1000 1500 2000 2500  )
solvee=(  adam sgd l-bfgs  )
rater=(  constant invscaling adaptive  )

for i in ${maxIter[@]}
do
	for k in ${solvee[@]}
	do
		for j in ${rater[@]}
		do
			python NeuralLearner_vPaul.py $i $j $k
			rm ./data/weights/*
		done
	done
done
exit 0

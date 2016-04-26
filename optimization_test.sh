#!/bin/bash

maxIter=(  25 50 75 100 200 300 400 500 600 700 800  )
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

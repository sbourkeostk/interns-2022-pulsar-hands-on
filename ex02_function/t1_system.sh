bin/pulsar-admin functions create \
	--inputs persistent://public/default/in1 \
	--output persistent://public/default/out1 \
	--py /host/test_functions.py \
	--className test_functions.ExclamationFunction \
	--name t1

bin/pulsar-admin functions delete --name t1


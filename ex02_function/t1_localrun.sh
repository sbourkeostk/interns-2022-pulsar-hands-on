pulsar-admin functions localrun \
	--inputs persistent://public/default/in1 \
	--output persistent://public/default/out1 \
	--py /Users/sbourke/pulsar/ex02_function/test_functions.py \
	--className test_functions.ExclamationFunction

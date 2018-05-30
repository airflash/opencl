#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function
import numpy as np
import pyopencl as cl
import time

def runTestOnDevice(devices):
	#ctx = cl.create_some_context()	#initialize the context (use default device)
	ctx = cl.Context(devices) 
	queue = cl.CommandQueue(ctx)	#initialize a Queue

	mf = cl.mem_flags
	a_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
	b_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)

	t0 = time.time()

	prg = cl.Program(ctx, """
	__kernel void sum2(__global const float *a_g, __global const float *b_g, __global float *res_g)
	{		
		int len = get_global_size(0);
    	int gid = get_global_id(0);

    	for (int j=0; j<3; j++) {
	    	for (int i=0; i<len; i++) {
				res_g[gid] = a_g[gid] + b_g[i];
	    	}
    	}

    	//res_g[gid] = a_g[gid] + b_g[gid];
	}

	__kernel void sum(__global const float *a_g, __global const float *b_g, __global float *res_g)
	{				
    	int gid = get_global_id(0);
    	res_g[gid] = a_g[gid] + b_g[gid];
	}

	__kernel void mul(__global const float *a_g, __global const float *b_g, __global float *res_g)
	{				
    	int gid = get_global_id(0);
    	res_g[gid] = a_g[gid] * b_g[gid];
	}

	__kernel void hard(__global const float *a_g, __global const float *b_g, __global float *res_g)
	{				
    	int gid = get_global_id(0);
    	res_g[gid] = 0;
    	for(int i=0; i<1000; i++) {
    		res_g[gid] += sin(a_g[gid]) * cos(b_g[gid]);
    	}
	}
	""").build()

	res_g = cl.Buffer(ctx, mf.WRITE_ONLY, a_np.nbytes)
	prg.hard(queue, a_np.shape, None, a_g, b_g, res_g)

	res_np = np.empty_like(a_np)
	cl.enqueue_copy(queue, res_np, res_g)

	t1 = time.time()

	#print(res_np)
	print(devices[0].name , " time: " , t1 - t0)

	# Check on CPU with Numpy:
	#print("-------------------------")
	#print(res_np - (a_np + b_np))
	#print(np.linalg.norm(res_np - (a_np + b_np)))


a_np = np.random.rand(20000000).astype(np.float32)
b_np = np.random.rand(20000000).astype(np.float32)

platforms = cl.get_platforms()

print()
print("------ all platforms --------")
for val in platforms:
	print(val)


# print()
# print("------ CPU devices in platforms -----------")

# for val in platforms:
# 	my_cpu_devices = val.get_devices(device_type=cl.device_type.CPU) 
# 	print(my_cpu_devices)

print()
print("------ GPU devices in platforms -----------")

for val in platforms:
	my_gpu_devices = val.get_devices(device_type=cl.device_type.GPU) 	#can be used without param
	print(my_gpu_devices)

print()
print("-----------------------------------")

for val in platforms:
	my_devices = val.get_devices() 	# device_type=cl.device_type.GPU
	if (my_devices):
		runTestOnDevice([my_devices[0]])	
	
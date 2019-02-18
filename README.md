основа: https://documen.tician.de/pyopencl/
еще	инфо про OpenCL https://habr.com/post/124925/


----------------------------------------
2019.02.18
Windows, home

1. pip install numpy					OK
2. качаю pyopencl.whl
3. pip install *.whl					OK	(версия 2.1 не заработала, 1.2 ок)


------ all platforms --------
<pyopencl.Platform 'NVIDIA CUDA' at 0x9791db0>
<pyopencl.Platform 'Intel(R) OpenCL' at 0xa217600>

------ GPU devices in platforms -----------
[<pyopencl.Device 'GeForce GTX 1060 6GB' on 'NVIDIA CUDA' at 0x97921c0>]
[]

-----------------------------------
GeForce GTX 1060 6GB  time:  0.7100405693054199
Intel(R) Core(TM) i5-3570 CPU @ 3.40GHz  time:  23.025317192077637




----------------------------------------
2018.. в офисе Skywind

Windows:
pip install pyopencl
	-> ошибка, нет Mako
pip install Mako
pip install pyopencl
	-> ошибка, нет MSVC что то там, 
	ставлю по ссылке в описании ошибки
pip install pyopencl
	-> ошибка, fatal error C1083: Cannot open include file: 'CL/cl.h'
	качаю и ставлю сам Intel SDK for OpenCL
	pip install pyopencl
-> нет, нихуя
	качаю и ставлю ATI OpenCL Drivers (зря)
...
мне не нужно собирать PyOpenCl из исходников (что пытается сделать pip install)
качаю wql с https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopencl (качать соответствующую версии и разрадяности питона сборку)
pip install *.wql
...
DONE!


ноут на работе
	AMD Radeon R7 M360
	Intel(R) HD Graphics 520

	AMD круче интела в разы

AMD OpenCL 2.0 driver
https://support.amd.com/en-us/kb-articles/Pages/OpenCL2-Driver.aspx

Intel OpenCL Driver
https://software.intel.com/en-us/intel-opencl


Anconda - дистрибутив Python + R + куча научных библиотек типа SciPy + менеджер пакетов conda
Miniconda - то же урезанное, для новичков лучше полную
основа: https://documen.tician.de/pyopencl/



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
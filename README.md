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
качаю wql с https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopencl
pip install *.wql
...
DONE!
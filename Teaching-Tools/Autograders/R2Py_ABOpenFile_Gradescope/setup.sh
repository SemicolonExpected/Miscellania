#! /bin./bash


#made by Victoria Zhong

apt install apt-transport-https dirmngr
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb https://download.mono-project.com/repo/ubuntu vs-bionic main" | tee /etc/apt/sources.list.d/mono-official-vs.list
dpkg --add-architecture i386 
apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main'

apt-get update
apt install --install-recommends winehq-stable
apt-get install -y python python-pip python-dev
pip install gradescope-utils
pip install subprocess32

apt-get install -qy git
git clone https://github.com/SeattleTestbed/repy_v2
cd repy_v2/scripts
python initialize.py
mkdir /autograder/source/assignment
python build.py /autograder/source/assignment

cd /autograder/source
cp attackcase*.r2py ./assignment
cp run_tests.py ./assignment
cp test.py ./assignment
#apt-get install -qy nunit nunit-console mono-complete monodevelop-nunit libnunit-framework2.6.3-cil libnunit-core2.6.3-cil libnunit-core-interfaces2.6.3-cil  libnunit-cil-dev libnunit-console-runner2.6.3-cil
#wget https://dist.nuget.org/win-x86-commandline/latest/nuget.exe
#mono nuget.exe install

# helloworld-conan

This sample is showing you how you can use conan to compile your c++ application. I also used **docker** to run this hello world app via a docker container.

## Environment Setup

Make sure **g++** installed. If not, go to [Build and run your first application with g++](http://kabiliravi.com/index.php/software/programming/mycpptutorial/environment-setup/build-and-run-your-first-application-with-gcc/) for more help.

Also make sure **make** command is installed. If not go to [Build and run your first application with make](http://kabiliravi.com/index.php/software/programming/mycpptutorial/environment-setup/build-and-run-your-first-application-with-make/) for more help.

And make sure **cmake** command is installed. If not go to [Build and run your first application with cmake](http://kabiliravi.com/index.php/software/programming/mycpptutorial/environment-setup/build-and-run-your-first-application-with-cmake/) for more help.


The easiest way to install **conan** is using **python** package manager **pip** and since you eventually need python to write parts of your build scripts, first we install **python3** and **pip3** and then we install conan using pip3.

In order to install python3 and pip, for:

  - MacOS
    ```
    $ brew install python3
    $ sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $ sudo python3 get-pip.py
    ```
  -
    ```
    $ sudo apt install python3
    $ sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $ sudo python3 get-pip.py
    ```

For MacOS you can install conan using **brew** command also:

```
$ brew update
$ brew install conan
```    

And for Arch linux, if you have yay package manager installed:

```
$ yay -S conan
```

After you installed python you can easily install conan with pip and the instructions is same for all operating systems.

```
$ pip3 install conan
```

## Building Hello World application

Create a folder called *build* and then use *conan install* command to build the application.
Visit [Build and run your first application with conan](http://kabiliravi.com/index.php/software/programming/mycpptutorial/environment-setup/build-and-run-your-first-application-with-conan/) to get more information about how to setup a conan configuration for you c++ application.

```
$ mkdir build
$ cd build
$ conan install ..
```


For Linux and Mac:
```
$ cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release
$ cmake --build .
```

For Windows:
```
$ cmake .. -G "Visual Studio <VS-VERSION> Win64"
$ cmake --build . --config Release
```

## Running the app

Run *greet* command like this:

```
$ ./bin/greet
Hello World!
```

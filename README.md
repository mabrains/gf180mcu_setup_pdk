GF180MCU PDK Setup for Klayout
==============================

[![License](https://img.shields.io/badge/license-Apache_v2-blue)](/LICENSE) 

[<p align="center"><img src="images/mabrains.png" width="700">](http://mabrains.com/)

## Prerequisites

At a minimum:

- python 3.10+
- python3-venv
- klayout 0.29.11+

## Installation

To begin, create a new directory that will contain all gf180mcu setup files and environment configurations:

```bash
mkdir gf180mcu_setup && cd gf180mcu_setup/
```

Next, clone the project into the current directory you have created:

```bash
git clone https://github.com/mabrains/gf180mcu_setup_pdk.git
```

Afterward, you will need to create a python virtual environment:

```bash
python3 -m venv ./gf180mcu_env && source ./gf180mcu_env/bin/activate
```

And then:

```bash
cd gf180mcu_setup_pdk
```

Subsequently, to install the required Python packages, execute the following command:

```bash
pip install -r requirements.txt
```

> **Note:** This project uses an older version of `gdsfactory` to remain compatible with the custom PCells developed for the GF180MCU PDK.

If you don't have the PDK already installed, you will need to define the following environment variables and run the installation script as explained:

```bash
- PDK_ROOT: the directory where the PDKs will be installed.
- PDK: the desired PDK variant from the supported list.
```

To do that, you need to run the following:

```bash
export PDK_ROOT=$HOME/pdks  
export PDK=gf180mcuC  
chmod +x install_pdk.sh  
./install_pdk.sh
```

If you already have the PDK installed, you can skip the step above, but make sure your KLayout tech directory follows the structure below:

```
$PDK_ROOT/$PDK$/libs.tech/klayout
├── drc
├── lvs
└── tech
    ├── drc
    ├── gf180mcu.lyp
    ├── gf180mcu.lyt
    ├── gf180mcu.map
    ├── lvs
    ├── macros
    │   ├── drc_options.yml
    │   ├── gf180mcu_drc.lydrc
    │   ├── gf180mcu_lvs.lylvs
    │   ├── gf180mcu_options.lym
    │   ├── lvs_options.yml
    │   └── run_drc_main
    └── pymacros
        ├── cells
        └── gf180mcu.lym
```

Lastly, to install the GF180MCU PDK for the KLayout tool, execute the following command:

Make sure that the tech path exists at `$PDK_ROOT/$PDK/libs.tech/klayout/` and that both `$PDK_ROOT` and `$PDK` are defined correctly.

```bash
python3 setup_klayout.py --tech_path=$PDK_ROOT/$PDK/libs.tech/klayout/ --klayout_home=$PWD/../gf180mcu_klayout --python_env=$PWD/../gf180mcu_env/
```

This will install the GF180MCU PDK technology in the KLayout tool. You can then open it by executing the following command:

This script will create a symbolic link to the KLayout tech, It also sets up the Python environment path and adds a `klayout_gf180mcu` alias to your shell configuration.
You need to open a new terminal after running the script for the alias to take effect.

You can then open KLayout using:

```bash
klayout_gf180mcu
```

Or open a pre-existing layout, you can use the following command:

```bash
klayout_gf180mcu <your_layout_file>
```

Example:

```bash
klayout_gf180mcu test_example/nfet_03v3.gds
```

## About Mabrains

Mabrains was founded to achieve the main purpose to change the world of Chip Design using AI. Empowering the world with a new methodologies and techniques that would disrupt the status quo in the EDA industry.

We have contributed in developing many PDKs for Open Source Tools. For more information, please refer to [Mabrains-Github](https://github.com/mabrains).

## Contact-Us

Requests for more information about Generic PDK and other open source technologies can be [submitted via this web form](https://mabrains.com/#contactus).

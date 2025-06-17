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

Before running the script, you must define two environment variables:

- `PDK_ROOT`:  the directory where the PDKs will be installed.
- `PDK`:  the desired PDK variant from the supported list above.

Example:

```bash
export PDK_ROOT=$HOME/pdks
export PDK=gf180mcuD
chmod +x install_pdk.sh
./install_pdk.sh
```

Lastly, to install the GF180MCU PDK for the KLayout tool, execute the following commands:

```bash
python3 setup_klayout.py --tech_path=$PDK_ROOT/$PDK/libs.tech/klayout/ --klayout_home=$PWD/../gf180mcu_klayout --python_env=$PWD/../gf180mcu_env/ 
```

This will install the GF180MCU PDK technology in the KLayout tool. You can then open it by executing the following command:

> **Note**: Open a new terminal before executing the following command.

```bash
klayout_gf180mcu
```

Alternatively, to open a pre-existing layout, you can use the following command:

```bash
klayout_gf180mcu <your_layout_file>
```

Example:

```bash
klayout_gf180mcu test_example/nmos.gds
```

## About Mabrains

Mabrains was founded to achieve the main purpose to change the world of Chip Design using AI. Empowering the world with a new methodologies and techniques that would disrupt the status quo in the EDA industry.

We have contributed in developing many PDKs for Open Source Tools. For more information, please refer to [Mabrains-Github](https://github.com/mabrains).

## Contact-Us

Requests for more information about Generic PDK and other open source technologies can be [submitted via this web form](https://mabrains.com/#contactus).

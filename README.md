# IEEE 1547.1 Interoperability Agent

[//]: # (![Eclipse VOLTTRON 10.0.5rc0]&#40;https://img.shields.io/badge/Eclipse%20VOLTTRON-10.0.5rc0-red.svg&#41;)

[//]: # (![Python 3.10]&#40;https://img.shields.io/badge/python-3.10-blue.svg&#41;)

[//]: # (![Python 3.11]&#40;https://img.shields.io/badge/python-3.11-blue.svg&#41;)

[//]: # ([![pypi version]&#40;https://img.shields.io/pypi/v/volttron-interoperability.svg&#41;]&#40;https://pypi.org/project/volttron-interoperability/&#41;)

[//]: # ()
[//]: # (Main branch tests:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![Main Branch Passing?]&#40;https://github.com/eclipse-volttron/volttron-interoperability/actions/workflows/run-tests.yml/badge.svg?branch=main&#41;]&#40;https://github.com/eclipse-volttron/volttron-interoperability/actions/workflows/run-tests.yml&#41;)

[//]: # ()
[//]: # (Develop branch tests:&nbsp;&nbsp; [![Develop Branch Passing?]&#40;https://github.com/eclipse-volttron/volttron-interoperability/actions/workflows/run-tests.yml/badge.svg?branch=develop&#41;]&#40;https://github.com/eclipse-volttron/volttron-interoperability/actions/workflows/run-tests.yml&#41;)

The VOLTTRON interoperability agent provides a standard, protocol-agnostic interface for
Distributed Energy Resources (DER) devices by mapping IEC 61850-7-420 data models to protocols such as SunSpec Modbus,
IEEE 1815.2, IEEE 2030.5, and custom protocols, in line with IEEE 1547 standards.
It translates the required functionalities into specific protocols for device control.
An actor wishing to communicate with devices using multiple protocols
compliant with IEEE 1547 can use the interoperability agent to manage all such devices.
The actor issues commands using IEC 61850-7-420 names, which the interoperability agent maps to specific protocols,
such as SunSpec Modbus, MESA-DER (DNP3), or IEEE 2030.5. The corresponding points are then commanded on the devices
via the VOLTTRON Platform Driver.

## Requirements

* python >= 3.10
* volttron >= 10.0 

## Documentation

More detailed documentation can be found on
[ReadTheDocs](https://eclipse-volttron.readthedocs.io/en/latest/external-docs/volttron-interoperability/index.html).

## Agent Configuration

The interoperability agent uses a JSON formatted configuration file:

```json
    {
      "targets": {
        "my_bess": {
          "target_type": "sunspec_modbus",
          "driver_device_topic": "sunspec"
        },
        "your_device": {
          "target_type": "ieee_1815_2"
        }
      }
} 
```

The configuration file should be stored in the VOLTTRON
configuration store. For an interoperability agent installed using the VIP identity
`der.interoperability`, the following command may be used to store the configuration:

```shell
vctl config store der.interoperability config path/to/config/file
```

The configuration file should contain a dictionary (JSON object) with a `targets` key. Each entry in `targets`
should also be a dictionary which contains the configuration for one device with which communication is being
managed. The key of each target is a user-chosen identifier for the target device. The value should be a dictionary
accepting at least the following parameters as keys:

| Parameter      | Required  | Type   | Description                                                                                                                                 |
|----------------|-----------|--------|---------------------------------------------------------------------------------------------------------------------------------------------|
| target_type    | true      | string | The class of device. This should be a type of device for which a mapping has been included or for which a user-defined mapping is available |
| target_module  | false     | string | The python module, for custom mappings, in wihch the target mapping can be found.                                                           |
| taget_class    | false     | string | The class name of the target type. This is not required for built-in mappings.                                                              | 

Additional configurations will be passed to the target mapping class. The `sunspec_modbus` and `ieee_1815.2` device types take the following parameters:

| Parameter           | Required | Type   | Description                                                                                      |
|---------------------|----------|--------|--------------------------------------------------------------------------------------------------|
| driver_device_topic | true     | string | The VOLTTRON topic with which to address the VOLTTRON driver for communication with this device. |


## Installation

Before installing, VOLTTRON should be installed and running.  Its virtual environment should be active.
Information on how to install of the VOLTTRON platform can be found
[here](https://github.com/eclipse-volttron/volttron-core).

#### Install and start the IEEE 1547.1 Interoperability Agent:

```shell
vctl install volttron-interoperability --vip-identity der.interoperability --tag 1547 --start
```

#### View the status of the installed agent

```shell
vctl status
```
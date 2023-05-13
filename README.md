# gngdownloader

Setup downloader and mover for Grid and Go setups. This is an unofficial tool, no relation to Grid and Go.

> :warning: I'm not a professional coder - this code works but it can definately be inproved. I take no responsibility for its use.

## Description

This is a simple tool to download Grid and Go setups and move them to your iRacing setup folder with a neat folder structure. 

You need a valid subscription and you can only download setups you have access to.

Currently supported series:
* GT-Sprint
* Gt4 Challenge
* IMSA
* NEC
* PCUP

Default behaviour: Download and move the setups to the provided iRacing setup folder path. The tool will create a folder for the current track.

## Getting Started

### Dependencies

* Python (min. 3.9)
* selenium
* art
* configparser

### Config

There is a config.ini file where you specifiy your GNG account details and paths. 

There is also a block called SERIES where you can select the series the tool will download the setups for. By default, all series are set to true, if you don't want one you can just set them to false.

### Executing program

You can simply run the main file without any parameters:
```
python GNGdownloader.py
```


## Authors

Feel free to reach out:

Kai Renz  
[@kairenz1990](https://twitter.com/kairenz1990)

## Version History

* 0.1
    * Initial Release

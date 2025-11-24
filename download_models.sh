#!/usr/bin/env bash
# Helper script to download MobileNet-SSD model files into the project directory


PROTOURL="https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/MobileNetSSD_deploy.prototxt"
MODELURL="https://github.com/chuanqi305/MobileNet-SSD/raw/master/MobileNetSSD_deploy.caffemodel"


echo "Downloading prototxt..."
curl -L -o MobileNetSSD_deploy.prototxt.txt "$PROTOURL"


echo "Downloading caffemodel (this can be large)..."
curl -L -o MobileNetSSD_deploy.caffemodel "$MODELURL"


echo "Done."

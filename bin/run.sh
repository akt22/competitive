#!/bin/bash

set -e

ROOT=$(cd $(dirname $0); pwd)/../kotlin

FILE=$(basename $1)
FILE_NAME="${FILE%%.*}"
JAR="${ROOT}/out/${FILE_NAME}.jar"

kotlinc $1 -include-runtime -d ${JAR}
echo "info: compile finished."
kotlin ${JAR}


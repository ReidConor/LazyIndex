#! /bin/bash

JOB_NAME="LazyIndex"
JOB_DIR=`pwd`
FILE_NAME=$(basename $1)
DATA_DIR=`cd $(dirname $1); pwd`


#https://dev.to/thiht/shell-scripts-matter
info()    { echo "[INFO]    $@"  ; }
warning() { echo "[WARNING] $@"  ; }
error()   { echo "[ERROR]   $@"  ; }
fatal()   { echo "[FATAL]   $@"  ; }

init(){
  clear
  info "-----------------------"
  info "  $JOB_NAME Started    "
  info "-----------------------"

  info "File name is "$FILE_NAME
  info "File is located at "$DATA_DIR

}

convertToText(){
  cd $DATA_DIR
  info "Converting $FILE_NAME to text."
  pdftotext $FILE_NAME
  info "Converted. "

}


calculateIndex(){
  info "Passing to Python to calculate index."
  cd $JOB_DIR
  python LazyIndex.py ${DATA_DIR}/${FILE_NAME%.*}.txt
  info "Calculated."

}


cleanUp(){
  info "Cleaning up."
  cd $DATA_DIR
  rm ${FILE_NAME%.*}.txt
  info "Cleaned."

}

main(){
  init

  convertToText $1

  calculateIndex

  cleanUp

  info "Done."

}

main $1

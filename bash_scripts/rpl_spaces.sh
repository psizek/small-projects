#!/bin/bash
echo This program changes filename spaces to underscores for every file in the directory (recursively).
echo Directory to modify contents of:
read dir
if [[ ! -d $dir ]]; then
exit
fi

regex=' '

loopingfunction() {
opwd=`pwd`
cd $1

for file in *; do
if [[ "$file" =~ $regex ]]; then #=~ is a regex evaluation expression.
modified=`echo $file | tr ' ' '_'`
mv -n "$file" "$modified"
fi
if [[ -d $file ]]; then
loopingfunction $file
fi
done

cd $opwd
}

loopingfunction $dir

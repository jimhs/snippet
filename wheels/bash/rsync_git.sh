#!/usr/bin/env bash

source $HOME/.self/.exports

NOW=$(date +"@%b.%d")

# todo: how to bypass unchanged files
for file in $GIT_FILES
do
	if [ -a $HOME_$file ]
	then
		rsync -az $HOME_$file $DEST_
	fi
done

pushd $GIT_
git add -A
git commit -m "$NOW"
git push
popd
